import sys
import os
import random
import math

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
	print("USAGE: CORPUS_PATH NUM_TEST_LINES LANGUAGE_IN LANGUAGE_OUT")
	exit()
else:
    corpus_path = os.path.abspath(sys.argv[1])
    num_test = sys.argv[2]
    lang_in = sys.argv[3]
    lang_out = sys.argv[4]

if not os.path.exists(corpus_path+"."+lang_in) or not os.path.exists(corpus_path+"."+lang_out):
	print("CORPUS_PATH "+corpus_path+" not found (specify name of .locale_code files without the extension, e.g. data/corpus for the files data/corpus.en and data/corpus.es)")
	exit()

moses_path = "mosesdecoder"
lines_in = open(corpus_path+"."+lang_in).readlines()
lines_out = open(corpus_path+"."+lang_out).readlines()
if '%' in num_test:
    num_test = int(math.floor(float(len(lines_in)) * float("."+num_test.replace("%",""))))
print("Number of test lines: "+str(num_test))
num_training = len(lines_in) - num_test
parallel_corpus = zip(lines_in, lines_out)
random.shuffle(parallel_corpus)
lines_in[:], lines_out[:] = zip(*parallel_corpus)


# Split corpus files
corpus_train=corpus_path+"_"+str(num_training)
corpus_test=corpus_path+"_"+str(num_test)

lines_in_train = lines_in[:num_training]
lines_out_train = lines_out[:num_training]
lines_in_test = lines_in[len(lines_in)-num_test:]
lines_out_test = lines_out[len(lines_out)-num_test:]

train_in_file = open(corpus_train+"."+lang_in, 'w')
train_in_file.writelines(lines_in_train)
train_out_file = open(corpus_train+"."+lang_out, 'w')
train_out_file.writelines(lines_out_train)
test_in_file = open(corpus_test+"."+lang_in, 'w')
test_in_file.writelines(lines_in_test)
test_out_file = open(corpus_test+"."+lang_out, 'w')
test_out_file.writelines(lines_out_test)

print("Created randomly split files: "+str(train_in_file.name)+" "+str(test_in_file.name)+" "+str(train_out_file.name)+" "+str(test_out_file.name))