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

	def do_bfs_list(sources, bfs_voisins=None):
		tmin = [INF] * MAX_NODES
		prev = [None] * MAX_NODES
		queue = copy(sources)
		for src in queue:
			tmin[src] = 0
		cur_pos_id = 0
		while cur_pos_id < len(queue):
			cur_pos = queue[cur_pos_id]
			cur_pos_id += 1
			cur_voisins = bfs_voisins[cur_pos] # <TODO: change if needed>
			for vois in cur_voisins:
				if tmin[vois] == INF:
					tmin[vois] = tmin[cur_pos]+1
					prev[vois] = cur_pos
					queue.append(vois)
		return tmin, prev
	
	def do_bfs(sources, bfs_voisins=None):
		tmin, prev = {}, {}
		if isinstance(bfs_voisins, dict):
			bfs_voisins = bfs_voisins.get
	
		queue = deque(copy(sources))
		for src in queue:
			tmin[src] = 0
			prev[src] = None
		while queue:
			cur_pos = queue.popleft()
			cur_voisins = bfs_voisins(cur_pos) # <TODO: change if needed>
			# cur_voisins = [(x+dx, y+dy) for dx, dy in moves if is_pos_valid(x+dx, y+dy, n)]
			for vois in cur_voisins:
				if vois not in tmin:
					dt = 1 # <Can be set to 0 and 1> # 1 if grid[vois[0]][vois[1]] == ? else 0
					tmin[vois] = tmin[cur_pos]+dt
					prev[vois] = cur_pos
					if dt: queue.append(vois)
					else: queue.appendleft(vois)
		return tmin, prev
	
	def get_bfs_path(prev, target):
		path = [target]
		while prev[path[-1]] is not None:
			path.append(prev[path[-1]])
		return path[::-1]

	def edges_to_voisins(edges, bidiretional):
		""" Transforms edge list to adjacency list """
		nodes = [e[0] for e in edges] + [e[1] for e in edges]
		voisins = {node : [] for node in nodes}
		for a, b in edges:
			voisins[a].append(b)
			if bidiretional:
				voisins[b].append(a)
		return voisins
	
	def is_graph_cyclic(voisins, sources=None):
		dfs_seen, dfs_current = set(), set()
		if sources is None:
			sources = list(voisins)
		def find_cycle(node):
			if node in dfs_seen:
				return (node in dfs_current)
			dfs_seen.add(node)
			dfs_current.add(node)
			has_cycle = any(map(find_cycle, voisins[node]))
			dfs_current.remove(node)
			return has_cycle
		return any(map(find_cycle, sources))
	

	# -------------------------------------------------------------------

	n, m, t = map(int, sys.stdin.readline().split())
	tricheurs = list(map(int, sys.stdin.readline().split()))

	routes = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
	routes = edges_to_voisins(routes, True)

	
	a1, _ = do_bfs(tricheurs, routes)
	a2, _ = do_bfs([1], routes)
	batims = []
	for i in range(1, n+1):
		if a1[i] > a2[i]:
			batims.append(i)
	print(*sorted(batims))




main()
