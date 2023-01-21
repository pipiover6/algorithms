# The coupon collection problem (with 6 coupons) is the following: how long does it take, on average, to randomly roll a dice until all 6 faces have appeared at least once?
# The answer is n times the n'th harmonic number, i.e. approximately n.log(n) as n tends to infinity 
# The following code is a Monte Carlo simulation of copuon collection

import random

def get_random_coupon(num_coupons=6):
	return random.choice(range(num_coupons))


def random_coupon_collection_trial(num_coupons=6):
	items=[]
	num_items=0
	time=0
	while num_items<num_coupons:
		time += 1
		new_item = get_random_coupon()

		if new_item not in items:
			items.append(new_item)
			num_items+=1

		#print(f"{time}: rolled {new_item}, total {items}")

	#print(f"finished after seeing {time} coupons")
	return time


def average_over_trials(num_trials=10000):
	tot = 0
	for _ in range(num_trials):
		tot += random_coupon_collection_trial()
	return tot/num_trials

#print(average_over_trials())
