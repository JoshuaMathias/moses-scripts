import click
import sys
import os
import random

num_test = 0
num_training = 0
if len(sys.argv)<3:
	print("USAGE: CORPUS_PATH LANGUAGE_IN LANGUAGE_OUT")
	exit()
else:
	corpus_path = sys.argv[1]
	# num_training = int(sys.argv[2])
	# num_test = int(sys.argv[3])
	lang_in = sys.argv[2]
	lang_out = sys.argv[3]

if not os.path.exists(corpus_path+"."+lang_in) or not os.path.exists(corpus_path+"."+lang_out):
	print("CORPUS_PATH "+corpus_path+" not found (specify name of .locale_code files without the extension, e.g. data/corpus for the files data/corpus.en and data/corpus.es)")
	exit()

if num_test == 0:
	create_test = False
moses_path = "mosesdecoder"
corpus_dir = os.path.dirname(corpus_path)
basename = os.path.basename(corpus_path)

# Tokenisation
token_path_in = corpus_path+".tok."+lang_in
token_path_out = corpus_path+".tok."+lang_out
command = moses_path+"/scripts/tokenizer/tokenizer.perl -l "+lang_in+" < "+corpus_path+"."+lang_in+" > "+token_path_in
print(command)
os.system(moses_path+"/scripts/tokenizer/tokenizer.perl -l "+lang_in+" < "+corpus_path+"."+lang_in+" > "+token_path_in)
command = moses_path+"/scripts/tokenizer/tokenizer.perl -l "+lang_out+" < "+corpus_path+"."+lang_out+" > "+token_path_out
print(command)
os.system(command)

# Truecase training
truecase_model_path = corpus_dir+"/truecase-model_"+basename
command = moses_path+"/scripts/recaser/train-truecaser.perl --model "+truecase_model_path+"."+lang_in+" --corpus "+token_path_in
print(command)
os.system(command)
command = moses_path+"/scripts/recaser/train-truecaser.perl --model "+truecase_model_path+"."+lang_out+" --corpus "+token_path_out
print(command)
os.system(command)

# Truecasing
true_path = corpus_path+".true"
command = moses_path+"/scripts/recaser/truecase.perl --model "+truecase_model_path+"."+lang_in+" < "+token_path_in+" > "+true_path+"."+lang_in
print(command)
os.system(command)
command = moses_path+"/scripts/recaser/truecase.perl --model "+truecase_model_path+"."+lang_out+" < "+token_path_out+" > "+true_path+"."+lang_out
print(command)
os.system(command)

# Clean the data
min_sentence_len = 1
max_sentence_len = 80
clean_path = corpus_path+"_clean"
os.system(moses_path+"/scripts/training/clean-corpus-n.perl "+true_path+" "+lang_in+" "+lang_out+" "+clean_path+" "+str(min_sentence_len)+" "+str(max_sentence_len))

# Escape special characters with html encoding
# os.system(moses_path+"/scripts/tokenizer/escape-special-chars.perl < "+clean_path+"."+lang_in+" > "+corpus_path+"_prepared"+"."+lang_in)
# os.system(moses_path+"/scripts/tokenizer/escape-special-chars.perl < "+clean_path+"."+lang_out+" > "+corpus_path+"_prepared"+"."+lang_out)

# corpus_train=corpus_path+"_"+str(num_training)
# corpus_test=corpus_path+"_test_"+str(num_test)

# if create_test:
# 	lines_in = open(corpus_path+"."+lang_in).readlines()
# 	lines_out = open(corpus_path+"."+lang_out).readlines()
# 	parallel_corpus = zip(lines_in, lines_out)
# 	random.shuffle(parallel_corpus)
# 	# print(parallel_corpus[0])
# 	lines_in[:], lines_out[:] = zip(*parallel_corpus)

# 	# Split corpus files

# 	lines_in_train = lines_in[:num_training]
# 	lines_out_train = lines_out[:num_training]
# 	lines_in_test = lines_in[len(lines_in)-num_test:]
# 	lines_out_test = lines_out[len(lines_out)-num_test:]

# 	train_in_file = open(corpus_train+"."+lang_in, 'w')
# 	train_in_file.writelines(lines_in_train)
# 	train_out_file = open(corpus_train+"."+lang_out, 'w')
# 	train_out_file.writelines(lines_out_train)
# 	test_in_file = open(corpus_test+"."+lang_in, 'w')
# 	test_in_file.writelines(lines_in_test)
# 	test_out_file = open(corpus_test+"."+lang_out, 'w')
# 	test_out_file.writelines(lines_out_test)

# else:
# os.system("cp "+corpus_path+"."+lang_in+" "+corpus_train+"."+lang_in)
# os.system("cp "+corpus_path+"."+lang_out+" "+corpus_train+"."+lang_out)

# If you don't need to randomize:
# os.system('head -n '+str(num_training)+" "+corpus_path+"."+lang_in+" > "+corpus_train+"."+lang_in)
# os.system('head -n '+str(num_training)+" "+corpus_path+"."+lang_out+" > "+corpus_train+"."+lang_out)
# os.system('tail -n '+str(num_test)+" "+corpus_path+"."+lang_in+" > "+corpus_test+"."+lang_in)
# os.system('tail -n '+str(num_test)+" "+corpus_path+"."+lang_out+" > "+corpus_test+"."+lang_out)
