import sys
import os
import subprocess

def remove_end_slashes(path):
    index = len(path) - 1
    for letter in reversed(path):
        if letter != os.sep:
            break
        index -= 1
    if index > 0:
        return path[:index - 1]
    else:
        return ''
    return path

if len(sys.argv)<3:
	print("USAGE: MODEL_PATH TEST_PATH LANGUAGE_IN LANGUAGE_OUT")
	exit()
else:
	model_path = os.path.abspath(sys.argv[1])
	test_path = os.path.abspath(sys.argv[2])
	lang_in = sys.argv[3]
	lang_out = sys.argv[4]

if not os.path.exists(model_path):
	print("MODEL_PATH "+model_path+" not found.")
	exit()

if not os.path.exists(model_path+os.sep+"moses.ini"):
	print("No moses.ini file found at "+model_path)
	exit()

if not os.path.exists(test_path+"."+lang_in) or not os.path.exists(test_path+"."+lang_out):
	print("TEST_PATH "+test_path+" not found (specify name of .locale_code files without the extension, e.g. data/corpus for the files data/corpus.en and data/corpus.es)")
	exit()

moses_path = "mosesdecoder"
translated_path = test_path+"_translated."+lang_out
log_path = "moses_test_logs.txt"

# Translate
command = moses_path+"/bin/moses -v 0 "+" -f "+model_path+os.path.sep+"moses.ini < "+test_path+"."+lang_in+" > "+translated_path
print(command)
os.system(command)

# BLEU Score
log_file = open(log_path, 'a')
log_file.write("\n\n"+os.path.basename(model_path)+" testing "+test_path+":\n") 
command = moses_path+"/scripts/generic/multi-bleu.perl "+test_path+"."+lang_out+" < "+translated_path
print(command)
os.system(command)
output = subprocess.check_output(command, shell=True)
log_file.write(output)