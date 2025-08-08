param(
    [Parameter(Mandatory=$true)]
    [string]$UnitNumber,
    
    [Parameter(Mandatory=$true)]
    [string]$LessonNumber,
    
    [Parameter(Mandatory=$true)]
    [string]$LessonImagesPath,
    
    [string]$LocalStagingPath = "c:\temp\course-staging\images",  # SAFE LOCAL STAGING AREA
    [string]$WebDomain = "https://your-domain.com",  # UPDATE THIS DOMAIN ONLY
    [switch]$DryRun = $false  # SAFETY: Shows what would happen without doing it
)

Write-Host "SAFE DEPLOYMENT MODE - Preparing images for Unit $UnitNumber, Lesson $LessonNumber" -ForegroundColor Green

# Map unit numbers to web-friendly names
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
$stagingUnitDir = Join-Path $LocalStagingPath $unitName
$stagingLessonDir = Join-Path $stagingUnitDir "lesson-$LessonNumber"

Write-Host "Local source: $webDir" -ForegroundColor Gray
Write-Host "SAFE staging destination: $stagingLessonDir" -ForegroundColor Yellow
Write-Host "*** NO DIRECT WEB SERVER ACCESS ***" -ForegroundColor Red -BackgroundColor White

# Check if local web directory exists and has images
if (!(Test-Path $webDir)) {
    Write-Error "Web directory not found: $webDir"
    Write-Host "Run Optimize-Images-For-Web.ps1 first!"
    exit 1
}

$imageFiles = Get-ChildItem -Path $webDir -Filter "*.png"
if ($imageFiles.Count -eq 0) {
    Write-Warning "No images found in web directory: $webDir"
    exit 1
}

Write-Host "Found $($imageFiles.Count) images to stage" -ForegroundColor Yellow

if ($DryRun) {
    Write-Host "`n*** DRY RUN MODE - No files will be copied ***" -ForegroundColor Magenta
}

# Create staging directories
try {
    if (!(Test-Path $stagingUnitDir)) {
        if ($DryRun) {
            Write-Host "[DRY RUN] Would create: $stagingUnitDir" -ForegroundColor Cyan
        } else {
            New-Item -ItemType Directory -Path $stagingUnitDir -Force | Out-Null
            Write-Host "Created staging unit directory: $stagingUnitDir" -ForegroundColor Green
        }
    }
    
    if (!(Test-Path $stagingLessonDir)) {
        if ($DryRun) {
            Write-Host "[DRY RUN] Would create: $stagingLessonDir" -ForegroundColor Cyan
        } else {
            New-Item -ItemType Directory -Path $stagingLessonDir -Force | Out-Null
            Write-Host "Created staging lesson directory: $stagingLessonDir" -ForegroundColor Green
        }
    }
}
catch {
    Write-Error "Failed to create staging directories: $($_.Exception.Message)"
    exit 1
}

# Copy optimized images to staging area (NOT web server)
try {
    $imageFiles | ForEach-Object {
        $destPath = Join-Path $stagingLessonDir $_.Name
        if ($DryRun) {
            Write-Host "  [DRY RUN] Would copy: $($_.Name)" -ForegroundColor Cyan
        } else {
            Copy-Item $_.FullName $destPath -Force
            Write-Host "  ✓ Staged: $($_.Name)" -ForegroundColor Green
        }
    }
    
    if (!$DryRun) {
        Write-Host "`nStaging complete!" -ForegroundColor Green
        Write-Host "Images staged at: $stagingLessonDir" -ForegroundColor Gray
    }
}
catch {
    Write-Error "Failed to copy images to staging: $($_.Exception.Message)"
    exit 1
}

# Generate web URLs for lesson.md (hypothetical URLs for now)
Write-Host "`n" + "="*80 -ForegroundColor Cyan
Write-Host "HYPOTHETICAL WEB URLS FOR LESSON.MD" -ForegroundColor Cyan
Write-Host "="*80 -ForegroundColor Cyan
Write-Host "These URLs assume standard course structure:" -ForegroundColor White
Write-Host ""

$imageFiles | Sort-Object Name | ForEach-Object {
    $webUrl = "$WebDomain/course-content/images/$unitName/lesson-$LessonNumber/$($_.Name)"
    $altText = $_.BaseName -replace "^\d+-\d+-\d+-", "" -replace "-", " "
    $altText = (Get-Culture).TextInfo.ToTitleCase($altText.ToLower())
    Write-Host "![${altText}]($webUrl)" -ForegroundColor Yellow
}

Write-Host "`n" + "="*80 -ForegroundColor Cyan
Write-Host "NEXT STEPS - MANUAL WEB SERVER DEPLOYMENT" -ForegroundColor Cyan
Write-Host "="*80 -ForegroundColor Cyan
Write-Host "1. Review staged files at: $stagingLessonDir" -ForegroundColor White
Write-Host "2. Manually copy to web server when ready" -ForegroundColor White
Write-Host "3. Verify URLs work before updating lesson.md" -ForegroundColor White
Write-Host "4. Update WebDomain parameter once confirmed" -ForegroundColor White

Write-Host "`n⚠️  SAFE MODE: No direct web server access attempted" -ForegroundColor Yellow -BackgroundColor DarkRed
