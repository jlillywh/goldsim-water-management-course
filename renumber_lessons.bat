@echo off
REM Lesson File Renumbering Script (Windows Batch Version) - Enhanced Safety
REM Usage: renumber_lessons.bat <insertion_point> [options]
REM 
REM Examples:
REM   renumber_lessons.bat 3             - Execute renumbering with backup
REM   renumber_lessons.bat 3 --dry-run   - Preview changes only (SAFE)
REM   renumber_lessons.bat 3 --backup-dir=my_backup - Custom backup directory
REM
REM SAFETY FEATURES:
REM - Always creates backup copies before making changes
REM - Supports dry-run mode to preview changes
REM - Automatic rollback on errors
REM - Comprehensive validation and logging

setlocal enabledelayedexpansion

REM Check if at least one argument provided
if "%1"=="" (
    echo ERROR: Missing insertion point argument
    echo.
    echo Usage: renumber_lessons.bat ^<insertion_point^> [options]
    echo.
    echo Examples:
    echo   renumber_lessons.bat 3             - Execute with backup
    echo   renumber_lessons.bat 3 --dry-run   - Preview changes only ^(RECOMMENDED FIRST^)
    echo   renumber_lessons.bat 3 --backup-dir=my_backup - Custom backup directory
    echo.
    echo SAFETY RECOMMENDATION: Always run with --dry-run first to preview changes!
    echo.
    exit /b 1
)

set insertion_point=%1
set additional_args=
shift

REM Collect additional arguments
:parse_args
if "%1"=="" goto args_done
set additional_args=!additional_args! %1
shift
goto parse_args
:args_done

echo ================================================================
echo LESSON FILE RENUMBERING TOOL - ENHANCED SAFETY VERSION
echo ================================================================
echo.
echo Insertion point: Lesson %insertion_point%
echo Additional arguments: %additional_args%
echo.

REM Check if Python is available
echo Checking Python availability...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not available or not in PATH
    echo.
    echo Please ensure Python is installed and accessible from command line.
    echo You can download Python from: https://www.python.org/downloads/
    echo.
    echo Alternative: Use PowerShell or manual renaming methods.
    echo.
    pause
    exit /b 1
)

echo Python is available. Proceeding with renumbering...
echo.

REM Check if this is a dry-run
echo %additional_args% | findstr /C:"--dry-run" >nul
if %errorlevel%==0 (
    echo *** DRY-RUN MODE DETECTED ***
    echo This will preview changes without modifying any files.
    echo.
) else (
    echo *** LIVE MODE - FILES WILL BE MODIFIED ***
    echo Backup copies will be created automatically.
    echo.
    echo SAFETY RECOMMENDATION: Run with --dry-run first to preview changes:
    echo   renumber_lessons.bat %insertion_point% --dry-run
    echo.
    set /p continue="Continue with file modifications? (y/N): "
    if /i not "!continue!"=="y" if /i not "!continue!"=="yes" (
        echo Operation cancelled by user.
        echo.
        echo To preview changes safely, run:
        echo   renumber_lessons.bat %insertion_point% --dry-run
        echo.
        pause
        exit /b 0
    )
)

REM Run the Python script with all arguments
echo Executing renumbering script...
echo.
python renumber_lessons.py %insertion_point% %additional_args%

REM Check the exit code
if %errorlevel%==0 (
    echo.
    echo ================================================================
    echo RENUMBERING COMPLETED SUCCESSFULLY
    echo ================================================================
    if not "%additional_args%"=="--dry-run" (
        echo.
        echo Backup files have been created for safety.
        echo If you need to undo changes, check the backup directory.
        echo.
    )
) else (
    echo.
    echo ================================================================
    echo RENUMBERING FAILED - SEE ERRORS ABOVE
    echo ================================================================
    echo.
    echo The script encountered errors. Files may have been restored
    echo automatically from backup if the operation was partially completed.
    echo.
    echo TROUBLESHOOTING:
    echo 1. Check the error messages above
    echo 2. Verify file permissions
    echo 3. Ensure no files are open in other applications
    echo 4. Run with --dry-run first to test
    echo.
)

echo.
pause
