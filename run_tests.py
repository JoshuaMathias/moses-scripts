import os

model_path = "model_wiki_13540_gnome_13540_es_en"
lang_in = "es"
lang_out = "en"
test_paths = []
test_paths.append("data/gnome/GNOME.en-es_clean_test_100")
test_paths.append("data/wikipedia/Wikipedia.en-es_clean_test_10000")
test_paths.append("data/wikipedia/Wikipedia.en-es_clean_10000")
test_paths.append("data/dgt/DGT.en-es_clean_test_10000")
test_paths.append("data/eu/EUbookshop.en-es_clean_test_10000")
test_paths.append("data/ecb/ECB.en-es_clean_test_10000")
test_paths.append("data/kde/KDE4.en-es_clean_test_10000")
test_paths.append("data/gnome/GNOME.en-es_clean_test_10000")
for test_path in test_paths:
	os.system("python moses_test.py "+model_path+" "+test_path+" "+lang_in+" "+lang_out)