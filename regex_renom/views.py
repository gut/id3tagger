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
from os import path, listdir, getcwd
from defs import *
_ROOT_PATH = path.dirname(path.realpath(__file__))


def getFiles(request):
	from common.files import listFilesRecNested
	from common.html import genFolderHtmlCode

	def check_dir(d):
		return path.isdir(d)
	
	_get = request.GET
	dir_name = path.realpath(_get.get('directory', getcwd()))
	title = '%s :: %s' % (APP_NAME, dir_name)
	d = {'title' : title}
	if check_dir(dir_name):
		files = genFolderHtmlCode(listFilesRecNested(dir_name))
	else:
		d['error'] = True
		files = "Directory not found: %s" % dir_name
	d['content'] = files
	d.update(dict(_get.items()))
	return render_to_response('regex_renom/main.tpl', d)

