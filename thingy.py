# -*- coding: utf-8 -*-
from multiprocessing import Pool
import hashlib
from itertools import product
from time import time

def millis():
	return int(time() * 1000)

def hash(strin):

	hashed = hashlib.md5(strin.encode()).hexdigest()
	#print("Hashing " + strin + ":" + hashed)
	return hashed

if __name__ == "__main__":

	alphabet = "abcdefghigklmnopqrstu"
	rep = 6

	words = []
	i = 0

	for word in product(alphabet, repeat=rep):
		words.append("".join(word))
		i += 1
		if i % 100000 == 0:

			p = Pool(6)

			timer = millis()

			p.map(hash, words)

			print(str(round((len(alphabet) ** rep) / (millis() - timer))) + " hashes/ms" + " at pos " + str(i))

			words = []