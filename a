# The following is an implementation of the Misra-Gries heavy hitters algorithm, that given
# a (very large) collection of items returns those that reappear in high frequency (if any). 

# Inputs:
#			stream - a large collection of items
#			cutoff - a frequency in (0,1)
#
# Output:
#			A collection of all pairs (item,occurence) where $item_ is a (distinct) element of the
#			stream that appears exactly $occurence times and $occurence / len($stream) > $cutoff
#	
# Algorithm:
# 		For this explanation's sake, assume we are after all items appearing with frequency > 25%.
#			There can be 3 such items at most. We think of the items as entering the arena one by one.
#			If they find a group of items that are equal to them, they join that group. If not and they're new,
#			they form a new group and become its sole member. However, all groups agree that there can only be 3
#			groups present in the room at once. So, whenever a 4th group is formed, the three original groups
#			each sacrifice one member, and, along with the last item in the arena forming the new 4th group, all 4
#			items leave the arena. This is like in tetris - once the fourth and empty column gets an item, the row disappears.
#			Each group of > 25% frequency knows that no matter how many of its members will be sacrificed,
#			at the end there will be at least one surviving member to represent the group. 
#			Once we are left with < 4 final groups, we still have to check they represent items with high frequency.

import math
def heavy_hitters(stream, cutoff):

	assert(0 < cutoff and cutoff < 1)
	tetris = math.ceil(1/cutoff)

	itr = iter(stream)
	arena = {}

	while True:
		try:
			item = next(itr)
		
		except:
			break

		if item in arena:
			arena[item] += 1

		elif len(arena) + 1 < tetris:
			arena[item] = 1

		else:
			assert(len(arena) == tetris-1)
			for item in arena:
				arena[item] -= 1

			arena = {k:v for k,v in arena.items() if v > 0}

	assert(len(arena) < tetris)
	itr = iter(stream)
	counters = {item:0 for item in arena}

	while True:
		try:
			item = next(itr)
		
		except:
			break

		if item in counters:
			counters[item] += 1

	return {k:v for k,v in counters.items() if v > cutoff * len(stream)}



# Test:
import random
T = 1000
N = 20
M = 8
stream = []
for i in range(1,N+1):
	for _ in range(i):
		stream.append(i)

n = len(stream) # N(N+1)/2
assert(2*n == N*(N+1))

for _ in range(T):
	random.shuffle(stream)
	a = [x for x in heavy_hitters(stream,M/n)]
	a.sort()
	assert(a == [t for t in range(M+1,N+1)])


