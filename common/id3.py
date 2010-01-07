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
from eyeD3 import Tag
from glob import glob

DESIRED_TAGS = ('Album', 'Artist', 'DiscNum', 'Genre', 'Title', 'TrackNum', 'Year')

def getTag(parsed_files):
	"""Get tags of each @PARSED_FILES. Return a
	getAllFilesRecursive-like dictionary with our DESIRED_TAGS:
	{'basename' : 'dir1', 'files' : 
		[
			{'filename' : 'file1.mp3',
			'Artist' : 'Artist1',...}
		, {'basename' : 'dir1.1' 
		...},...]
	,..}"""
	def getTagFromThisFile(f):
		d = {'filename' : f,}
		tag = Tag()
		tag.link(f)
		for t in DESIRED_TAGS:
			# e.g: d['Artist'] = tag.getArtist()
			if t == 'Genre':
				d[t] = tag.getGenre().getName()
			elif t == 'TrackNum' or t == 'DiscNum':
				d[t] = eval('tag.get%s()' % t)[0]  # Tuple: (TrackNum, TotalTracks)
			else:
				d[t] = eval('tag.get%s()' % t)
		return d

	def getTagAux(parsed_files):
		newFilesList = []
		root = getcwd()
		chdir(path.join(root, parsed_files['basename']))
		for f in parsed_files['files']:
			if type(f) is dict:  # recursion!
				getTagAux(f)
				newFilesList.append(f)  # this folder will remain there, but now updated
			elif type(f) is str:
				newFilesList.append(getTagFromThisFile(f))
		chdir(root)
		parsed_files['files'] = newFilesList

	# ignores the first basename as it's the same of the current dir
	old = parsed_files['basename']
	parsed_files['basename'] = ''
	getTagAux(parsed_files)
	parsed_files['basename'] = old

