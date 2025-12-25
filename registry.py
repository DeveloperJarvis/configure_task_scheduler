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
# registry MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------

# --------------------------------------------------
# task registry
# --------------------------------------------------
class TaskRegistry:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task):
        if task.task_id in self.tasks:
            raise ValueError("Duplicate task ID")
        self.tasks[task.task_id] = task
    
    def get_enabled_tasks(self):
        return [t for t in self.tasks.values() if t.enabled]
