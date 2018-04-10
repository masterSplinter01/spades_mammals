from __future__ import division
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
from collections import Counter

pair_edge = open("score_pair_stats_meta").readlines()

# t-values
step = 0.02
t = np.arange(0.0, 1.0, step)
#splitting readlines from file to list of list: edge_id edge_id t0 -> [[edge_id, edge_id, t0], ... ]
split_edges = [x.split() for x in pair_edge]

#create list of unique edges
edge_list1 = [e[0] for e in split_edges]
edge_list2 = [e[1] for e in split_edges]
edge_list = list(set(edge_list1+edge_list2))

#extract pairs of edges from pair_edge without t0
pairs = [[e[0], e[1]] for e in split_edges]

#create dict: {t: [list of pairs where t0 >= t]}
t_edge_pairs = dict()

for x in t:
	d = [[e[0], e[1]] for e in split_edges if float(e[2]) >= x]
    	t_edge_pairs[x] = d


#generate list of unique_edges for each t
t_uniq_edges = dict()

for key in t_edge_pairs:
	temp_list = t_edge_pairs[key]
	flat_list = [item for sublist in temp_list for item in sublist]
    	t_uniq_edges[key] = list(set(flat_list))

#generate list of edges for each t

t_edges_with_repeats = dict()

for key in t_edge_pairs:
	temp_list = t_edge_pairs[key]
	flat_list = [item for sublist in temp_list for item in sublist]
	t_edges_with_repeats[key] = list(flat_list)

#edge-count for each t

t_edge_one = dict()

for key in t_edges_with_repeats:
	counter = Counter(t_edges_with_repeats[key])
	un_count = 0
	for k, v in counter.items():
		if v == 1:
			un_count += 1
	t_edge_one[key] = un_count

#number of unique edges for each t
t_uniq_edges_count = dict()

for key in t_edge_pairs:
   	t_uniq_edges_count[key]  = len(t_uniq_edges[key])

#for key in t_uniq_edges_count:
#	print(t_uniq_edges_count[key])

#t_uniq_edges_count_sorted = sorted(t_uniq_edges_count.items())

#h,z = zip(*t_uniq_edges_count_sorted)
t_edge_one = sorted(t_edge_one.items())

h,z = zip(*t_edge_one)

plt.plot(h,z)
plt.title("number of unique edges for each t")
plt.savefig("t_uniq_edges_count.png")
