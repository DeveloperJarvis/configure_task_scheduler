# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the configure_task_scheduler Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# configure_task_scheduler - Run tasks at intervals like cron
#                       Skills: sched module, background jobs, config files
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# configure_task_scheduler MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import os
import logging
from scheduler import SchedulerEngine
from registry import TaskRegistry
from config_loader import ConfigLoader


def hello():
    print("Hello task executed")


def cleanup():
    print("Cleanup task executed")


TASK_MAPPING = {
    "hello": hello,
    "cleanup": cleanup,
}


def main():
    logging.basicConfig(level=logging.INFO)

    registry = TaskRegistry()
    scheduler = SchedulerEngine()

    tasks = ConfigLoader.load(
        os.path.join("config","task_valid.json"),
        TASK_MAPPING
    )

    for task in tasks:
        registry.add_task(task)
        scheduler.schedule_task(task)
    
    scheduler.start()


if __name__ == "__main__":
    main()
