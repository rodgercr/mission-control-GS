NOME_MISSAO = "FIAP LightWeek 01"
NOME_EQUIPE = "Equipe CCPK"

# Matriz: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [23, 94, 90, 97, 92],
    [26, 85, 78, 93, 86],
    [32, 68, 55, 88, 72],
    [37, 45, 40, 84, 58],
    [41, 24, 15, 76, 33],
    [33, 58, 47, 86, 62],
]

# Areas monitoradas
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]


# Funcoes de analise dos sensores

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", "Temperatura abaixo do esperado"
    elif valor <= 30:
        return "NORMAL", "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", "Temperatura elevada"
    else:
        return "CRÍTICO", "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", "Comunicação em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", "Comunicação instável"
    else:
        return "NORMAL", "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", "Bateria abaixo do recomendado"
    else:
        return "NORMAL", "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", "Estabilidade operacional reduzida"
    else:
        return "NORMAL", "Estabilidade operacional adequada"


# Pontuacao e classificacao

def pontuar(classificacao):
    if classificacao == "CRÍTICO":
        return 2
    elif classificacao == "ATENÇÃO":
        return 1
    else:
        return 0


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(classificacao_ciclo):
    if classificacao_ciclo == "MISSÃO CRÍTICA":
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
    elif classificacao_ciclo == "MISSÃO EM ATENÇÃO":
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Manter operação normal e continuar monitoramento."


# Funcoes do relatorio final

def analisar_tendencia(riscos_por_ciclo):
    primeiro = riscos_por_ciclo[0]
    ultimo = riscos_por_ciclo[-1]

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontos_por_area, areas):
    maior_pontuacao = pontos_por_area[0]
    indice_maior = 0

    for i in range(len(pontos_por_area)):
        if pontos_por_area[i] > maior_pontuacao:
            maior_pontuacao = pontos_por_area[i]
            indice_maior = i

    return areas[indice_maior]


def media_da_coluna(dados, coluna):
    soma = 0
    for ciclo in dados:
        soma = soma + ciclo[coluna]
    return soma / len(dados)


# Funcao principal

def main():
    riscos_por_ciclo = []
    pontos_por_area = [0, 0, 0, 0, 0]

    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    # Percorre todos os ciclos
    for indice in range(len(dados_missao)):
        ciclo = dados_missao[indice]
        numero_ciclo = indice + 1

        temperatura = ciclo[0]
        comunicacao = ciclo[1]
        bateria = ciclo[2]
        oxigenio = ciclo[3]
        estabilidade = ciclo[4]

        classe_temp, msg_temp = analisar_temperatura(temperatura)
        classe_com, msg_com = analisar_comunicacao(comunicacao)
        classe_bat, msg_bat = analisar_bateria(bateria)
        classe_oxi, msg_oxi = analisar_oxigenio(oxigenio)
        classe_est, msg_est = analisar_estabilidade(estabilidade)

        pontos_temp = pontuar(classe_temp)
        pontos_com = pontuar(classe_com)
        pontos_bat = pontuar(classe_bat)
        pontos_oxi = pontuar(classe_oxi)
        pontos_est = pontuar(classe_est)

        risco_ciclo = pontos_temp + pontos_com + pontos_bat + pontos_oxi + pontos_est
        riscos_por_ciclo.append(risco_ciclo)

        pontos_por_area[0] = pontos_por_area[0] + pontos_temp
        pontos_por_area[1] = pontos_por_area[1] + pontos_com
        pontos_por_area[2] = pontos_por_area[2] + pontos_bat
        pontos_por_area[3] = pontos_por_area[3] + pontos_oxi
        pontos_por_area[4] = pontos_por_area[4] + pontos_est

        classificacao = classificar_ciclo(risco_ciclo)
        recomendacao = gerar_recomendacao(classificacao)

        print()
        print(f"CICLO {numero_ciclo}")
        print("-" * 60)
        print(f"Temperatura: {temperatura} °C | {classe_temp} | {msg_temp}")
        print(f"Comunicação: {comunicacao}% | {classe_com} | {msg_com}")
        print(f"Bateria: {bateria}% | {classe_bat} | {msg_bat}")
        print(f"Oxigênio: {oxigenio}% | {classe_oxi} | {msg_oxi}")
        print(f"Estabilidade: {estabilidade}% | {classe_est} | {msg_est}")
        print()
        print(f"Pontuação de risco do ciclo: {risco_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

    # Relatorio final
    media_temp = media_da_coluna(dados_missao, 0)
    media_com = media_da_coluna(dados_missao, 1)
    media_bat = media_da_coluna(dados_missao, 2)
    media_oxi = media_da_coluna(dados_missao, 3)
    media_est = media_da_coluna(dados_missao, 4)

    maior_risco = riscos_por_ciclo[0]
    ciclo_mais_critico = 1
    for i in range(len(riscos_por_ciclo)):
        if riscos_por_ciclo[i] > maior_risco:
            maior_risco = riscos_por_ciclo[i]
            ciclo_mais_critico = i + 1

    risco_medio = sum(riscos_por_ciclo) / len(riscos_por_ciclo)

    ciclos_criticos = 0
    for risco in riscos_por_ciclo:
        if risco >= 6:
            ciclos_criticos = ciclos_criticos + 1

    tendencia = analisar_tendencia(riscos_por_ciclo)
    area_mais_afetada = identificar_area_mais_afetada(pontos_por_area, areas_monitoradas)
    classificacao_final = classificar_ciclo(risco_medio)

    print()
    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print()
    print(f"Média de temperatura: {media_temp:.2f} °C")
    print(f"Média de comunicação: {media_com:.2f}%")
    print(f"Média de bateria: {media_bat:.2f}%")
    print(f"Média de oxigênio: {media_oxi:.2f}%")
    print(f"Média de estabilidade: {media_est:.2f}%")
    print()
    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {ciclos_criticos}")
    print()
    print("Tendência da missão:")
    print(tendencia)
    print()
    print("Pontuação acumulada por área:")
    for i in range(len(areas_monitoradas)):
        print(f"{areas_monitoradas[i]}: {pontos_por_area[i]} pontos")
    print()
    print("Área mais afetada:")
    print(area_mais_afetada)
    print()
    print("Classificação final da missão:")
    print(classificacao_final)
    print()
    print("Conclusão:")
    if classificacao_final == "MISSÃO CRÍTICA":
        print("A missão enfrentou falhas graves e exige intervenção imediata da equipe.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("A missão apresentou instabilidade relevante durante a operação. Ainda")
        print("existem sistemas em atenção e a equipe deve manter o plano de contingência ativo.")
    else:
        print("A missão se manteve estável e dentro dos parâmetros esperados.")


main()
