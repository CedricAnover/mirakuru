# Copyright (C) 2014 by Clearcode <http://clearcode.cc>
# and associates (see AUTHORS).

# This file is part of mirakuru.

# mirakuru is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# mirakuru is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with mirakuru.  If not, see <http://www.gnu.org/licenses/>.
"""Executors"""

from mirakuru.executors.simple import SimpleExecutor
from mirakuru.executors.output import OutputCoordinatedExecutor
from mirakuru.executors.tcp import TCPCoordinatedExecutor
from mirakuru.executors.http import HTTPCoordinatedExecutor

__all__ = (
    SimpleExecutor, OutputCoordinatedExecutor,
    TCPCoordinatedExecutor, HTTPCoordinatedExecutor
)