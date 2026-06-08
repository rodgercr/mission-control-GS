# Mission Control AI

Sistema de monitoramento inteligente de uma missão espacial experimental, desenvolvido em **Python** para a Global Solution GS2026.1 (Pensamento Computacional e Automação com Python).

O programa simula o acompanhamento de uma missão dividida em **ciclos**. Em cada ciclo ele analisa cinco sensores, gera alertas automáticos, calcula o nível de risco e, ao final, apresenta um relatório completo com a situação geral da operação. Toda a "inteligência" do sistema é baseada em **regras lógicas** — sem bibliotecas externas, interface gráfica ou machine learning.

---

## Sobre o projeto

- **Nome da missão:** FIAP LightWeek 01
- **Equipe:** Equipe CCPK
- **Integrantes:**
  - Rodger Costa Rios – RM 571438
  - Kenichi Caio Yamamoto – RM 569815

---

## Como executar

O projeto usa apenas a biblioteca padrão do Python, então não é preciso instalar nada.

1. Tenha o **Python 3** instalado.
2. No terminal, dentro da pasta do projeto, execute:

```
python mission_control.py
```

O programa roda sozinho e imprime no terminal a análise de cada ciclo seguida do relatório final.

---

## Como o sistema funciona

### Estrutura dos dados

Os dados ficam guardados em uma **matriz** chamada `dados_missao` (uma lista de listas). Cada linha é um ciclo da missão e cada coluna é um sensor, sempre nesta ordem:

```
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

Existe também a lista `areas_monitoradas`, que dá nome a cada coluna, na mesma ordem:

| Posição | Sensor       | Área monitorada           |
|---------|--------------|---------------------------|
| 0       | Temperatura  | Temperatura interna       |
| 1       | Comunicação  | Comunicação com a base    |
| 2       | Bateria      | Sistema de energia        |
| 3       | Oxigênio     | Suporte de oxigênio       |
| 4       | Estabilidade | Estabilidade operacional  |

### Lógica geral

Para cada ciclo, o programa percorre os cinco sensores e classifica cada um como **NORMAL**, **ATENÇÃO** ou **CRÍTICO**. Cada classificação vira uma pontuação de risco, que é somada para definir o estado do ciclo inteiro. No final, o sistema compara os ciclos para identificar a tendência da missão e a área mais afetada.

---

## Regras de alerta

Cada sensor é classificado de acordo com as faixas abaixo. (As faixas seguem a sugestão do enunciado da GS.)

### Temperatura (°C)

| Condição                 | Classificação |
|--------------------------|---------------|
| menor que 18             | ATENÇÃO       |
| de 18 até 30             | NORMAL        |
| maior que 30 até 35      | ATENÇÃO       |
| maior que 35             | CRÍTICO       |

### Comunicação (%)

| Condição        | Classificação |
|-----------------|---------------|
| menor que 30    | CRÍTICO       |
| de 30 até 59    | ATENÇÃO       |
| 60 ou mais      | NORMAL        |

### Bateria (%)

| Condição        | Classificação |
|-----------------|---------------|
| menor que 20    | CRÍTICO       |
| de 20 até 49    | ATENÇÃO       |
| 50 ou mais      | NORMAL        |

### Oxigênio (%)

| Condição        | Classificação |
|-----------------|---------------|
| menor que 80    | CRÍTICO       |
| de 80 até 89    | ATENÇÃO       |
| 90 ou mais      | NORMAL        |

### Estabilidade (%)

| Condição        | Classificação |
|-----------------|---------------|
| menor que 40    | CRÍTICO       |
| de 40 até 69    | ATENÇÃO       |
| 70 ou mais      | NORMAL        |

---

## Pontuação e classificação

Cada classificação gera uma pontuação de risco:

| Classificação | Pontos |
|---------------|--------|
| NORMAL        | 0      |
| ATENÇÃO       | 1      |
| CRÍTICO       | 2      |

Como cada ciclo tem 5 sensores, a pontuação máxima de um ciclo é **10 pontos**.

Com base na soma, o ciclo é classificado assim:

| Pontuação total | Classificação do ciclo |
|-----------------|------------------------|
| 0 a 2 pontos    | MISSÃO ESTÁVEL         |
| 3 a 5 pontos    | MISSÃO EM ATENÇÃO      |
| 6 a 10 pontos   | MISSÃO CRÍTICA         |

---

## Análises do relatório final

- **Médias** de cada sensor ao longo de todos os ciclos.
- **Ciclo mais crítico** e a maior pontuação de risco registrada.
- **Risco médio** da missão e quantidade de ciclos críticos.
- **Tendência da missão:** compara o risco do primeiro ciclo com o do último para dizer se a missão melhorou, piorou ou permaneceu estável.
- **Área mais afetada:** soma o risco de cada área em todos os ciclos e aponta a que acumulou mais.
- **Classificação final** e uma **conclusão** sobre a operação.

---

## Estrutura do repositório

```
mission-control-GS/
│
├── README.md
└── mission_control.py
```

---

## Vídeo pitch

Link do vídeo de apresentação no YouTube: https://youtu.be/l2CnIkIQ7nA
