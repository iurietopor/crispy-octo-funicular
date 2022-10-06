# python

import sys, os

def GetTargetWorkDir():
	main_file_dir = sys.argv[0]
	return os.path.dirname(main_file_dir)