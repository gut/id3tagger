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

from os import path,listdir,getcwd,chdir,rename
from glob import glob

def getAllFilesRecursive(_dir = '.', ext = '*', hide_hidden = True):
	"""Returns all matched @EXT files under @_DIR arg recursivelly in the form:
	{'basename' : 'dir1', 'files' : 
		['file1', {'basename' : 'dir1.1' 
		...},...]
	,..}"""

	files = []
	for f in glob(path.join(_dir, ext)):
		f = path.basename(f)
		if f.startswith('.') and not f.startswith('./') and hide_hidden:
			continue  # we don't want to see hidden files
		file_rel = path.join(_dir,f)
		if path.isdir(file_rel):
			files.append(getAllFilesRecursive(file_rel))
		else:  # regular file
			files.append(f)
	return {'basename' : path.basename(_dir), 'files' : files}

def makeRenamingChanges(parsed_files):
	"""Apply renaming to the files on @PARSED_FILES as described
	by updateDictWithReplacement"""
	def makeRenamingChangesAux(parsed_files):
		root = getcwd()
		chdir(path.join(root, parsed_files['basename']))
		for f in parsed_files['files']:
			if type(f) is dict:  # recursion!
				makeRenamingChangesAux(f)
			elif type(f) is tuple or type(f) is list:
				rename(*f)  # rename(f[0], f[1])
		chdir(root)

	# ignores the first basename as it's the same of the current dir
	parsed_files['basename'] = ''
	makeRenamingChangesAux(parsed_files)

