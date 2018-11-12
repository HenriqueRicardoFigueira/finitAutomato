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
        -Variaveis
		      
          inputAlph
		      symbolNull
		      states
		      initialState
		      finalState
		      tempTransitions
          
        -Métodos
          
          def getInputAlph():
            Retorna alfabeto de entrada.
		      def getSimbol():
            Retorna símbolo em branco.
		      def getStates():
            Retorna estados.
          def getInitial():
            Retorna estado inicial.
		      def getFinal():
            Retorna lista de estados finais.
          def getTrans():
            Retorna lista de transições.
 
  -Pygraph
    

  -FITA
    


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
