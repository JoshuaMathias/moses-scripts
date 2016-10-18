# moses-scripts
Convenience scripts for uses of the Moses machine translation command line utility.

These Python scripts I created and used for my own research and experimentation with Moses, in order to carry out many tests. In the future I may add a script to do cross-validation.
The following scripts require command line arguments:
*moses_prepare.py
USAGE: CORPUS_PATH LANGUAGE_IN LANGUAGE_OUT

*moses_train.py*
USAGE: CORPUS_PATH LANGUAGE_IN LANGUAGE_OUT

*moses_test.py*
USAGE: MODEL_PATH TEST_PATH LANGUAGE_IN LANGUAGE_OUT

*moses_tests.py*
USAGE: MODEL_PATH LANGUAGE_IN LANGUAGE_OUT TEST_PATHS

The following script does not require command line arguments:
*run_tests.py*
This script is an example of running a set of tests in succession, to be edited according to individual needs.
