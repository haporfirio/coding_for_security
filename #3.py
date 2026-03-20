#3 

cotacoes = {
    "dolar": 5.15,
    "euro": 5.55,
    "libra": 6.45
}

print("[1] Real -> Dólar")
print("[2] Real -> Euro")
print("[3] Real -> Libra")

opcao = int(input("Escolha uma opção: "))

if opcao < 1 or opcao > 3:
    print("Opção inválida")
else:
    valor = float(input("Digite o valor em reais: R$ "))

    if valor < 0:
        print("Valor inválido")
    else:
        if opcao == 1:
            convertido = valor / cotacoes["dolar"]
            print(f"R$ {valor:.2f} = US$ {convertido:.2f}")
        elif opcao == 2:
            convertido = valor / cotacoes["euro"]
            print(f"R$ {valor:.2f} = € {convertido:.2f}")
        else:
            convertido = valor / cotacoes["libra"]
            print(f"R$ {valor:.2f} = £ {convertido:.2f}")