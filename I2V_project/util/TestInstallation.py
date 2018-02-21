#!/usr/bin/env python
'''
'''
import unittest
import logging
from logging import config

class ModuleImportTestCase(unittest.TestCase):
	def test_gensim(self):
		result = False
		logger.info("try to test gensim installation...")
		try:
			import gensim
			logger.info("succeed in importing gensim")
		except:
			logger.error("Failed to import gensim")
			raise

if __name__=='__main__':
	unittest.main()
