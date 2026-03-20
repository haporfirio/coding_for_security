#exercicio1 

idade = int(input("Digite a idade: "))

if idade < 0 or idade > 120:
    print("Idade inválida")
elif idade <= 11:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")