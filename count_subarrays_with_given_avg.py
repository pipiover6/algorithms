def naive_count_subarrays_with_given_avg(arr,avg):
	ret = 0
	n = len(arr)
	for i in range(n):
		s = 0
		for j in range(i,n):
			s += arr[j]
			if s == (j-i+1) * avg:
				ret += 1
	return ret

def choose2(x):
	return (x*(x-1))/2

def accumulated_sums_array(arr):
	ret = arr.copy()
	for i in range(1,len(arr)):
		ret[i] += ret[i-1]
	return ret


def frequencies(arr):
	ret = {}
	for x in arr:
		if x in ret:
			ret[x] += 1
		else:
			ret[x] = 1
	return ret

# Algorithm:
# 		By reducing arr's elements by avg, we may assume avg=0. Now we are after subarrays with sum 0.
#			By moving to the accumulated sum array, we are after pairs of elements with equal entries.
#			For example, if the arr = [1,2,3,4,5] and avg = 3, then we first move to [-2,-1,0,1,2] and then to
#			[0,-2,-3,-3,-2,0] and we have 3 pairs of equal elements.

def count_subarrays_with_given_avg(arr,avg):
	lowered_arr = [x - avg for x in arr]
	summed_arr = accumulated_sums_array(lowered_arr)
	freq = frequencies(summed_arr)
	
	if 0 in freq:
		freq[0] += 1
	
	return sum([choose2(freq[k]) for k in freq])
