# python
import os, sys
import xml.etree.ElementTree as ET
from modules.traces.tool import printf




#################
# MAIN
#################
def MAIN():
	# global_debug_level for printed messeges in Console


	print()
	path_to_file = "E:\\AROBS\\work\\QA_test\\Baseline\\AIO\\rewoek_test_suites_serial-to-ssh\\py_rework\\test_file.xml"
	file_tree = ET.parse(path_to_file)
	# print(file_tree.getroot())
	file_root = file_tree.getroot()
	printf('info', "MainXMLTag = ", file_root.tag)

	for test_cases in file_root:
		printf('verbose', 'Proceded tag: ', test_cases.tag)
		for test_steps in test_cases:
			printf('info', test_steps[0].tag)
			# for t_step in test_steps:
			# 	print(t_step.[])


if __name__ == '__main__':
	MAIN()

