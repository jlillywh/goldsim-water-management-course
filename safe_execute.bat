@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM ================================================================
REM  SAFE_EXECUTE.BAT - Automated Safety Protocol Wrapper
REM ================================================================
REM  Purpose: Execute any project automation with automatic Git
REM           snapshots, logging, and validation protocols
REM  Usage:   safe_execute.bat <command> [arguments...]
REM  Example: safe_execute.bat python scripts/renumber_lessons.py 5
REM ================================================================

REM Initialize variables
SET "TIMESTAMP=%DATE:~-4,4%%DATE:~-10,2%%DATE:~-7,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%"
SET "TIMESTAMP=!TIMESTAMP: =0!"
SET "LOG_FILE=automation_log.txt"
SET "COMMAND_LINE=%*"

REM Validate that a command was provided
IF "%1"=="" (
    ECHO [ERROR] No command provided.
    ECHO Usage: safe_execute.bat ^<command^> [arguments...]
    ECHO Example: safe_execute.bat python scripts/renumber_lessons.py 5
    GOTO :EOF
)

ECHO.
ECHO ================================================================
ECHO   SAFE EXECUTION PROTOCOL INITIATED
ECHO ================================================================
ECHO Command: %COMMAND_LINE%
ECHO Time: %TIMESTAMP%
ECHO.

REM ================================================================
REM STEP 1: CREATE SAFETY SNAPSHOT (GIT COMMIT)
REM ================================================================
ECHO [STEP 1/3] Creating safety snapshot...

REM Check for uncommitted changes
git status --porcelain > temp_status.txt
FOR /F %%i IN (temp_status.txt) DO SET "STATUS_CHECK=%%i"
DEL temp_status.txt

IF DEFINED STATUS_CHECK (
    ECHO Found uncommitted changes - creating pre-execution commit...
    git add .
    git commit -m "Pre-execution snapshot [%TIMESTAMP%] - Before: %COMMAND_LINE%"
    IF ERRORLEVEL 1 (
        ECHO [FATAL] Failed to create safety snapshot. Aborting execution.
        GOTO :EOF
    )
    ECHO ✓ Safety snapshot created successfully.
) ELSE (
    ECHO ✓ Working directory is clean - no snapshot needed.
)
ECHO.

REM ================================================================
REM STEP 2: EXECUTE COMMAND WITH LOGGING
REM ================================================================
ECHO [STEP 2/3] Executing command...

REM Log the command execution start
ECHO ================================================================ >> "%LOG_FILE%"
ECHO EXECUTION LOG - %DATE% %TIME% >> "%LOG_FILE%"
ECHO Command: %COMMAND_LINE% >> "%LOG_FILE%"
ECHO ================================================================ >> "%LOG_FILE%"

REM Execute the command and capture output
%COMMAND_LINE% > temp_output.txt 2>&1
SET "COMMAND_EXIT_CODE=!ERRORLEVEL!"

REM Append the output to the log file
TYPE temp_output.txt >> "%LOG_FILE%"
ECHO. >> "%LOG_FILE%"
ECHO Exit Code: !COMMAND_EXIT_CODE! >> "%LOG_FILE%"
ECHO End Time: %DATE% %TIME% >> "%LOG_FILE%"
ECHO. >> "%LOG_FILE%"

REM Display the output to the user
TYPE temp_output.txt
DEL temp_output.txt

IF !COMMAND_EXIT_CODE! NEQ 0 (
    ECHO [ERROR] Command failed with exit code !COMMAND_EXIT_CODE!
    ECHO Check %LOG_FILE% for details.
    GOTO :EOF
)

ECHO ✓ Command executed successfully.
ECHO.

REM ================================================================
REM STEP 3: MANDATORY VALIDATION
REM ================================================================
ECHO [STEP 3/3] Running mandatory validation check...

REM Execute validation command
python scripts\generate_course_outline.py --update-readme
SET "VALIDATION_EXIT_CODE=!ERRORLEVEL!"

IF !VALIDATION_EXIT_CODE! NEQ 0 (
    ECHO [WARNING] Validation check failed with exit code !VALIDATION_EXIT_CODE!
    ECHO The primary command succeeded, but validation encountered issues.
) ELSE (
    ECHO ✓ Validation completed successfully.
)
ECHO.

REM ================================================================
REM EXECUTION SUMMARY
REM ================================================================
ECHO ================================================================
ECHO   SAFE EXECUTION COMPLETE
ECHO ================================================================
ECHO Primary Command: %COMMAND_LINE%
ECHO Exit Code: !COMMAND_EXIT_CODE!
ECHO Validation Code: !VALIDATION_EXIT_CODE!
ECHO Logged to: %LOG_FILE%
IF !COMMAND_EXIT_CODE! EQU 0 (
    IF !VALIDATION_EXIT_CODE! EQU 0 (
        ECHO Status: SUCCESS ✓
    ) ELSE (
        ECHO Status: PRIMARY SUCCESS, VALIDATION WARNING ⚠
    )
) ELSE (
    ECHO Status: FAILED ✗
)
ECHO ================================================================
ECHO.

ENDLOCAL
