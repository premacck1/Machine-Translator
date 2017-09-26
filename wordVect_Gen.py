import numpy;
import random;
import math;
import gensim;

sentences = gensim.models.word2vec.LineSentence('eng_small_2.txt')
model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=1, workers=4)
model.save("en_wv_2")

sentences = gensim.models.word2vec.LineSentence('sa_2.txt')
model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=1, workers=4)
model.save("sp_wv_2")
