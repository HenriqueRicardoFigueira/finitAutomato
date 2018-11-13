# finitAutomato

## Get Start
Clone ou faça o Download do projeto em .zip (via terminal/manual) para sua maquina.
- Clone:
  - Execute o camando no Terminal e acessa a pasta do projeto:
    ```
    git clone https://github.com/HenriqueRicardoFigueira/finitAutomato.git
    cd finitAutomato-master/
    ```
- Download:
  - Execute no Terminal de comando:
    ```
    wget https://github.com/HenriqueRicardoFigueira/finitAutomato/archive/master.zip
    ```
  - Descompacte e abra a pasta do projeto:
    ```
    unzip finitAutomato-master.zip
    cd finitAutomato-master/

### Documentação
  -START

   	-funcionamento:
        	Responsável por quebrar o arquivo, colher corretamente os dados e retorna-los .
        	-Variaveis:
		      
          		inputAlph
			symbolNull
			states
			initialState
		 	finalState
			tempTransitions

		-Métodos:
			#retorna alfabeto de entrada.
			def getInputAlph(self):
		    		
			#retorna símbolo em branco.
			def getSimbol(self):
		    	
			#retorna lista de estados.	
			def getStates(self):
			
			#retorna estado inicial.	
		  	def getInitial(self):
		    		
			#retorna lista de estados finais.	
			def getFinal(self):
		    	
			#retorna lista de transições.
 			def getTrans(self):
		    		
  -Pygraph
  
  	-funcionamento:
		Responsavel pela criação do grafo e suas arestas.
		
	-Métodos:
	
   			#função para inserir dois nos e suas arestas ou uma aresta somente
    		def inserirNo(self, vertice):
        	
			#verifica se existe um vertice com o nome ja no grafo
			def verificaNomeVertice(self, vertice):
  

    		#verifica se existe um vertice com o nome ja no grafo
    		def retornVertByName(self, name):
    

    		#função para inserir uma nova aresta
    		def inserirAdj(self, vertice, vertice2, symbol):

    		#retorna a lista de adjascencia de um nó bidirecional
    		def getAdjacentes(self, no, Letter):


    		def retAdjacentes(self, no):

  
    

  -AF
  
  	-funcionamento:
		Responsavel por inserir estados no grafo, inserir transações nas arestas, marcar estados finais
		fazer a verificação de aceitação ou rejeição e caminhar no grafo.
	
	-Métodos:
		#retorna estado que está sendo processado no momento
		def getCurrentState(self, state):
 		
		#verifica a aceitação ou rejeição de uma palavra, tratando todos os casos que aceita ou
		rejeita. Na questão do não-determinismo, verifica quantas transações são possiveis para a 
		letra que está sendo processada, caminhando para todas possiveis e aplicando o tratamento de 
		aceitação ou rejeição. Quando uma transação "morre" ela vai para uma lista de remoções e é removida
		após a execução.
		def isEnd(self):
    		
		#caminnha com as transçãoes dentro do grafo, recuperando uma lista de adjacentes e verificando a quantidade de transações
		possiveis.
		def caminha(self):

    


### Passos para Execução:
- Execute o seguinte comando no terminal:
  ```
  python turing.py examples/(NOME DO ARQUIVO DA MAQUINA) "CONTEUDO DA FITA"
  ```
## Observações
Se você ja está perdido a ponto de ter chegado até aqui, vá em frente e se afunde de uma vez! :trollface:
## Autor
[Gabriel Negrão Silva](https://github.com/itsgnegrao). :alien:

[Henrique Ricardo Figueira](https://github.com/HenriqueRicardoFigueira). :alien:
