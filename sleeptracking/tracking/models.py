from django.db import models

class Sleep(object):
	def __init__(self, id='', rate='', duration='', deep_pct='', light_pct='', date=''):
		self.id = id
		self.rate = rate
		self.duration = duration
		self.deep_pct = deep_pct
		self.light_pct = light_pct
		self.date = date