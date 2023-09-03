print("Rafaela")
print("18")
print("Rafaela", "Lavor", "Santos")
print("Dia", "Mês", "Ano", sep='/')
print("Dia", "Mês", "Ano ", end='')
print(2023)

#ENTRADA DE DADOS

nome = input("Qual seu nome? ")
print("Seu nome é: ", nome)
nome = int(input("Insira seu nome "))
print(type(nome))

#TIPOS DE CLASS

print(type("Rafaela")) #STR
print(type(7)) #INT
print(type(10.5)) #FLOUT
print(type(True or False)) #BOOLEANO
print(type(34j)) #COMPLEX

#VARIAVEIS 

nome= "Rafaela"
print(nome)

#OPERADORES ARITMETICOS

print( 14 % 5) #resto da divisão
print( 14//5 ) #divisão com resultado inteiro
 
#OPERADOR DE ATRIBUIÇÃO

a = 1
b = 2 
c = 3

a+=5 #a = a + 5
print(a)
b-=5 #b = b - 5
print(b)
c/=4 #c = c / 4
print(c)

#OPERADOR DE COMPARAÇÃO

print( 7 == 8 ) #verifica se os valores são iguais
print( 7 != 8 ) #verifica se os valores são diferentes
print( 7 > 8 )  #verifica se os valores são maior que 
print( 7 < 8 )  #verifica se os valores são menor que
print( 7>= 8 )  #verifica se o valor é maior ou igual
print( 7<= 8 )  #verifica se o valor é menor ou igual

#OPERADORES LOGICOS

x = 5
numero = x > 1 and x == 5 #Operador AND verifica se todas as condições são verdadeiras, então retorna TRUE
print(numero)

numero = x > 1 or x == 5 #Operador OR verifica se uma das condições são verdadeiras, então retorna TRUE
print(numero)

numero = not( x > 1 or x == 5 ) #Operador NOT inverte o valor de saida da expressão
print(numero)

#CONCATENAÇÃO, CONVERSÃO DE TIPOS E FORMATAÇÃO

primeiro_nome = "Rafaela "
sobrenome = "Adria"
Idade = 22
altura = 1.76

print("Ola, o meu nome é: " + primeiro_nome + sobrenome) #Concatenação de Strings
print("Ola, o meu nome é: " + primeiro_nome + sobrenome, "e minha idade é", Idade) #Concatenação de String e números usando virgula
print("Ola, o meu nome é: " + primeiro_nome + sobrenome, "e minha idade é", str(Idade)) #Concatenação de string e numeros usando virgula e a conversão
print("Ola, o meu nome é: " + primeiro_nome + sobrenome + "e minha idade é " + str(Idade)) #Concatenação de string e numeros usando virgula e a conversão 

#SAIDA E ENTRADA DE DADOS, OPERADORES ARITMETICOS

print("Conversão de metros para Centimetros")
metros = float(input("Insira o valor em metros "))
print(f"O valor em " , metros ,"metros equivale a ", metros * 100, "centimetros")

print("Conversão de centimetros em metros")
cent = float(input("Insira o valor em metros "))
print(f"O valor em", cent, "centimetros equivale a", cent / 100 ,"metros")
