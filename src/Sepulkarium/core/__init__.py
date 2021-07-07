# -*- coding: utf-8 -*-

# __init__.py
#
# This is all methods for the Sepulkarium.
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
    lib.__init__
    ~~~~~~~~~~~~

    Sepulkarium is the main library it's include all methods and configurations

    :copyright: (c) 2021 by Janik Tarverdyan <Janik.Tarverdyan@gmail.com>.
    :license: GPLv3, see LICENSE for more details.
"""


class Sepulkarium(object):

    """Docstring for Sepulkarium. """

    __classname__ = 'Sepulkarium'

    def __init__(self, function):
        """TODO: to be defined. """
        self.function = function

    def __call__(self, *args, **kwargs):

        # We can add some code
        # before function call
        self.function(*args, **kwargs)

        # We can also add some code
        # after function call.

    def __get__(self):
        """Docstring for get method"""
        pass

    @classmethod
    def settings(self, arg=False, *args, **kwargs):
        if kwargs is None:
            # checked and saved data directory
            pass
        else:
            # TODO: write document for this case.
            pass
