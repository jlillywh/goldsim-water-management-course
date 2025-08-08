param(
    [Parameter(Mandatory=$true)]
    [string]$LessonImagesPath,
    
    [int]$MaxWidth = 1200,
    [int]$MaxHeight = 800,
    [int]$Quality = 85
)

$processedDir = Join-Path $LessonImagesPath "processed"
$webDir = Join-Path $LessonImagesPath "web"

Write-Host "Optimizing images for web deployment..." -ForegroundColor Green
Write-Host "Source: $processedDir" -ForegroundColor Gray
Write-Host "Destination: $webDir" -ForegroundColor Gray

# Ensure web directory exists
if (!(Test-Path $webDir)) {
    New-Item -ItemType Directory -Path $webDir -Force
    Write-Host "Created web directory: $webDir" -ForegroundColor Green
}

# Check if ImageMagick is available
$magickCmd = Get-Command "magick" -ErrorAction SilentlyContinue
if (!$magickCmd) {
    Write-Warning "ImageMagick not found. Attempting simple copy instead..."
    $useImageMagick = $false
} else {
    Write-Host "Using ImageMagick for optimization" -ForegroundColor Green
    $useImageMagick = $true
}

# Get all PNG files from processed directory
$imageFiles = Get-ChildItem -Path $processedDir -Filter "*.png" -ErrorAction SilentlyContinue

if ($imageFiles.Count -eq 0) {
    Write-Warning "No PNG files found in processed directory: $processedDir"
    Write-Host "Make sure you have images in the processed folder before optimizing."
    exit 1
}

Write-Host "Found $($imageFiles.Count) images to optimize" -ForegroundColor Yellow

foreach ($imageFile in $imageFiles) {
    $inputFile = $imageFile.FullName
    $outputFile = Join-Path $webDir $imageFile.Name
    
    try {
        if ($useImageMagick) {
            # Use ImageMagick for optimization
            $resizeParam = "${MaxWidth}x${MaxHeight}>"
            & magick convert "$inputFile" -resize $resizeParam -quality $Quality "$outputFile"
            
            if ($LASTEXITCODE -eq 0) {
                $originalSize = (Get-Item $inputFile).Length
                $newSize = (Get-Item $outputFile).Length
                $savings = [math]::Round((($originalSize - $newSize) / $originalSize) * 100, 1)
                Write-Host "  ✓ $($imageFile.Name) (${savings}% size reduction)" -ForegroundColor Green
            } else {
                throw "ImageMagick conversion failed"
            }
        } else {
            # Simple copy if ImageMagick not available
            Copy-Item $inputFile $outputFile -Force
            Write-Host "  ✓ $($imageFile.Name) (copied without optimization)" -ForegroundColor Yellow
        }
    }
    catch {
        Write-Warning "Failed to process $($imageFile.Name): $($_.Exception.Message)"
        # Try simple copy as fallback
        Copy-Item $inputFile $outputFile -Force
        Write-Host "  ⚠ $($imageFile.Name) (fallback copy)" -ForegroundColor Yellow
    }
}

Write-Host "`nOptimization complete!" -ForegroundColor Green
Write-Host "Optimized images saved to: $webDir" -ForegroundColor Gray

# Generate markdown image list for easy copy-paste into lesson.md
Write-Host "`n" + "="*60 -ForegroundColor Cyan
Write-Host "MARKDOWN IMAGE REFERENCES" -ForegroundColor Cyan
Write-Host "="*60 -ForegroundColor Cyan
Write-Host "Copy these lines into your lesson.md Assets section:" -ForegroundColor White
Write-Host ""

Get-ChildItem -Path $webDir -Filter "*.png" | Sort-Object Name | ForEach-Object {
    $description = $_.BaseName -replace "^\d+-\d+-\d+-", "" -replace "-", " "
    $description = (Get-Culture).TextInfo.ToTitleCase($description.ToLower())
    Write-Host "- ``$($_.Name)``: $description screenshot" -ForegroundColor Yellow
}

Write-Host "`n" + "="*60 -ForegroundColor Cyan
Write-Host "Ready for deployment! Run:" -ForegroundColor Green
Write-Host ".\Deploy-Lesson-Images.ps1 -UnitNumber [##] -LessonNumber [##] -LessonImagesPath '$LessonImagesPath'" -ForegroundColor Yellow
