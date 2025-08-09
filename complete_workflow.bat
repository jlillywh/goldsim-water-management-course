@echo off
REM Complete Lesson Management Workflow
REM This batch file provides a complete workflow for adding new lessons

echo.
echo ==========================================================
echo GoldSim Course - Complete Lesson Management Workflow
echo ==========================================================
echo.
echo This script helps you manage the complete workflow when
echo adding new lessons to the course structure.
echo.
echo Current workflow steps:
echo 1. Create your new lesson file manually (UU-LL-lesson-title.md)
echo 2. Run renumbering script to fix subsequent lesson numbers  
echo 3. Update README.md with the current course structure
echo.

set /p continue="Ready to proceed with lesson management? (y/N): "

if /i not "%continue%"=="y" (
    echo Workflow cancelled.
    goto :end
)

echo.
echo Step 1: Checking current course structure...
echo --------------------------------------------------
python scripts\generate_course_outline.py
echo.

:renumber_choice
echo Step 2: Lesson Renumbering
echo --------------------------------------------------
echo.
set /p need_renumber="Do you need to renumber lessons? (y/N): "

if /i "%need_renumber%"=="y" (
    echo.
    set /p insertion_point="Enter the lesson number where you inserted the new lesson (e.g., 5): "
    
    echo.
    echo Preview of renumbering changes:
    echo --------------------------------
    python scripts\renumber_lessons.py !insertion_point! --dry-run
    echo.
    
    set /p confirm_renumber="Proceed with renumbering? (y/N): "
    
    if /i "!confirm_renumber!"=="y" (
        echo.
        echo Executing renumbering...
        python scripts\renumber_lessons.py !insertion_point!
        
        if errorlevel 1 (
            echo ERROR: Renumbering failed. Check the output above.
            goto :end
        )
        
        echo ✓ Renumbering completed successfully.
    ) else (
        echo Renumbering skipped.
    )
) else (
    echo Renumbering skipped.
)

echo.
echo Step 3: Documentation Update
echo --------------------------------------------------
echo Updating README.md with current course structure...
echo.

python scripts\generate_course_outline.py --update-readme

if errorlevel 1 (
    echo ERROR: README update failed. Check the output above.
    goto :end
)

echo.
echo ==========================================================
echo Workflow completed successfully!
echo ==========================================================
echo.
echo Summary of actions taken:
if /i "%need_renumber%"=="y" if /i "%confirm_renumber%"=="y" echo ✓ Lesson files renumbered from position %insertion_point%
echo ✓ README.md updated with current course structure
echo ✓ All lesson hyperlinks updated automatically
echo.
echo Your course documentation is now synchronized with the file structure.
echo.

:end
pause
