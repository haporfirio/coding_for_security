testes = [
    {"entrada": 14, "saida": 16, "placa_final": 3, "dia": "quarta"},
    {"entrada": 9, "saida": 9, "placa_final": 7, "dia": "sexta"},
    {"entrada": 23, "saida": 2, "placa_final": 5, "dia": "sabado"},
    {"entrada": 8, "saida": 12, "placa_final": 4, "dia": "segunda"},
    {"entrada": 20, "saida": 3, "placa_final": 2, "dia": "segunda"}
]

for caso in testes:
    entrada = caso["entrada"]
    saida = caso["saida"]
    placa_final = caso["placa_final"]
    dia = caso["dia"]

    if saida >= entrada:
        horas = saida - entrada
    else:
        horas = (24 - entrada) + saida

    if horas == 0:
        horas = 1

    tarifa_base = 10 + (horas - 1) * 5

    noturno = 0
    if entrada >= 22 or entrada < 6 or saida <= 6:
        noturno = tarifa_base * 0.50

    subtotal = tarifa_base + noturno

    desconto = 0
    if dia == "segunda" and placa_final % 2 == 0:
        desconto = subtotal * 0.10

    total = subtotal - desconto

    print("=== Estacionamento ===")
    print(f"Entrada: {entrada:02d}h | Saída: {saida:02d}h")
    print(f"Permanência: {horas} horas")
    print(f"Tarifa base:            R$ {tarifa_base:.2f}")
    print(f"Adicional noturno (50%): R$ {noturno:.2f}")
    print(f"Desconto:               R$ {desconto:.2f}")
    print(f"Total:                  R$ {total:.2f}")
    print()