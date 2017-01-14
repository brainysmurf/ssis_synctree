from synctree.branch import Branch
from synctree.subbranch import SubBranch

class TestSubbranch(SubBranch):
	pass

class TestBranch(Branch):
    _subbranch_class = TestSubbranch

from ssis_synctree.templates.moodle_template import MoodleFullTemplate
class ConnectTemplate(Branch):
	_template = MoodleFullTemplate

import logging

class LogThis:

	def __init__(self):
		self.logger = []
		for logger_name, logger_level in [('stupid', 'warn'), ('over', 'info')]:
			logger = logging.getLogger(logger_name)
			logger.setLevel(getattr(logging, logger_level.upper()))
			self.logger.append( logger )

	def whu(self):
		pass

# from synctree.hijacker import augment_template

# class Test:

# 	def __init__(self, h, w):
# 		print(h)
# 		self.workdammit = 'w'

# 	def yo(self, arg):
# 		print(arg)
# 		return 'excepted!'

# 	def test(self, arg):
# 		print(self.workdammit)
# 		return 1

# 	def __call__(self, one, two):
# 		print(self.workdammit)

# class Test2(Test):
# 	def notthis(self):
# 		pass

# 	def this(self, action):
# 		print('this')
# 		self.here(action)
# 		return 1

# 	def here(self, action):
# 		print("here")

# class What:
# 	def __init__(self, method):
# 		self.method = method
# 		print(method)

# 	def __call__(self):
# 		print(self.method())


if __name__ == '__main__':

	pass
	# other = augment_template('notthis')(Test2)
	# print(other)
	# o = other('one', 'two')
	# result = o.this('action')
	# print(result)