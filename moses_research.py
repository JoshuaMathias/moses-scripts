import sys
import os
import random

paths = []
paths.append("data/gnome/GNOME.en-es")
paths.append("data/wikipedia/Wikipedia.en-es")
paths.append("data/wikipedia/Wikipedia.en-es")
paths.append("data/dgt/DGT.en-es")
paths.append("data/eu/EUbookshop.en-es")
paths.append("data/ecb/ECB.en-es")
paths.append("data/kde/KDE4.en-es")
paths.append("data/gnome/GNOME.en-es")
lang_in = "es"
lang_out = "en"

for path in paths:
	run_research(path, lang_in, lang_out)

# def do_all(path, lang_in, lang_out):
# 	os.system("python moses_create_tests.py"+path+" "+num_test+" "+lang_in+" "+lang_out)
# 	train_path = path+"_"+num_training
# 	test_path = path+"_"+num_test
# 	os.system("python moses_train.py "+train_path+" "+lang_in+" "+lang_out)
# 	model_path = "model_"+os.path.basename(corpus_path)
# 	os.system("python moses_test.py "+model_path+" "+test_path+" "+lang_in+" "+lang_out)

def run_research(path, lang_in, lang_out):
	print("Performing research for "+str(path)+" "+lang_in+" "+lang_out)
	num_test=10000
	num_lines = len(open(path+"."+lang_in).readlines())
	os.system("python moses_prepare.py "+path+" "+lang_in+" "+lang_out)
	path = path+"_clean"
	if num_lines<90000:
		num_test = 1000
	num_training = num_lines - num_test
	train_path = path+"_"+num_training
	test_path = path+"_"+num_test

	bleu_scores = []
	num_crosses = 10
	for i in range(num_crosses):
		cross_path = path+"_cross"+str(i+1)
		os.system("python moses_train.py "+train_path+" "+lang_in+" "+lang_out)
		model_path = "model_"+os.path.basename(corpus_path)
		os.system("python moses_test.py "+model_path+" "+test_path+" "+lang_in+" "+lang_out)