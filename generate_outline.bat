@echo off
REM Course Outline Generator - Enhanced Launcher
REM This batch file runs the Python script to generate the current course outline
REM and optionally update the README.md file

echo.
echo GoldSim Water Management Course Outline Generator
echo ==================================================
echo.
echo 1. Print outline to console only
echo 2. Update README.md with current outline
echo 3. Update README.md and save outline to file
echo 4. Just save outline to course_outline.txt
echo.

set /p choice="Choose option (1-4): "

if "%choice%"=="1" (
    echo.
    echo Generating course outline...
    echo.
    python generate_course_outline.py
) else if "%choice%"=="2" (
    echo.
    echo Updating README.md with current course outline...
    echo.
    python generate_course_outline.py --update-readme
) else if "%choice%"=="3" (
    echo.
    echo Updating README.md and saving outline to file...
    echo.
    python generate_course_outline.py --update-readme --save-outline
) else if "%choice%"=="4" (
    echo.
    echo Saving outline to course_outline.txt...
    echo.
    python generate_course_outline.py --save-outline
) else (
    echo Invalid choice. Running default (print to console)...
    echo.
    python generate_course_outline.py
)

echo.
echo ====================================================
echo Course outline operation complete.
echo.
pause
