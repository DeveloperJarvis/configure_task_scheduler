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
# scheduler MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import sched
import time
from executor import TaskExecutor


# --------------------------------------------------
# scheduler engine
# --------------------------------------------------
class SchedulerEngine:
    def __init__(self):
        self.scheduler = sched.scheduler(
            time.time, time.sleep
        )
    
    def schedule_task(self, task):
        def wrapper():
            TaskExecutor.execute(task)
            task.update_next_run()
            self.schedule_task(task)
        
        delay = max(0, task.next_run - time.time())
        self.scheduler.enter(delay, 1, wrapper)
    
    def start(self):
        self.scheduler.run()
