@echo off
REM Quick Image Sorting for GoldSim Course Development
REM This batch file automatically sorts images from SnagIt to correct lesson folders
REM Files that don't meet UULL naming convention are ignored

cd /d "c:\Users\JasonLillywhite\OneDrive - GoldSim\work\GoldSimOnlineCourse\goldsim-water-management-course"

echo.
echo ================================================
echo   Quick Image Sort for GoldSim Course
echo ================================================
echo Source: C:\Users\JasonLillywhite\Documents\Snagit\OnlineCourse
echo Target: Course lesson folders
echo.

REM Always specify the SnagIt source directory
set SNAGIT_DIR=C:\Users\JasonLillywhite\Documents\Snagit\OnlineCourse

REM Check if SnagIt directory exists
if not exist "%SNAGIT_DIR%" (
    echo ❌ SnagIt directory not found: %SNAGIT_DIR%
    echo Please check your SnagIt output configuration.
    echo.
    pause
    exit /b 1
)

REM Check if we want to do a dry run
if "%1"=="--dry-run" (
    echo Running in DRY RUN mode...
    echo Files that don't match UULL naming will be ignored.
    echo.
    python sort_images.py --source "%SNAGIT_DIR%" --dry-run
) else if "%1"=="-d" (
    echo Running in DRY RUN mode...
    echo Files that don't match UULL naming will be ignored.
    echo.
    python sort_images.py --source "%SNAGIT_DIR%" --dry-run
) else (
    echo Moving UULL-named images to lesson folders...
    echo Non-matching files will be ignored and left in SnagIt folder.
    echo.
    python sort_images.py --source "%SNAGIT_DIR%"
)

echo.
if %errorlevel% equ 0 (
    echo ✅ Operation completed successfully!
    echo Non-UULL files remain in SnagIt folder for manual handling.
) else (
    echo ❌ Operation failed with errors.
)

echo.
pause
