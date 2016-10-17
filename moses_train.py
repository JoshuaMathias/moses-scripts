import click
import sys
import os
import random

if len(sys.argv)<3:
	print("USAGE: CORPUS_PATH LANGUAGE_IN LANGUAGE_OUT")
	exit()
else:
	corpus_path = sys.argv[1]
	lang_in = sys.argv[2]
	lang_out = sys.argv[3]

if not os.path.exists(corpus_path+"."+lang_in) or not os.path.exists(corpus_path+"."+lang_out):
	print("CORPUS_PATH "+corpus_path+" not found (specify name of .locale_code files without the extension, e.g. data/corpus for the files data/corpus.en and data/corpus.es)")
	exit()

moses_path = "mosesdecoder"

# Train language model
num_grams = 3
lang_model_path = os.path.abspath(corpus_path+"."+lang_out+".arpa")
command = moses_path+"/bin/lmplz -o "+str(num_grams)+" < "+corpus_path+"."+lang_out+" > "+lang_model_path
print(command)
os.system(command)

# Make language model binary for faster loading at translation time
binary_lang_path = lang_model_path+".binary"
command = "/home/joshuamonkey/498/phrasal/src-cc/kenlm/bin/build_binary "+lang_model_path+" "+binary_lang_path
print(command)
os.system("/home/joshuamonkey/498/phrasal/src-cc/kenlm/bin/build_binary "+lang_model_path+" "+binary_lang_path)

# Train translation model
command = moses_path+"/scripts/training/train-model.perl -external-bin-dir mosesdecoder/bin/training-tools -mgiza -root-dir . " \
	+ "--corpus "+corpus_path+" --f "+lang_in+" --e "+lang_out+" -lm 0:"+str(num_grams)+":"+binary_lang_path+" -model-dir model_"+os.path.basename(corpus_path)+"_"+lang_in+"_"+lang_out
print(command)
os.system(command)
