# LISTAS

#lista = [1,2,3,4,5]
#print(lista[2])
#lista[2]=4 #atribui um novo número para a posição 2 da lista
#print(lista[2])

# TUPLA

#Acessando valores da tupla 

#ponto=(1,2)
#print("Coordenada X:", ponto[0])
#print("Coordenada Y:", ponto[1])
#if(ponto[0]==1):
#  print("X é igual a 1")
#if(ponto[1]==2):
#  print("Y é igual a 2")
#print("Coordenada X: ", ponto[0])
#print("Coordenada X: ", ponto[1])
#lista_ponto = list(ponto) 
#print(lista_ponto)

# DICIONARIO

pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# ACESSANDO OS VALORES DO DICIONARIO

#print("Nome: ", pessoa["nome"])
#print("Idade: ", pessoa["idade"])
#print("Cidade: ", pessoa["cidade"])

# CONTADOR

#palavra = input("Entre com a palavra: ")
#contador = 0

#for letra in palavra:
    #if letra == 'a' or letra == 'A': 
        #contador += 1

#print("A letra 'a' aparece", contador, "vezes na palavra digitada") 

# ADD, REMOVER, LISTA

#cores = {"vermelho", "verde", "azul"} #criando conjunto de cores
#cores.add("amarelo") #adicionando uma cor ao conjunto
#cores.add("vermelho") #tentando adicionar um elemento duplicado no conjunto>não terá efeito
#print("Cores: ", cores)
#if "azul" in cores: #verificando se uma cor esta no conjunto
    #print("azul está no conjunto.")
#cores.remove("verde") #removendo uma cor do conjunto
#cores.add("roxo")
#print("Cores após remover verde", cores) #imprimindo novo conjunto

#   USO DO FOR
  #Pedindo ao usuário para inserir palavrase formando uma lista com palavras de comprimento maior que um valor especifico 

#comprimento_minimo = 6
#quantidade_palavras = int(input("Quantas palavras você gostaria de inserir? "))

#palavras = []
#for i in range(quantidade_palavras):
 #   palavra = input(f"Insira a palavra {i+1}: ")
  #  palavras.append(palavra)

#print("\nPalavras com comprimento maior que", comprimento_minimo, ":")
#for palavra in palavras:
 #   if len(palavra) > comprimento_minimo:
  #      print(palavra)    

  #LISTA ORDENADA

#import random

#lista_palavras = ["Pizzaria", "Chinesa", "Sushi", "Mexicana", "Italiana"]
#escolha_palavra = random.choice(lista_palavras)
#print("Iremos comer uma", escolha_palavra)
