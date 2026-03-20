#exercocioo 7 


testes = [380, 1250, 70, 15, -100, 0]

for valor in testes:
    print(f"=== Saque: R$ {valor} ===")

    if valor <= 0:
        print("Valor inválido")
    elif valor % 10 != 0:
        print("Valor inválido")
    else:
        resto = valor

        ced_200 = resto // 200
        resto = resto % 200

        ced_100 = resto // 100
        resto = resto % 100

        ced_50 = resto // 50
        resto = resto % 50

        ced_20 = resto // 20
        resto = resto % 20

        ced_10 = resto // 10
        resto = resto % 10

        total_cedulas = ced_200 + ced_100 + ced_50 + ced_20 + ced_10

        print(f"R$ 200: {ced_200} cédula(s)")
        print(f"R$ 100: {ced_100} cédula(s)")
        print(f"R$ 50:  {ced_50} cédula(s)")
        print(f"R$ 20:  {ced_20} cédula(s)")
        print(f"R$ 10:  {ced_10} cédula(s)")
        print(f"Total de cédulas: {total_cedulas}")

    print()