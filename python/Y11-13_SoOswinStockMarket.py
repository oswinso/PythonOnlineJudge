#!/usr/bin/env python

"""
This module takes in a list of floats seperated by spaces, and returns the largest difference between two floats.
Author: Oswin So
"""

def main():
	raw = raw_input("Enter prices: \n")
	rawList = raw.split(" ")
	priceList = []
	for price in rawList:
		priceList.append(float(price))

	diff = 0;
	iIndex = 0;
	jIndex = 0;
	for i in range(0,len(rawList)-1):
		for j in range(i, len(rawList)):
			if priceList[j] - priceList[i] > diff:
				diff = priceList[j] - priceList[i]
				iIndex = i
				jIndex = j
	print "{} {}".format(priceList[iIndex], priceList[jIndex])

if __name__ == "__main__":
	main()