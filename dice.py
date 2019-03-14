#Brute force die roll
import math
import logging
k_0 = 0

def binomialCoefficient(top, bottom):
	#Top chooses Bottom
	upper = math.factorial(top)
	lower = math.factorial(bottom)*math.factorial(top-bottom)
	return upper/lower


def probabilityScoreOnDice(p, n, s):
	#Returns the probability of scoring p points on n dice with s sides each
	#https://www.lucamoroni.it/the-dice-roll-sum-problem/
	k_max = math.floor((p-n)/s)
	summation = 0
	for number in range(k_0, k_max+1):
		subsum = math.pow(-1, number)*binomialCoefficient(n,number)*binomialCoefficient((p-s*number-1), (p-s*number-n))
		summation = summation+subsum
	returnable =  (1/math.pow(s, n))*summation
	logging.debug("Probability of scoring " + str(p) + " on " + str(n) + "d" + str(s) + " is " + str(returnable))
	return returnable

def probabilityScoreOrLess(p, n, s):
	x = 0
	total = 0
	while x <= p:
		adding = probabilityScoreOnDice(x,n,s)
		total = total + adding
		x = x+1
	return total

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
x = probabilityScoreOrLess(17, 6, 8)
print(x)