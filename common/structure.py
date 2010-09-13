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
from eyeD3 import Tag
from tags import DESIRED_TAGS
from os import path
from copy import copy

class TagElement:
	"""Access @filename and @tags for desired information"""
	tags = {}
	def __init__(self, _filename):
		self.filename = _filename
		self.basename = path.basename(_filename)
		tag = Tag()
		tag.link(self.filename)
		for t in DESIRED_TAGS:
			# e.g: self.tags['Artist'] = tag.getArtist()
			if t == 'Genre':
				self.tags[t] = tag.getGenre().getName() if tag.getGenre() else "Unknown Genre"
			elif t == 'TrackNum' or t == 'DiscNum':
				self.tags[t] = eval('tag.get%s()' % t)[0]  # Tuple: (TrackNum, TotalTracks)
			else:
				self.tags[t] = eval('tag.get%s()' % t)
		# by default the new tags are the same as the old ones
		self.new_tags = copy(self.tags.copy)

	def __repr__(self):
		return "   TagElement: %s\n    tags: %s" % (self.basename, self.tags)

class Directory:
	"""Group of TagElement from the same directory. Check @basename and
	run the iterator for data. The iterator returns first the directories and
	then the files of @basename"""
	directories = []
	files = []

	def __init__(self, _basename):
		self.basename = _basename

	def __repr__(self):
		return "Directory: %s\n directories inside: %s\n files inside: %s" % (self.basename, self.directories, self.files)

	def addFile(self, new_file):
		if isinstance(new_file, TagElement):
			self.files.append(new_file)
			return True
		else:
			return False

	def addDirectory(self, new_dir):
		if isinstance(new_dir, Directory):
			self.directories.append(new_dir)
			return True
		else:
			return False

	# iteration properties
	__last_index = 0
	def __iter__(self):
		return self
	def next(self):
		ret = None
		if self.__last_index < len(self.directories):  # get the directory
			ret = self.directories[self.__last_index]
		elif self.__last_index < len(self.directories) + len(self.files):  # get the file
			ret = self.files[self.__last_index - len(self.directories)]
		else:  # ready to reset
			self.__last_index = 0
			raise StopIteration

		self.__last_index += 1
		return ret

