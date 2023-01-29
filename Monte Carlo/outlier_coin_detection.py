#problem : there's 16 coins; 15 regular and one special in that it always tosses to heads. 
#You get 15 tosses, after which you need to make a guess on the identity of the special coin. What's your strategy?

import random

num_coins = 16
num_tosses = num_coins-1


def get_secret_coin(n = num_coins):
	return random.randint(0,n-1);

def get_toss(coin, secret_coin):
	if coin == secret_coin:
		return "heads"
	return random.choice(["heads", "tails"])

#naive strategy : innocent until proven guilty - bet on one coin at a time, move to the next if you got a tails.

def trial_via_naive_strategy():
	secret_coin = get_secret_coin()
	guess = 0

	for _ in range(num_tosses):
		toss = get_toss(guess, secret_coin)
		if toss == "tails": 	#this means our guess is bad
			guess += 1

	return guess == secret_coin

num_trials = 100000
num_success = 0
for _ in range(num_trials):
	if(trial_via_naive_strategy()):
		num_success += 1

print(num_success/num_trials)
