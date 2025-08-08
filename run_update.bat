@echo off
SETLOCAL

REM --- Script to automatically renumber lessons and update the README ---

ECHO.
ECHO ================================================
ECHO ==   GoldSim Course: Automated Update Utility   ==
ECHO ================================================
ECHO.

REM Check if an argument was provided
IF "%1"=="" (
    ECHO [INFO] No insertion point provided - updating documentation only.
    ECHO.
    ECHO For lesson insertion/renumbering, use: run_update.bat [lesson_number]
    ECHO e.g., run_update.bat 3  (to insert after lesson 3)
    ECHO e.g., run_update.bat 5  (to insert after lesson 5)
    ECHO.
    GOTO UPDATE_README
)

SET INSERTION_POINT=%1

ECHO [Step 1 of 2] Renumbering lessons starting after %INSERTION_POINT%...
python renumber_lessons.py %INSERTION_POINT% --force
IF ERRORLEVEL 1 (
    ECHO [FATAL] Renumbering script failed. Aborting.
    GOTO :EOF
)
ECHO Renumbering complete.
ECHO.

:UPDATE_README
IF "%1"=="" (
    ECHO [Documentation Update] Updating README.md with current course outline...
) ELSE (
    ECHO [Step 2 of 2] Updating README.md with the new course outline...
)
python generate_course_outline.py --update-readme
IF ERRORLEVEL 1 (
    ECHO [FATAL] README update script failed.
    GOTO :EOF
)
ECHO README.md updated successfully.
ECHO.

ECHO ================================================
IF "%1"=="" (
    ECHO ==   Documentation Update Complete.
) ELSE (
    ECHO ==   Update Complete.
)
ECHO ================================================
ECHO.

ENDLOCAL
