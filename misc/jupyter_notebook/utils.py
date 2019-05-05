import numpy as np

def print_words(words):
    for e in list(words):
        print(e, ': ', words[e])

def get_rand_img(H, W):
    return np.random.randn(H, W)