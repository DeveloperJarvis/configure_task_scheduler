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
# test_config_loader MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import os
import unittest
from config_loader import ConfigLoader


def dummy():
    pass


# --------------------------------------------------
# test config loader
# --------------------------------------------------
class TestConfigLoader(unittest.TestCase):

    def test_valid_config(self):
        tasks = ConfigLoader.load(
            os.path.join("config","task_valid.json"),
            {"hello": dummy, "cleanup": dummy}
        )
        self.assertEqual(len(tasks), 2)
    
    def test_invalid_config(self):
        with self.assertRaises(ValueError):
            ConfigLoader.load(
                os.path.join("config","task_invalid.json"),
                {"hello": dummy}
            )

if __name__ == "__main__":
    unittest.main()
