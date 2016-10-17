import sys
import os
import subprocess

test_paths = []
if len(sys.argv)<3:
	print("USAGE: MODEL_PATH LANGUAGE_IN LANGUAGE_OUT TEST_PATHS")
	exit()
else:
	model_path = os.path.abspath(sys.argv[1])
	lang_in = sys.argv[2]
	lang_out = sys.argv[3]
	for i in range(4,len(sys.argv)):
		test_paths.append(os.path.abspath(sys.argv[i]))

for test_path in test_paths:
	os.system("moses_test.py "+model_path+" "+test_path+" "+lang_in+" "+lang_out)