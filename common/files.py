#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright (C) 2009 - Gustavo Serra Scalet <gsscalet@gmail.com>

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

__AUTHOR__ = "Gustavo Serra Scalet <gsscalet@gmail.com>"

from os import path,listdir

def listFilesRecNested(_dir = '.', hide_hidden = True):
	"""Returns all mp3 under @_DIR arg recursivelly in the form:
	{'basename' : 'dir1', 'files' : 
		['file1', {'basename' : 'dir1.1' 
		...},...]
	,..}"""

	files = []
	for f in listdir(_dir):
		if f.startswith('.') and not f.startswith('./') and hide_hidden:
			continue  # we don't want to see hidden files
		file_rel = path.join(_dir,f)
		if path.isdir(file_rel):
			files.append(listFilesRecNested(file_rel))
		else:  # regular file
			files.append(f)
	return {'basename' : path.basename(_dir), 'files' : files}
