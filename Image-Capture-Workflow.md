# Image Capture and Organization Automation for GoldSim Water Management Course

## Overview
This document outlines the automated workflow for capturing, organizing, and deploying lesson images during course development using a centralized capture approach with UULL naming convention.

## UULL Naming Convention

**Format**: `[UU] [LL] [LessonName]-[sequence]-[description].png`

**Examples**:
- `04 01 Introduction to Water Demand-01-concepts-diagram.png`
- `04 01 Introduction to Water Demand-02-goldsim-setup.png`
- `04 02 Municipal Water Modeling-01-reservoir-config.png`
- `07 03 Modeling Wells and Pumping-01-well-boundary.png`
- `07 05 Managed Aquifer Recharge-12-results-analysis.png`

**Breakdown**:
- **04** = Unit Number (always 2 digits)
- **01** = Lesson Number (always 2 digits)  
- **Introduction to Water Demand** = Lesson Name (natural spacing)
- **01** = Sequence Number (2+ digits)
- **concepts-diagram** = Description (kebab-case)

## Centralized Workflow

### Phase 1: One-Time Setup
**Configure SnagIt Once:**
- Set default save location to: `c:\temp\course-captures\`
- Use UULL naming convention for all captures
- No need to change SnagIt settings for different lessons

### Phase 2: Automated Sorting

**PowerShell Script: `Sort-Captured-Images.ps1`**
- Reads all images from central capture directory
- Parses UULL naming to determine unit/lesson
- Automatically moves images to correct lesson folders
- Creates proper directory structure (raw/processed/web)
- Handles naming format standardization

## Directory Structure After Sorting

Each lesson gets images organized as follows:
```
[Unit-Directory]/
├── Lesson_XX-[Lesson-Name]/
│   ├── lesson.md
│   └── images/
│       ├── raw/          # Original captures (moved here automatically)
│       ├── processed/    # Edited/annotated versions  
│       └── web/          # Web-optimized versions
```

## Complete Automated Workflow

### One-Time Setup:
```powershell
# Configure central capture location and SnagIt
.\Organize-Lesson-Images.ps1
```

### For Each Lesson Development Session:

1. **Capture Screenshots**
   - Use SnagIt with central location configured
   - Name files with UULL convention as you capture
   - Example: `04 01 Introduction to Water Demand-01-goldsim-startup.png`

2. **Sort Images into Lesson Folders**
   ```powershell
   # Dry run to see what will happen
   .\Sort-Captured-Images.ps1 -DryRun
   
   # Actually move the images
   .\Sort-Captured-Images.ps1
   ```

3. **Optimize for Web**
   ```powershell
   .\Optimize-Images-For-Web.ps1 -LessonImagesPath "[lesson-path]\images"
   ```

4. **Safe Staging for Review**
   ```powershell
   .\Safe-Stage-Images.ps1 -UnitNumber "04" -LessonNumber "01" -LessonImagesPath "[lesson-path]\images"
   ```

## Advanced Features

### Smart Directory Detection
- Script automatically finds lesson directories by pattern matching
- Handles various unit naming conventions (04-Water-Demand-and-Use, etc.)
- Creates missing image directory structure

### Error Handling
- Reports unrecognized file names
- Shows available lessons if target not found
- Provides helpful naming examples

### Safety Features
- Dry run mode to preview operations
- Moves originals to raw/ and copies to processed/
- Preserves original captures while enabling editing workflow

## Quick Reference Commands

```powershell
# Setup (run once)
.\Organize-Lesson-Images.ps1

# Sort captured images (run after each capture session)
.\Sort-Captured-Images.ps1

# Optimize for web (run when lesson images are ready)
.\Optimize-Images-For-Web.ps1 -LessonImagesPath "[path-to-lesson]\images"

# Stage for safe deployment (run before web server deployment)
.\Safe-Stage-Images.ps1 -UnitNumber "XX" -LessonNumber "XX" -LessonImagesPath "[path-to-lesson]\images"
```

## Benefits of Centralized Approach

1. **Single SnagIt Configuration** - Set it once, works for all lessons
2. **Batch Processing** - Capture multiple lessons worth of images, then sort
3. **Flexible Workflow** - Can capture images out of order and sort later
4. **Error Prevention** - Consistent naming prevents organizational mistakes
5. **Scalability** - Easy to manage hundreds of images across dozens of lessons

**PowerShell Script: `Optimize-Images-For-Web.ps1`**

```powershell
param(
    [Parameter(Mandatory=$true)]
    [string]$LessonImagesPath
)

$processedDir = Join-Path $LessonImagesPath "processed"
$webDir = Join-Path $LessonImagesPath "web"

