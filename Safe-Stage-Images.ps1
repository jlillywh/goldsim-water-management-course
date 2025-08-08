# SAFE IMAGE STAGING AND REVIEW WORKFLOW
# This script stages images locally and creates deployment packages for manual review

param(
    [Parameter(Mandatory=$true)]
    [string]$UnitNumber,
    
    [Parameter(Mandatory=$true)]
    [string]$LessonNumber,
    
    [Parameter(Mandatory=$true)]
    [string]$LessonImagesPath,
    
    [string]$ReviewStagingPath = "c:\temp\course-image-review"
)

Write-Host "=== SAFE IMAGE STAGING FOR REVIEW ===" -ForegroundColor Green -BackgroundColor DarkBlue
Write-Host "Unit $UnitNumber, Lesson $LessonNumber" -ForegroundColor White

# Create comprehensive staging structure
$unitName = switch ($UnitNumber) {
    "01" { "getting-started" }
    "02" { "climate-drivers" }
    "03" { "surface-flow" }
    "04" { "water-demand" }
    "05" { "hydraulic-controls" }
    "06" { "reservoir-operations" }
    "07" { "groundwater" }
    "08" { "flow-network" }
    "09" { "water-quality" }
    "10" { "model-analyses" }
    "11" { "specialized-applications" }
    "12" { "risk-reliability" }
    default { "unit-$UnitNumber" }
}

$webDir = Join-Path $LessonImagesPath "web"
$reviewDir = Join-Path $ReviewStagingPath "$unitName-lesson-$LessonNumber"
$packageDir = Join-Path $reviewDir "deployment-package"

# Safety checks
if (!(Test-Path $webDir)) {
    Write-Error "Web images directory not found: $webDir"
    Write-Host "Run Optimize-Images-For-Web.ps1 first!"
    exit 1
}

$imageFiles = Get-ChildItem -Path $webDir -Filter "*.png"
if ($imageFiles.Count -eq 0) {
    Write-Warning "No images found to stage."
    exit 1
}

# Create review structure
New-Item -ItemType Directory -Path $reviewDir -Force | Out-Null
New-Item -ItemType Directory -Path $packageDir -Force | Out-Null

Write-Host "Created review directory: $reviewDir" -ForegroundColor Green

# Copy images to review area
$imageFiles | ForEach-Object {
    $destPath = Join-Path $packageDir $_.Name
    Copy-Item $_.FullName $destPath -Force
    Write-Host "  ✓ Staged for review: $($_.Name)" -ForegroundColor Gray
}

# Create deployment instructions
$instructionsPath = Join-Path $reviewDir "DEPLOYMENT-INSTRUCTIONS.txt"
$instructions = @"
SAFE DEPLOYMENT INSTRUCTIONS FOR UNIT $UnitNumber LESSON $LessonNumber
================================================================

REVIEW THESE IMAGES FIRST:
- Check that all images are appropriate for publication
- Verify image quality and content
- Ensure no sensitive information is visible

SUGGESTED WEB SERVER STRUCTURE:
/course-content/images/$unitName/lesson-$LessonNumber/

FILES TO DEPLOY:
$($imageFiles | ForEach-Object { "  - $($_.Name)" } | Out-String)

MANUAL DEPLOYMENT STEPS:
1. Review all images in: $packageDir
2. Create folder on web server: /course-content/images/$unitName/lesson-$LessonNumber/
3. Upload all images from deployment-package folder
4. Test URLs to ensure they work
5. Update lesson.md with confirmed URLs

HYPOTHETICAL URLS (UPDATE DOMAIN):
$($imageFiles | ForEach-Object { 
    $webUrl = "https://your-domain.com/course-content/images/$unitName/lesson-$LessonNumber/$($_.Name)"
    $altText = $_.BaseName -replace "^\d+-\d+-\d+-", "" -replace "-", " "
    $altText = (Get-Culture).TextInfo.ToTitleCase($altText.ToLower())
    "![${altText}]($webUrl)"
} | Out-String)

ASSET LIST FOR LESSON.MD:
### Images Required
$($imageFiles | ForEach-Object {
    $description = $_.BaseName -replace "^\d+-\d+-\d+-", "" -replace "-", " "
    $description = (Get-Culture).TextInfo.ToTitleCase($description.ToLower())
    "- ``$($_.Name)``: $description screenshot"
} | Out-String)

Created: $(Get-Date)
"@

$instructions | Out-File -FilePath $instructionsPath -Encoding UTF8

Write-Host "`n📋 Created deployment instructions: $instructionsPath" -ForegroundColor Cyan
Write-Host "📦 Images ready for review: $packageDir" -ForegroundColor Cyan

# Open review folder for easy access
Write-Host "`n🔍 Opening review folder..." -ForegroundColor Yellow
Start-Process explorer.exe -ArgumentList $reviewDir

Write-Host "`n✅ SAFE STAGING COMPLETE" -ForegroundColor Green
Write-Host "Next: Review images and deploy manually when ready" -ForegroundColor White
