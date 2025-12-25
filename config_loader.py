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
# config_loader MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import json
from task import Task


# --------------------------------------------------
# config loader
# --------------------------------------------------
class ConfigLoader:
    @staticmethod
    def load(file_path, task_mapping):
        with open(file_path, "r") as f:
            data = json.load(f)
        
        tasks = []
        for item in data:
            if not item.get("enabled", True):
                continue

            task_id = item["task_id"]
            interval = item["interval_seconds"]
            func_name = item["entry_point"]

            if func_name not in task_mapping:
                raise ValueError(
                    f"Unknown task function: {func_name}"
                )
            
            task = Task(
                task_id=task_id,
                name=item["task_name"],
                interval=interval,
                func=task_mapping[func_name],
            )
            tasks.append(task)
        
        return tasks
