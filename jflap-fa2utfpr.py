# Linha 1: alfabeto de entrada
# Linha 2: simbolo a ser considerado para representar epsilon ou lambda (nao deve pertencer ao alfabeto de entrada)
# Lista 3: conjunto de estados
# Linha 4: estado inicial
# Linha 5: conjunto de estados de aceitacao
# Linhas 6 em diante: transicoes, uma por linha, cada qual no seguinte formato: estado atual, simbolo do alfabeto de entrada ou epsilon, estado destino


from xml.etree import ElementTree as ET
import csv
import sys

def set2list(dataset):
	sortedList = list(dataset)
	sortedList.sort()
	return sortedList


class Transition(object):
	def __init__(self):
		self.currentState = None
		self.currentInputSymbol = None
		self.newState = None

	def __lt__(self, other):
		if self.currentState != other.currentState:
			return self.currentState < other.currentState
		if self.currentInputSymbol != other.currentInputSymbol:
			return self.currentInputSymbol < other.currentInputSymbol
		return self.newState < other.newState 


class Jflap2Utfpr(object):
	def __init__(self):
		self.state_id_to_name = {}
		self.alphabet = set()
		self.states = set()
		self.initialStates = set()
		self.acceptanceStates = set()
		self.transitions = []
		self.blankSymbol = 'B'

	def convert(self, inputFile, outputFile, blankSymbol = 'B', alphabet = None):
		self.blankSymbol = blankSymbol
		if alphabet is not None:
			self.alphabet = alphabet

		xmldoc = ET.parse(inputFile)
		root = xmldoc.getroot()
		tm = root.find('automaton')
		if tm == None:  # Old JFLAP format
			tm = root

		for s in tm.findall('state'):
			state_id = s.attrib['id']
			if s.attrib.has_key('name'):
				state_name = s.attrib['name']
			else:
				state_name = str(state_id)
			self.state_id_to_name[state_id] = state_name
			self.states.add(state_name)
			if s.find('initial') is not None:
				self.initialStates.add(state_name)
			if s.find('final') is not None:
				self.acceptanceStates.add(state_name)

		for t in tm.findall('transition'):
			transition = Transition()
			self.transitions.append(transition)
			transition.currentState = self.state_id_to_name[t.find('from').text]
			transition.newState = self.state_id_to_name[t.find('to').text]
			if t.find('read').text is not None:
				transition.currentInputSymbol = t.find('read').text
				self.alphabet.add(transition.currentInputSymbol)
			else:
				transition.currentInputSymbol = blankSymbol
			self.transitions.sort()
		
		if self.blankSymbol in self.alphabet:
			for c in ascii_uppercase:
				if c not in self.alphabet:
					self.blankSymbol = c
				break
			print("Simbolo originalmente escolhido para representar branco foi utilizado para outros fins no automato. Simbolo para branco foi substituido por " + self.blankSymbol + ".")

		with open(outputFile, 'w') as csvfile:
			writer = csv.writer(csvfile, delimiter = ' ', escapechar = None, quotechar = None, quoting = csv.QUOTE_NONE, skipinitialspace = True)
			writer.writerow(set2list(self.alphabet))
			writer.writerow(self.blankSymbol)
			writer.writerow(set2list(self.states))
			writer.writerow(set2list(self.initialStates))
			writer.writerow(set2list(self.acceptanceStates))
			for t in self.transitions:
				writer.writerow([t.currentState, t.currentInputSymbol, t.newState])

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Parametros insuficientes. Informe o nome de arquivo de entrada e o nome do arquivo de saida")
		sys.exit(1)
	converter = Jflap2Utfpr()
	converter.convert(sys.argv[1], sys.argv[2], "B")

