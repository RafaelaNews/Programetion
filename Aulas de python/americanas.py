nome = input("tell your name: ")
idade = int(input("write your years old: "))
if(idade<=17):
    print(f"{nome}, {idade}, you're little years old")
elif(idade>17 and idade<60):
    print(f"{nome} you're big child {idade}")
else:
    print("go in americanas")


