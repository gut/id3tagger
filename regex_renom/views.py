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
__VERSION__ = 0.1

# Create your views here.
from django.shortcuts import render_to_response
from os import path, listdir
_ROOT_PATH = path.dirname(path.realpath(__file__))

def getFiles(request, rel = '', title = ''):
	def listFilesRecNested(_dir = '.'):
		"""Returns all mp3 under @_DIR arg recursivelly in the form:
		{'basename' : 'dir1', 'files' : 
			['file1', {'basename' : 'dir1.1' 
			...},...]
		,..}"""

		from os import path,listdir,chdir
		files = [_dir,]
		chdir(_dir)
		for file in listdir('.'):
			if path.isdir(file):
				files.append(listFilesRecNested(file))
			else:
				files.append(file)
		if _dir != '.':
			chdir('..')
		return files

	dir_name = path.join(_ROOT_PATH, rel)
	if not title:
		title = path.basename(dir_name)
	for f in gutfunctions.listFilesRecNested(dir_name)
	print files
	d = dict([(i, eval(i)) for i in ('files', 'title')])
	return render_to_response('regex_renom/main.tpl', d)

