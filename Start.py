#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, copy, random


class Start:
	def __init__(self):

		#Abre o Arquivo
		arq = open(sys.argv[1],'r')

		self.linhasArq = arq.read().splitlines()

		#variaveis
		self.inputAlph = self.linhasArq[0].split(" ")
		self.symbolNull = self.linhasArq[1].split(" ")
		self.states = self.linhasArq[2]
		self.initialState = self.linhasArq[3].split(" ")
		self.finalState = self.linhasArq[4].split(" ")
		
		self.tempTransitions = self.linhasArq[7:]
		self.transitions = []
		
		for i in self.tempTransitions:
			i = i.split(" ")
			t = list(i)
			self.transitions.append(t)


	def getInputAlph(self):
		return self.inputAlph

	def getSimbol(self):
		return self.symbolNull
	
	def getStates(self):
		return self.states
	
	def getInitial(self):
		return self.initialState
	
	def getFinal(self):
		return self.finalState
	
	def getTrans(self):
		return self.transitions