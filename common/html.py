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

from django import template
from defs import *
from os import path
_ROOT_PATH = path.dirname(path.realpath(__file__))

def genFolderCode(directories, t, disk_changed = False):
	"compiles the dict found on @directories to the html on template @T"
	files = []
	for d in directories.directories:
		files.append({'folder' : genFolderCode(d, t, disk_changed), 'generate_new_table' : True})
	for f in directories.files:
		#FIXME for f in sorted(directories['files']):
		for f in directories.files:
			#FIXME if f.new_tags != f.tags:
			files.append(f)

	t = template.Template(open(t).read())
	folder_dict = {'basename' : directories.basename, 'disk_changed' : disk_changed, 'files' : files}
	return t.render(template.Context(folder_dict))

