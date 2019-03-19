#Dice 
#Determine the probability of getting given scores for given dice
#Math originally checked against https://www.lucamoroni.it/the-dice-roll-sum-problem/

import math
import logging
k_0 = 0

def binomialCoefficient(top, bottom):
	#Top chooses Bottom
	upper = math.factorial(top)
	lower = math.factorial(bottom)*math.factorial(top-bottom)
	return upper/lower

def consecutiveRolls(n, s=6):
	#Odds of rolling any side are 1/s where s is the amount of sides on the die
	#For consecutive rolls, the odds are raised exponentially n times, where n are the number of rolls
	return math.pow((1/s), n)

def missRoll(n, s=6):
	return 1-consecutiveRolls(n, s)


def probabilityScoreOnDice(p, n, s=6):
	#Returns the probability of scoring p points on n dice with s sides each
	k_max = math.floor((p-n)/s)
	summation = 0
	for number in range(k_0, k_max+1):
		subsum = math.pow(-1, number)*binomialCoefficient(n,number)*binomialCoefficient((p-s*number-1), (p-s*number-n))
		summation = summation+subsum
	returnable =  (1/math.pow(s, n))*summation
	logging.debug("Probability of scoring " + str(p) + " on " + str(n) + "d" + str(s) + " is " + str(returnable))
	return returnable


def probabilityLessThan(p, n, s=6):
	x = n
	total = 0
	while x < p:
		adding = probabilityScoreOnDice(x,n,s)
		total = total + adding
		x = x+1
	logging.debug("Probability of scoring under " + str(p) + " on " + str(n) + "d" + str(s) + " is " + str(total))
	return total


def probabilityGreaterThan(p, n, s=6):
	x = n*s
	total = 0
	while x > p:
		adding = probabilityScoreOnDice(x,n,s)
		total = total + adding
		x = x-1
	logging.debug("Probability of scoring over " + str(p) + " on " + str(n) + "d" + str(s) + " is " + str(total))
	return total


def probabilityWeights(p, n, s=6):
	scoreList = []
	scoreList.append(probabilityLessThan(p, n, s))
	scoreList.append(probabilityScoreOnDice(p,n,s))
	scoreList.append(probabilityGreaterThan(p,n,s))
	return scoreList


if __name__ == "__main__":

	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

	scoreList = []
	scoreList.append(probabilityLessThan(17, 6, 8))
	scoreList.append(probabilityScoreOnDice(17,6,8))
	scoreList.append(probabilityGreaterThan(17,6,8))

	print(scoreList)
	print(sum(scoreList))