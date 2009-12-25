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
from django import template
from os import path, listdir, getcwd
from defs import *
_ROOT_PATH = path.dirname(path.realpath(__file__))

def genHtmlCode(arg):
	d = {'basename' : arg['basename']}
	files = []
	for f in sorted(arg['files']):
		if type(f) is dict:
			files.append([genHtmlCode(f), 'generate_new_table'])
		elif type(f) is list:
			files.append(f)
		else:
			# as the template expects a 2-position list ('now' and 'after'), let's do it
			files.append([f, ''])
	d['files'] = files
	template_folder = path.join(_ROOT_PATH, '..', 'template', 'regex_renom', 'folder.tpl')
	t = template.Template(open(template_folder).read())
	return t.render(template.Context(d))


def getFiles(request):
	def listFilesRecNested(_dir = '.'):
		"""Returns all mp3 under @_DIR arg recursivelly in the form:
		{'basename' : 'dir1', 'files' : 
			['file1', {'basename' : 'dir1.1' 
			...},...]
		,..}"""

		from os import path,listdir
		files = []
		for f in listdir(_dir):
			file_rel = path.join(_dir,f)
			if path.isdir(file_rel):
				files.append(listFilesRecNested(file_rel))
			else:  # regular file
				files.append(f)
		return {'basename' : path.basename(_dir), 'files' : files}
	
	_get = request.GET
	rel = _get.get('directory', '')
	workdir = getcwd()
	if rel.startswith('/'):
		dir_name = rel
	else:
		dir_name = path.join(workdir, rel) if rel else workdir
	title = '%s :: %s' % (APP_NAME, dir_name)
	files = genHtmlCode(listFilesRecNested(dir_name))
	d = {'content' : files, 'title' : title}
	d.update(dict(_get.items()))
	return render_to_response('regex_renom/main.tpl', d)

