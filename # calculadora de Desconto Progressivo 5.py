# calculadora de Desconto Progressivo



testes = [
    (80.00, "nao"),
    (200.00, "nao"),
    (200.00, "sim"),
    (450.00, "nao"),
    (1000.00, "sim")
]

for valor, vip in testes:
    if valor <= 100:
        percentual = 0
    elif valor <= 300:
        percentual = 10
    elif valor <= 500:
        percentual = 15
    else:
        percentual = 20

    desconto = valor * (percentual / 100)

    if vip == "sim":
        desconto_vip = valor * 0.05
    else:
        desconto_vip = 0

    valor_final = valor - desconto - desconto_vip

    print("=== Resumo da Compra ===")
    print(f"Valor original:      R$ {valor:.2f}")
    print(f"Desconto ({percentual}%):     R$ {desconto:.2f}")
    print(f"Desconto VIP (5%):   R$ {desconto_vip:.2f}")
    print(f"Valor final:         R$ {valor_final:.2f}")
    print()