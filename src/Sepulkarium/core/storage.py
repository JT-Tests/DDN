#!/usr/bin/env python
# -*- coding: utf-8 -*-

# storage.py
#
# This is a storage for the sepulcas.
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
    lib.storage
    ~~~~~~~~~~~

    The storage for saving and removing sepulcas. Storage works automatically
    when add, edit or remove any sepulca.

    @methods __get__, __remove__, __edit__

    :copyright: (c) 2021 by Janik Tarverdyan <Janik.Tarverdyan@gmail.com>.
    :license: GPLv3, see LICENSE for more details.
"""


# Storage works with local, it means not working and configured with popular
# databases by default, but it's possible for using all popular databases
# programmes like SQL Family and No SQL like MongoDB if necessary.
#
# See about classes: https://cutt.ly/EmmZima
class Storage(object):
    """
    Storage none includes DB programmes by default. It's save data into the
    local. Local DB format by default is "JSON" (JavaScript Object Notation).
    """

    def __init__(self, *args, **kwargs):
        """
        pass
        """
        super().__init__(*args, **kwargs)

    def __get__(self, *args, **kwargs):
        """
        Get all sepulcas from the storage
        """
        pass

    def __remove__(self):
        """
        Documentation remove method
        """
        pass

    def __edit__(self):
        """
        Documentation edit method
        """
        pass

    # Flag names are globally defined!  So in general, we need to be careful to
    # pick names that are unlikely to be used by other libraries. If there is a
    # conflict, we'll get an error at import time.
    def __FLAGS__(self, mode='disabled', *args, **kwargs):
        """
        Flags:  A flag is one or more data bits used to store binary values as
                specific program structure indicators. A flag is a component of
                a programming language's data structure.

                A computer interprets a flag value in relative terms or based
                on the data structure presented during processing, and uses the
                flag to mark a specific data structure. Thus, the flag value
                directly impacts the processing outcome.

                A flag reveals whether a data structure is in a possible state
                range and may indicate a bit field attribute, which is often
                permission-related. A microprocessor has multiple state
                registers that store multiple flag values that serve as
                possible post-processing condition indicators such as
                arithmetic overflow.

                The command line switch is a common flag format in which a
                parser option is set at the beginning of a command line
                program. Then, switches are translated into flags during
                program processing.


        Flag Types: This is a list of the DEFINE_*’s that you can do. All flags
                    take a name, default value, help-string, and optional
                    ‘short’ name (one-letter name). Some flags have other
                    arguments, which are described with the flag.

            List:
                * DEFINE_string: takes any input and interprets it as a string.

                * DEFINE_bool or DEFINE_boolean: typically does not take an
                argument: pass --myflag to set FLAGS.myflag to True, or
                --nomyflag to set FLAGS.myflag to False. --myflag=true and
                --myflag=false are also supported, but not recommended.

                * DEFINE_float: takes an input and interprets it as a floating
                point number. This also takes optional arguments lower_bound
                and upper_bound; if the number specified on the command line
                is out of range, it raises a FlagError.

                * DEFINE_integer: takes an input and interprets it as an
                integer. This also takes optional arguments lower_bound and
                upper_bound as for floats.

                * DEFINE_enum: takes a list of strings that represents legal
                values. If the command-line value is not in this list, it
                raises a flag error; otherwise, it assigns to FLAGS.flag as
                a string.

                * DEFINE_list: Takes a comma-separated list of strings on the
                command line and stores them in a Python list object.

                * DEFINE_spaceseplist: Takes a space-separated list of strings
                on the commandline and stores them in a Python list object.
                For example: --myspacesepflag "foo bar baz"

                * DEFINE_multi_string: The same as DEFINE_string, except the
                flag can be specified more than once on the command line.
                The result is a Python list object (list of strings), even if
                the flag is only on the command line once.

                * DEFINE_multi_integer: The same as DEFINE_integer, except the
                flag can be specified more than once on the command line. The
                result is a Python list object (list of ints), even if the flag
                is only on the command line once.

                * DEFINE_multi_enum: The same as DEFINE_enum, except the flag
                can be specified more than once on the command line. The result
                is a Python list object (list of strings), even if the flag is
                only on the command line once.



       Example for usage:

            flags.DEFINE_string('name', 'Jane Random', 'Your name.')

            flags.DEFINE_integer('age', None,
                                 'Your age in years.', lower_bound=0)

            flags.DEFINE_boolean('debug', False, 'Produces debugging output.')

            flags.DEFINE_enum('job', 'running',
                              ['running', 'stopped'], 'Job status.')
        """
        Flags = {}