# Use ImageMagick or similar for optimization
Get-ChildItem -Path $processedDir -Filter "*.png" | ForEach-Object {
    $inputFile = $_.FullName
    $outputFile = Join-Path $webDir $_.Name
    
    # Optimize for web (resize if needed, compress)
    # This assumes ImageMagick is installed
    & magick convert "$inputFile" -resize "1200x800>" -quality 85 "$outputFile"
    
    Write-Host "Optimized: $($_.Name)"
}
```

## Web Server Integration

### Web Server Path Structure
**Assumption:** Web server accessible at `\\webserver\course-content\` or similar

```
webserver/
├── course-content/
│   ├── images/
│   │   ├── 01-getting-started/
│   │   ├── 02-climate-drivers/
│   │   ├── 03-surface-flow/
│   │   ├── 04-water-demand/
│   │   ├── 05-hydraulic-controls/
│   │   ├── 06-reservoir-operations/
│   │   ├── 07-groundwater/
│   │   └── [etc...]
│   └── models/
│       └── [GoldSim model files]
```

### Deployment Script

**PowerShell Script: `Deploy-Lesson-Images.ps1`**

```powershell
param(
    [Parameter(Mandatory=$true)]
    [string]$UnitNumber,
    
    [Parameter(Mandatory=$true)]
    [string]$LessonNumber,
    
    [Parameter(Mandatory=$true)]
    [string]$WebServerPath = "\\webserver\course-content\images"
)

$localWebDir = Get-ChildItem -Path "c:\Users\JasonLillywhite\OneDrive - GoldSim\work\GoldSimOnlineCourse\goldsim-water-management-course\$UnitNumber-*\Lesson_$LessonNumber-*\images\web"

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
}

$webUnitDir = Join-Path $WebServerPath $unitName
$webLessonDir = Join-Path $webUnitDir "lesson-$LessonNumber"

# Create web directories
if (!(Test-Path $webLessonDir)) {
    New-Item -ItemType Directory -Path $webLessonDir -Force
}

# Copy optimized images
Copy-Item -Path "$localWebDir\*" -Destination $webLessonDir -Force

Write-Host "Deployed images to: $webLessonDir"

# Generate markdown image references for easy copy-paste
Write-Host "`nMarkdown references for lesson.md:"
Get-ChildItem -Path $webLessonDir -Filter "*.png" | ForEach-Object {
    $webUrl = "https://your-domain.com/course-content/images/$unitName/lesson-$LessonNumber/$($_.Name)"
    Write-Host "![Description]($webUrl)"
}
```

## Quick Start Usage

### For Each New Lesson:

1. **Setup lesson image directories:**
```powershell
.\Organize-Lesson-Images.ps1 -UnitNumber "04" -LessonNumber "02" -LessonName "Municipal-Water-Demand-Modeling"
```

2. **Configure SnagIt to save to the raw directory** (script will display path)

3. **Capture your screenshots** as you build the GoldSim model

4. **Process images** (edit, annotate in your preferred tool)

5. **Optimize for web:**
```powershell
.\Optimize-Images-For-Web.ps1 -LessonImagesPath "path\to\lesson\images"
```

6. **Deploy to web server:**
```powershell
.\Deploy-Lesson-Images.ps1 -UnitNumber "04" -LessonNumber "02"
```

## Naming Conventions

### Image File Names
Format: `[unit]-[lesson]-[sequence]-[description].png`

Examples:
- `04-02-01-goldsim-new-model.png`
- `04-02-02-add-reservoir-element.png`
- `04-02-03-configure-municipal-demand.png`
- `04-02-04-demand-time-series-setup.png`
- `04-02-05-results-demand-vs-supply.png`

### Web URLs
Format: `https://your-domain.com/course-content/images/[unit-name]/lesson-[number]/[filename].png`

Example:
`https://your-domain.com/course-content/images/water-demand/lesson-02/04-02-03-configure-municipal-demand.png`

## Integration with Lesson Development

### Automatic Asset List Generation
Each script can generate asset lists for the lesson.md file:

```markdown
### Images Required
- `04-02-01-goldsim-new-model.png`: Screenshot showing new model creation dialog
- `04-02-02-add-reservoir-element.png`: Adding Reservoir element from palette
- `04-02-03-configure-municipal-demand.png`: Configuring demand parameters in reservoir
- `04-02-04-demand-time-series-setup.png`: Setting up time series for demand variations
- `04-02-05-results-demand-vs-supply.png`: Results showing demand vs supply analysis
```

## Next Steps

1. **Confirm web server path** - What's the actual path/URL structure for your web server?
2. **Install ImageMagick** (if not already installed) for image optimization
3. **Customize SnagIt settings** for consistent capture quality
4. **Test workflow** with one lesson to refine the process

Would you like me to modify any part of this workflow or need clarification on the web server configuration?
```
