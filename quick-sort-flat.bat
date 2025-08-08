@echo off
REM Ultra-Simple Image Sorting for GoldSim Course
REM Moves all UULL images to single global images folder

cd /d "c:\Users\JasonLillywhite\OneDrive - GoldSim\work\GoldSimOnlineCourse\goldsim-water-management-course"

echo.
echo ================================================
echo   Ultra-Simple Image Sort
echo ================================================
echo Target: Global images/ folder
echo Structure: Completely flat - no lesson folders
echo.

if "%1"=="--dry-run" (
    echo Running in DRY RUN mode...
    echo.
    python sort-images-flat.py --dry-run
) else if "%1"=="-d" (
    echo Running in DRY RUN mode...
    echo.
    python sort-images-flat.py --dry-run
) else (
    echo Moving UULL images to global images folder...
    echo.
    python sort-images-flat.py
)

echo.
if %errorlevel% equ 0 (
    echo ✅ Operation completed successfully!
    echo.
    echo Next steps:
    echo   - All images are now in images/ folder
    echo   - Use markdown: ![Title](images/filename.png)
    echo   - Lesson files can be renamed to: UU-LL-lesson-name.md
) else (
    echo ❌ Operation failed.
)

echo.
pause
