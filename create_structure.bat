@echo off

REM Root directory
@REM set ROOT=config_task_scheduler
set ROOT=.

REM Create directories if they do not exist
if not exist "%ROOT%" mkdir "%ROOT%"
if not exist "%ROOT%\config" mkdir "%ROOT%\config"
if not exist "%ROOT%\tests" mkdir "%ROOT%\tests"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"
call :create_py_file "%ROOT%\scheduler.py"
call :create_py_file "%ROOT%\task.py"
call :create_py_file "%ROOT%\executor.py"
call :create_py_file "%ROOT%\config_loader.py"
call :create_py_file "%ROOT%\registry.py"

call :create_py_file "%ROOT%\tests\test_config_loader.py"
call :create_py_file "%ROOT%\tests\test_registry.py"
call :create_py_file "%ROOT%\tests\test_scheduler.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\config\task_valid.json"
call :create_file "%ROOT%\config\task_invalid.json"

call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the configure_task_scheduler Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # configure_task_scheduler - Run tasks at intervals like cron
echo #                       Skills: sched module, background jobs, config files
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b