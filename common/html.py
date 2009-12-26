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

def genFolderHtmlCode(arg):
	"compiles the dict found on @ARG to the html on template"
	d = {'basename' : arg['basename']}
	files = []
	for f in sorted(arg['files']):
		if type(f) is dict:
			files.append({'folder' : genFolderHtmlCode(f), 'generate_new_table' : True})
		elif type(f) is list or type(f) is tuple:
			# I guess it's correctly parsed...
			e = {'list' : f}
			if f[0] != f[1]:
				e['changed'] = True
			files.append(e)
		else:
			files.append(f)
	d['files'] = files
	template_folder = path.join(_ROOT_PATH, '..', 'template', 'regex_renom', 'folder.tpl')
	t = template.Template(open(template_folder).read())
	return t.render(template.Context(d))

