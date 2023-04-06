import sys
from collections import deque, namedtuple, defaultdict
from math import *
# from fractions import *
# import numpy as np
sys.setrecursionlimit(10**9)

# Comment this to reduce memory usage
from copy import copy, deepcopy
from functools import reduce, lru_cache
from itertools import *
from random import * # randint, shuffle, ...
import heapq
cache = lru_cache(maxsize=None)

def main():
	INF, LLINF = 10**9, 4*(10**18)
	MOD, MOD_EDU = 10**9+7, 998244353
	ID_FCT = lambda x:x
	# print = sys.stdout.write
	# input = sys.stdin.readline
	input = lambda : sys.stdin.readline().rstrip()

	def modul(n, mod=MOD): return (n%mod + mod)%mod
	def err_print(*args, end="\n", sep=" "): sys.stderr.write(" ".join(chain([str(a) for a in args], [end])))
	def list_map(string, fct=int): return list(map(fct, string.split()))
	def read_matrix(n, f=ID_FCT): return [list(map(f, sys.stdin.readline().strip().split())) for _ in range(n)]
	def read_char_matrix(n): return [sys.stdin.readline().strip() for _ in range(n)]


	# -------------------------------------------------------------------



	# -------------------------------------------------------------------

	n = int(sys.stdin.readline())
	themes = [sys.stdin.readline().rstrip().split() for _ in range(n)]

	states = {(None, None): 1}
	for i in range(n):
		themes2 = {}
		for (er, prev), nb in states.items():
			for t in themes[i]:
				if t != prev and (i < n-1 or t != er):
					er2 = t if er is None else er
					stt = (er2, t)
					themes2[stt] = themes2.get(stt, 0) + nb
		states = themes2
	print(sum(states.values()))



main()
