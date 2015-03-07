#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, glob, os, string
wordCount = {}

def my_word_count(filepath,outputpath):
	global wordCount
	with open(filepath, 'r') as f:
		for l in f.readlines():
			line = l.strip('\n')
			if line:
				words = map(lambda x:x.lower().translate(string.maketrans("",""), string.punctuation),line.split())
				pass
				for word in words:
					if word not in wordCount:
						wordCount[word] = 1
					else:
						wordCount[word] += 1

	with open(outputpath,'w+') as wf:
		for k,v in sorted(wordCount.items()):
			wf.write(k.ljust(8) + str(v).rjust(8)+ '\n')

if __name__ == '__main__':
	inputpath = sys.argv[1]
	outputpath = sys.argv[2]
	for infile in sorted(glob.glob(inputpath + '/*.txt')):
		my_word_count(infile,str(outputpath))
