# python 

import configparser, os, sys

## user modules ##

def GetConfig(var_name):
	config = configparser.ConfigParser()
	# config_file_path = 'E:\\AROBS\\work\\QA_test\\Baseline\\AIO\\rewoek_test_suites_serial-to-ssh\\py_rework\\config\\config.ini'
	# config_file = 
	# config.read('../config/config.ini')
	if os.path.exists(config_file):
		config.read(config_file)
	# return_variable = None
	switch={
		"global_log_level": config['Default']['global_log_level']
	}
	return switch.get(var_name, 'Error during: tool.py -> GetConfig() -> switch')


def LogLevel():
	return GetConfig('global_log_level')


def printf(level, *mess):
	global_debug_level = LogLevel()
	# Internal functon
	def ToStr(var_list):
		return list(map(lambda elem: str(elem), var_list))

	def PrintC(LogLevel, message_list):
		print("{:8}".format(LogLevel), ' '.join(ToStr(message_list)))

	### ###
	if( ( "verbose" in global_debug_level ) and ( level in ["verbose", "debug", "info"] ) ):
		PrintC(level, mess)
	elif( ( "debug" in global_debug_level ) and ( level in ["debug", "info"] ) ):
		PrintC(level, mess)
	elif( level == "info" ):
		PrintC(level, mess)

def PrintInfo():

	printf('verbose', 'Current_work_dir:', GetTargetWorkDir())
	printf('verbose', 'Package: ', __package__)
	printf('debug', "main_file:", os.path.basename(sys.argv[0]) )
	printf('debug', "global_log_level =", GetConfig('global_log_level'))





### DEBUG ###
if __name__ == '__main__':
	from utils import *
	config_file = '../config/config.ini'
	os.chdir(GetTargetWorkDir())
	PrintInfo()
else:
	from .utils import GetTargetWorkDir
	config_file = './config/config.ini'
	os.chdir(GetTargetWorkDir())
	PrintInfo()