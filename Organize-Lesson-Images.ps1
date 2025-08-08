param(
    [string]$CentralCaptureDir = "c:\temp\course-captures",  # CONFIGURE SNAGIT TO SAVE HERE
    [string]$CourseRoot = "c:\Users\JasonLillywhite\OneDrive - GoldSim\work\GoldSimOnlineCourse\goldsim-water-management-course"
)

Write-Host "=== CENTRALIZED IMAGE CAPTURE ORGANIZATION ===" -ForegroundColor Green -BackgroundColor DarkBlue

# Create central capture directory if it doesn't exist
if (!(Test-Path $CentralCaptureDir)) {
    New-Item -ItemType Directory -Path $CentralCaptureDir -Force | Out-Null
    Write-Host "Created central capture directory: $CentralCaptureDir" -ForegroundColor Green
}

Write-Host "`n" + "="*80 -ForegroundColor Cyan
Write-Host "SNAGIT SETUP INSTRUCTIONS" -ForegroundColor Cyan
Write-Host "="*80 -ForegroundColor Cyan
Write-Host "1. Open SnagIt" -ForegroundColor White
Write-Host "2. Go to File > Preferences > Output" -ForegroundColor White
Write-Host "3. Set default save location to:" -ForegroundColor White
Write-Host "   $CentralCaptureDir" -ForegroundColor Yellow
Write-Host "`n4. Use UULL naming pattern:" -ForegroundColor White
Write-Host "   [UnitNumber][LessonNumber][LessonName]-[sequence]-[description].png" -ForegroundColor Yellow
Write-Host "`n   Examples:" -ForegroundColor White
Write-Host "   0401Introduction-to-Water-Demand-01-concepts-diagram.png" -ForegroundColor Green
Write-Host "   0401Introduction-to-Water-Demand-02-goldsim-setup.png" -ForegroundColor Green
Write-Host "   0402Municipal-Water-Modeling-01-reservoir-config.png" -ForegroundColor Green
Write-Host "   0703Modeling-Wells-and-Pumping-01-well-boundary.png" -ForegroundColor Green
Write-Host "="*80 -ForegroundColor Cyan

# Check for existing images in central location
$existingImages = Get-ChildItem -Path $CentralCaptureDir -Filter "*.png" -ErrorAction SilentlyContinue
if ($existingImages.Count -gt 0) {
    Write-Host "`nFound $($existingImages.Count) images in central capture directory:" -ForegroundColor Yellow
    
    # Group by unit/lesson for organization
    $imageGroups = $existingImages | Group-Object { 
        if ($_.BaseName -match '^(\d{2})(\d{2})([^-]+)') {
            "$($matches[1])-$($matches[2])-$($matches[3])"
        } else {
            "Unknown-Format"
        }
    }
    
    foreach ($group in $imageGroups) {
        Write-Host "`n  Unit/Lesson: $($group.Name)" -ForegroundColor Cyan
        $group.Group | ForEach-Object {
            Write-Host "    - $($_.Name)" -ForegroundColor Gray
        }
    }
    
    Write-Host "`nRun Sort-Captured-Images.ps1 to organize these into lesson folders" -ForegroundColor Green
} else {
    Write-Host "`nNo images found in central directory. Ready for new captures!" -ForegroundColor Green
}

Write-Host "`nNext steps:" -ForegroundColor White
Write-Host "1. Configure SnagIt with the path above" -ForegroundColor Gray
Write-Host "2. Capture images using UULL naming pattern" -ForegroundColor Gray
Write-Host "3. Run: .\Sort-Captured-Images.ps1" -ForegroundColor Yellow
Write-Host "4. Run: .\Optimize-Images-For-Web.ps1 for specific lessons" -ForegroundColor Gray
