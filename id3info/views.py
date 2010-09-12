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
from os import path, getcwd
from defs import *

def analyse(request):
	from common.files import getAllFilesRecursive
	from common.tags import DESIRED_TAGS
	from common.html import genFolderCode

	def checkDir(d):
		return path.isdir(d)

	_get = request.GET
	dir_name = path.realpath(_get.get('directory', getcwd()))
	willMakeChanges = lambda : _get.get('change', "") == CHANGE_TRUE_VALUE

	title = makeTitle (dir_name)
	d = {'title' : title}
	if checkDir(dir_name):
		raw_dict = getAllFilesRecursive(dir_name, 'mp3')
		if raw_dict:
			print raw_dict
		folder_template = path.join(TEMPLATE_FOLDER, 'id3info', 'folder.tpl')
		files = genFolderCode(raw_dict, folder_template)
	else:
		d['error'] = True
		files = "Directory not found: %s" % dir_name
	d['content'] = files
	d.update(dict(_get.items()))  # reuse the defined variables on _get
	return render_to_response('id3info/main.tpl', d)

