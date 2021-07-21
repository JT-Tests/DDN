# -*- coding: utf-8 -*-

# settings.py
#
# The library need some kind of configuration. There are different settings
# you might want to change depending on the application environment like
# toggling the debug mode, setting the secret key, and other such
# environment-specific things.
#
# Copyright (c) 2021 Janik Tarverdyan <Janik.Tarverdyan@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


"""
    core.settings
    ~~~~~~~~~~~~~

    Library default settings.

    :copyright: (c) 2021 by Janik.Tarverdyan@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""


from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Database path
DB_PATH = BASE_DIR.parent.parent / 'data/database'
