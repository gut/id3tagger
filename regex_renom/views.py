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
	from common.files import getAllFilesRecursive
	from common.html import genFolderHtmlCode
	import re

	def checkDir(d):
		return path.isdir(d)
	
	def applyReplacement(regex, replacement, raw_dict):
		"""Returns a new dictionary with the 'files' key containing 
		the tuple (old, replaced)"""

		files = []
		any_changes = False
		for f in raw_dict['files']:
			if type(f) is dict:
				files.append(applyReplacement(regex, replacement, f))
			else:
				replaced = regex.sub(replacement, f)
				if replaced != f:
					any_changes = True
					files.append([f, replaced])
				else:
					files.append(f)
		return {'basename' : raw_dict['basename'], 'files' : files}, any_changes

	_get = request.GET
	dir_name = path.realpath(_get.get('directory', getcwd()))
	# p = 'extension'; exec('%s = _get.get("%s", "")' % (p,p))
	#  as that is not allowed...
	extension = _get.get("extension", "")
	search = _get.get("search", "")
	replacement = _get.get("replacement", "")

	title = '%s :: %s' % (APP_NAME, dir_name)
	d = {'title' : title}
	if checkDir(dir_name):
		raw_dict = getAllFilesRecursive(dir_name)
		parsed_files, any_changes = applyReplacement(re.compile(search), replacement, raw_dict)
		files = genFolderHtmlCode(parsed_files)
		d['can_change'] = any_changes
	else:
		d['error'] = True
		files = "Directory not found: %s" % dir_name
	d['content'] = files
	d.update(dict(_get.items()))
	return render_to_response('regex_renom/main.tpl', d)

