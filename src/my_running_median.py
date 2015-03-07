#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Jingyi Chen
# Email: jc2834@cornell.edu

import sys, glob, os, shutil

def my_running_median(filepath, outputpath):
	lenPool, result = [], []
	with open(filepath, 'r') as f:
		for l in f.readlines():
			line = l.strip('\n').strip(',').strip('.')
			if line:
				newLen = len(line.split())
				lenPool.append(newLen)

	for i in range(1,len(lenPool)+1):
		result.append(compute_median(lenPool[:i]))

	with open(outputpath,'w+') as wf:
		for res in result:
			wf.write(str(res) + '\n')

def compute_median(A):
	if len(A) == 0:
		return 0.0
	if len(A)%2 != 0:
		return float(select(A, len(A)/2))
	else:
		return (select(A, len(A)/2) + select(A, len(A)/2-1))/2.0

def select(A,k):
	if len(A) <= 5:
		insertion_sort(A)
		return A[k]

	B = []
	for i in range(0,len(A),5):
		subA = A[i:i+5]
		subA = insertion_sort(subA)
		B.append(subA[len(subA)/2])
		if len(subA)%2 == 0:
			B.append(subA[len(subA)/2 - 1])

	medianB = select(B,len(B)/2)
	p1, p2, newA = re_arrange(A,medianB)

	if p1 <= k <= p1+p2-1:
		return medianB
	elif k > p1+p2-1:
		return select(newA[p1+p2:],k-p1-p2+1)
	elif k < p1:
		return select(newA[:p1],k-1)

def insertion_sort(items):
	for i in range(1, len(items)):
		j = i
		while j > 0 and items[j] < items[j-1]:
			items[j], items[j-1] = items[j-1], items[j]
			j -= 1
	return items

def re_arrange(A,medianB):
	left, mid, right = [], [], []
	for a in A:
		if a < medianB:
			left.append(a)
		elif a == medianB:
			mid.append(a)
		else:
			right.append(a)
	newA = left + mid + right
	return len(left), len(mid), newA

if __name__ == '__main__':
	inputpath = sys.argv[1]
	outputpath = sys.argv[2]

	with open('aSingleOne.txt', 'wb') as outfile:
		for filename in glob.glob(inputpath + '/*.txt'):
			with open(filename, 'rb') as readfile:
				shutil.copyfileobj(readfile, outfile)

	my_running_median('aSingleOne.txt',str(outputpath))
