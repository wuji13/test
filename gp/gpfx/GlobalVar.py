# -*- coding: utf-8 -*-

class GlobalVar(object):
	cursor = None

	def set(self,c):
		GlobalVar.cursor = c

#	def set_cursor(c): 
#	  GlobalVar.cursor = c

	def get(self): 
	  return GlobalVar.cursor


