import json


def questao_1():
    INDICE = 13
    SOMA = 0
    K = 0
    
    while K < INDICE:
        K += 1
        SOMA += K
    
    print(f"O valor final de SOMA é: {SOMA}")

def questao_2(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        print(f"{numero} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero} não pertence à sequência de Fibonacci.")

def questao_3():
    dados_faturamento = '''
    [
        {
            "dia": 1,
            "valor": 22174.1664
        },
        {
            "dia": 2,
            "valor": 24537.6698
        },
        {
            "dia": 3,
            "valor": 26139.6134
        },
        {
            "dia": 4,
            "valor": 0.0
        },
        {
            "dia": 5,
            "valor": 0.0
        },
        {
            "dia": 6,
            "valor": 26742.6612
        },
        {
            "dia": 7,
            "valor": 0.0
        },
        {
            "dia": 8,
            "valor": 42889.2258
        },
        {
            "dia": 9,
            "valor": 46251.174
        },
        {
            "dia": 10,
            "valor": 11191.4722
        },
        {
            "dia": 11,
            "valor": 0.0
        },
        {
            "dia": 12,
            "valor": 0.0
        },
        {
            "dia": 13,
            "valor": 3847.4823
        },
        {
            "dia": 14,
            "valor": 373.7838
        },
        {
            "dia": 15,
            "valor": 2659.7563
        },
        {
            "dia": 16,
            "valor": 48924.2448
        },
        {
            "dia": 17,
            "valor": 18419.2614
        },
        {
            "dia": 18,
            "valor": 0.0
        },
        {
            "dia": 19,
            "valor": 0.0
        },
        {
            "dia": 20,
            "valor": 35240.1826
        },
        {
            "dia": 21,
            "valor": 43829.1667
        },
        {
            "dia": 22,
            "valor": 18235.6852
        },
        {
            "dia": 23,
            "valor": 4355.0662
        },
        {
            "dia": 24,
            "valor": 13327.1025
        },
        {
            "dia": 25,
            "valor": 0.0
        },
        {
            "dia": 26,
            "valor": 0.0
        },
        {
            "dia": 27,
            "valor": 25681.8318
        },
        {
            "dia": 28,
            "valor": 1718.1221
        },
        {
            "dia": 29,
            "valor": 13220.495
        },
        {
            "dia": 30,
            "valor": 8414.61
        }
    ]
    '''
    dados = json.loads(dados_faturamento)

    faturamentos_validos = [d["valor"] for d in dados if d["valor"] > 0]
    
    menor_valor = min(faturamentos_validos)
    maior_valor = max(faturamentos_validos)
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)
    
    dias_acima_media = sum(1 for valor in faturamentos_validos if valor > media_mensal)
    
    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

def questao_4():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    faturamento_total = sum(faturamento_estados.values())
    
    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}%")

def questao_5(texto):
    texto_invertido = ""
    for i in range(len(texto)-1, -1, -1):
        texto_invertido += texto[i]
    print(f"String invertida: {texto_invertido}")

def mostrar_menu():
    print("\nEscolha uma questão:")
    print("1 - Valor da variável SOMA")
    print("2 - Verificar se número pertence à sequência de Fibonacci")
    print("3 - Faturamento diário")
    print("4 - Percentual de faturamento por estado")
    print("5 - Inverter uma string")
    print("6 - Sair")

def escolher_questao():
    while True:
        mostrar_menu()
        escolha = input("Digite o número da questão que deseja resolver: ")

        if escolha == '1':
            questao_1()
        
        elif escolha == '2':
            numero = int(input("Digite um número para verificar na sequência de Fibonacci: "))
            questao_2(numero)
        
        elif escolha == '3':
            questao_3()
        
        elif escolha == '4':
            questao_4()
        
        elif escolha == '5':
            texto = input("Digite a string que deseja inverter: ")
            questao_5(texto)
        
        elif escolha == '6':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    escolher_questao()
