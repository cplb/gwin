# Copyright (C) 2018 Duncan Macleod
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import tempfile

import pytest


def get_parametrized_value(request, param, default):
    """Return a parameter from a parametrized method, or ``default``

    This function is only designed to be used from within a fixture that
    uses the `request` object.
    """
    try:
        return request.getfixturevalue(param)
    except LookupError:
        return default


def tempfile_with_content(content, **kwargs):
    """Create a `tempfile.NamedTemporaryFile` with content
    """
    kwargs.setdefault('delete', True)
    tmpf = tempfile.NamedTemporaryFile(**kwargs)
    tmpf.write(content)
    tmpf.seek(0)
    return tmpf
