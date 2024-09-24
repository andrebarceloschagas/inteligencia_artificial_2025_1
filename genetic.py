import numpy as np
import random
import itertools

# Definindo as distâncias entre as cidades (matriz de distâncias)
def gerar_matriz_distancias(num_cidades):
    matriz = np.random.randint(10, 100, size=(num_cidades, num_cidades))
    np.fill_diagonal(matriz, 0)
    return matriz

# Função que calcula o custo (distância total) de um cromossomo (rota)
def calcular_custo_rota(rota, matriz_distancias):
    custo_total = 0
    for i in range(len(rota) - 1):
        custo_total += matriz_distancias[rota[i], rota[i + 1]]
    custo_total += matriz_distancias[rota[-1], rota[0]]  # Retorno à cidade inicial
    return custo_total

# Função que gera a população inicial
def gerar_populacao_inicial(tamanho_populacao, num_cidades):
    return [random.sample(range(num_cidades), num_cidades) for _ in range(tamanho_populacao)]

# Função de seleção por torneio
def selecao_por_torneio(populacao, matriz_distancias, tamanho_torneio=3):
    melhor = None
    for _ in range(tamanho_torneio):
        individuo = random.choice(populacao)
        if melhor is None or calcular_custo_rota(individuo, matriz_distancias) < calcular_custo_rota(melhor, matriz_distancias):
            melhor = individuo
    return melhor

# Crossover de Ordem (Order Crossover - OX)
def crossover_ox(pai1, pai2):
    tamanho = len(pai1)
    ponto1, ponto2 = sorted(random.sample(range(tamanho), 2))
    
    filho = [None] * tamanho
    filho[ponto1:ponto2] = pai1[ponto1:ponto2]
    
    preenchimento = [cidade for cidade in pai2 if cidade not in filho]
    j = 0
    for i in range(tamanho):
        if filho[i] is None:
            filho[i] = preenchimento[j]
            j += 1
    return filho

# Mutação por troca de cidades
def mutacao(cromossomo, taxa_mutacao=0.01):
    if random.random() < taxa_mutacao:
        i, j = random.sample(range(len(cromossomo)), 2)
        cromossomo[i], cromossomo[j] = cromossomo[j], cromossomo[i]
    return cromossomo

# Função para executar o algoritmo genético
def algoritmo_genetico(matriz_distancias, num_cidades, tamanho_populacao=100, num_geracoes=500, taxa_crossover=0.9, taxa_mutacao=0.01):
    populacao = gerar_populacao_inicial(tamanho_populacao, num_cidades)
    melhor_solucao = min(populacao, key=lambda ind: calcular_custo_rota(ind, matriz_distancias))
    
    for geracao in range(num_geracoes):
        nova_populacao = []
        
        for _ in range(tamanho_populacao // 2):
            # Seleção de pais
            pai1 = selecao_por_torneio(populacao, matriz_distancias)
            pai2 = selecao_por_torneio(populacao, matriz_distancias)
            
            # Crossover
            if random.random() < taxa_crossover:
                filho1 = crossover_ox(pai1, pai2)
                filho2 = crossover_ox(pai2, pai1)
            else:
                filho1, filho2 = pai1[:], pai2[:]
            
            # Mutação
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            
            nova_populacao.extend([filho1, filho2])
        
        populacao = nova_populacao
        
        # Atualizar a melhor solução
        melhor_da_geracao = min(populacao, key=lambda ind: calcular_custo_rota(ind, matriz_distancias))
        if calcular_custo_rota(melhor_da_geracao, matriz_distancias) < calcular_custo_rota(melhor_solucao, matriz_distancias):
            melhor_solucao = melhor_da_geracao
        
        # Mostrar progresso
        if geracao % 100 == 0:
            print(f"Geração {geracao}: Melhor custo = {calcular_custo_rota(melhor_solucao, matriz_distancias)}")
    
    return melhor_solucao, calcular_custo_rota(melhor_solucao, matriz_distancias)

# Parâmetros do problema
num_cidades = 10
matriz_distancias = gerar_matriz_distancias(num_cidades)

# Executando o algoritmo genético
melhor_rota, melhor_custo = algoritmo_genetico(matriz_distancias, num_cidades)

print(f"Melhor rota encontrada: {melhor_rota}")
print(f"Custo da melhor rota: {melhor_custo}")
