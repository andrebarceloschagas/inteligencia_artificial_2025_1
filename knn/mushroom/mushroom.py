
import csv
import math
import random


class KNNClassificadorCogumelos:
    """
    Implementação do algoritmo K-Nearest Neighbors (K-Vizinhos Mais Próximos)
    para classificação do dataset de cogumelos (venenosos vs comestíveis).
    
    Este classificador utiliza codificação one-hot para lidar com variáveis categóricas.
    """
    
    def __init__(self, k=5):
        """
        Inicializa o classificador KNN para cogumelos.
        
        Args:
            k (int): Número de vizinhos a considerar para classificação
        """
        self.k = k
        self.dados_treino = []
        self.mapeamento_codificacao = {}
        self.cabecalho_processado = []
    
    def distancia_euclidiana(self, ponto1, ponto2):
        """
        Calcula a distância euclidiana entre dois pontos.
        
        Args:
            ponto1: Lista com as características do primeiro ponto
            ponto2: Lista com as características do segundo ponto
            
        Returns:
            float: Distância euclidiana entre os pontos
        """
        distancia = 0
        for i in range(len(ponto1)):
            distancia += (ponto1[i] - ponto2[i])**2
        return math.sqrt(distancia)
    
    def obter_vizinhos(self, instancia_teste):
        """
        Encontra os k vizinhos mais próximos de uma instância de teste.
        
        Args:
            instancia_teste: Lista com as características da instância a classificar
            
        Returns:
            list: Lista com os k vizinhos mais próximos
        """
        distancias = []
        for instancia_treino in self.dados_treino:
            # Calcula distância apenas com as características (exclui o rótulo)
            dist = self.distancia_euclidiana(instancia_teste[:-1], instancia_treino[:-1])
            distancias.append((instancia_treino, dist))
        
        # Ordena por distância (menor para maior)
        distancias.sort(key=lambda x: x[1])
        
        # Retorna os k vizinhos mais próximos
        vizinhos = []
        for i in range(self.k):
            vizinhos.append(distancias[i][0])
        return vizinhos
    
    def predizer_classificacao(self, vizinhos):
        """
        Prediz a classificação baseada nos vizinhos mais próximos.
        
        Args:
            vizinhos: Lista dos vizinhos mais próximos
            
        Returns:
            str: Classe predita (mais votada entre os vizinhos)
        """
        votos_classe = {}
        for vizinho in vizinhos:
            rotulo = vizinho[-1]  # Último elemento é o rótulo da classe
            if rotulo in votos_classe:
                votos_classe[rotulo] += 1
            else:
                votos_classe[rotulo] = 1
        
        # Ordena por número de votos (maior para menor)
        votos_ordenados = sorted(votos_classe.items(), key=lambda x: x[1], reverse=True)
        return votos_ordenados[0][0]
    
    def codificar_one_hot(self, dataset, cabecalho):
        """
        Aplica codificação one-hot para variáveis categóricas.
        
        Args:
            dataset: Dataset com variáveis categóricas
            cabecalho: Lista com nomes das colunas
            
        Returns:
            list: Dataset codificado com one-hot encoding
        """
        dataset_codificado = []
        todos_valores = {}  # Armazena todos os valores únicos para cada característica
        
        # Coleta todos os valores únicos para cada característica (exceto a coluna alvo)
        for i, nome_caracteristica in enumerate(cabecalho[:-1]):
            todos_valores[nome_caracteristica] = set()
            for linha in dataset:
                todos_valores[nome_caracteristica].add(linha[i])
        
        # Cria um mapeamento para cada valor único para um inteiro
        self.mapeamento_codificacao = {}
        for nome_caracteristica, valores in todos_valores.items():
            self.mapeamento_codificacao[nome_caracteristica] = {
                valor: idx for idx, valor in enumerate(sorted(list(valores)))
            }
        
        # Aplica a codificação one-hot
        for linha in dataset:
            linha_codificada = []
            for i, nome_caracteristica in enumerate(cabecalho[:-1]):
                # Codifica one-hot para cada característica categórica
                vetor_one_hot = [0] * len(todos_valores[nome_caracteristica])
                vetor_one_hot[self.mapeamento_codificacao[nome_caracteristica][linha[i]]] = 1
                linha_codificada.extend(vetor_one_hot)
            linha_codificada.append(linha[-1])  # Adiciona o rótulo alvo
            dataset_codificado.append(linha_codificada)
        
        return dataset_codificado
    
    def treinar(self, dados_treino):
        """
        Treina o classificador com os dados de treino.
        
        Args:
            dados_treino: Lista com os dados de treinamento codificados
        """
        self.dados_treino = dados_treino
    
    def predizer(self, instancia_teste):
        """
        Faz a predição para uma instância de teste.
        
        Args:
            instancia_teste: Instância a ser classificada
            
        Returns:
            str: Classe predita
        """
        vizinhos = self.obter_vizinhos(instancia_teste)
        return self.predizer_classificacao(vizinhos)


def carregar_dataset_cogumelos(nome_arquivo):
    """
    Carrega o dataset de cogumelos de um arquivo CSV.
    
    Args:
        nome_arquivo (str): Caminho para o arquivo CSV
        
    Returns:
        tuple: (dataset, cabecalho) ou (None, None) em caso de erro
    """
    dataset = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            cabecalho = next(leitor_csv)  # Lê o cabeçalho
            print(f"Cabeçalho encontrado: {cabecalho}")
            
            linha_num = 1
            for linha in leitor_csv:
                linha_num += 1
                # Pula linhas vazias
                if not linha or len(linha) == 0:
                    continue
                
                # Verifica se a linha tem o número correto de colunas
                if len(linha) != len(cabecalho):
                    print(f"Aviso: Linha {linha_num} tem número incorreto de colunas: {linha}")
                    continue
                
                # Remove espaços em branco
                linha_limpa = [item.strip() for item in linha]
                dataset.append(linha_limpa)
                
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado!")
        return None, None
    except Exception as e:
        print(f"Erro ao carregar dataset: {e}")
        return None, None
    
    if len(dataset) == 0:
        print("Erro: Nenhum dado foi carregado do arquivo!")
        return None, None
    
    print(f"Carregadas {len(dataset)} amostras do dataset")
    return dataset, cabecalho


def processar_dataset_cogumelos(dataset, cabecalho):
    """
    Processa o dataset verificando se a coluna alvo já está na posição correta.
    
    Args:
        dataset: Dataset original
        cabecalho: Cabeçalho original
        
    Returns:
        tuple: (dataset_processado, cabecalho_processado)
    """
    # Verifica se a última coluna é 'poisonous' ou similar
    if 'poisonous' in cabecalho[-1].lower() or cabecalho[-1].lower() in ['class', 'target', 'label']:
        # A coluna alvo já está no final, não precisa mover
        print("Coluna alvo já está na posição correta (final)")
        return dataset, cabecalho
    else:
        # Assume que a primeira coluna é o alvo, move para o final
        print("Movendo coluna alvo da primeira para a última posição")
        dataset_processado = []
        for linha in dataset:
            dataset_processado.append(linha[1:] + [linha[0]])
        
        cabecalho_processado = cabecalho[1:] + [cabecalho[0]]
        return dataset_processado, cabecalho_processado


def dividir_dataset(dataset, proporcao_treino=0.8, embaralhar=True):
    """
    Divide o dataset em conjuntos de treino e teste.
    
    Args:
        dataset: Dataset completo
        proporcao_treino (float): Proporção dos dados para treino (0.0 a 1.0)
        embaralhar (bool): Se deve embaralhar os dados antes de dividir
        
    Returns:
        tuple: (dados_treino, dados_teste)
    """
    if embaralhar:
        dataset_copia = dataset.copy()
        random.shuffle(dataset_copia)
        dataset = dataset_copia
    
    tamanho_treino = int(len(dataset) * proporcao_treino)
    dados_treino = dataset[:tamanho_treino]
    dados_teste = dataset[tamanho_treino:]
    
    return dados_treino, dados_teste


def avaliar_modelo(classificador, dados_teste):
    """
    Avalia o desempenho do modelo nos dados de teste.
    
    Args:
        classificador: Classificador KNN treinado
        dados_teste: Dados de teste
        
    Returns:
        tuple: (acuracia, predicoes_corretas, total_testes)
    """
    predicoes_corretas = 0
    predicoes = []
    
    print(f"Avaliando modelo com k={classificador.k}...")
    print("-" * 70)
    
    for i, instancia_teste in enumerate(dados_teste):
        predicao = classificador.predizer(instancia_teste)
        rotulo_real = instancia_teste[-1]
        predicoes.append(predicao)
        
        # Traduz os rótulos para português
        rotulo_real_pt = "Venenoso" if rotulo_real == 'p' else "Comestível"
        predicao_pt = "Venenoso" if predicao == 'p' else "Comestível"
        
        print(f'Teste {i+1:3d}: Esperado: {rotulo_real_pt:10s} | Predito: {predicao_pt:10s}', end='')
        
        if predicao == rotulo_real:
            predicoes_corretas += 1
            print(' ✓')
        else:
            print(' ✗')
    
    acuracia = (predicoes_corretas / len(dados_teste)) * 100
    return acuracia, predicoes_corretas, len(dados_teste)

def main():
    """
    Função principal que executa o algoritmo KNN no dataset de cogumelos.
    """
    print("=" * 80)
    print("    CLASSIFICADOR KNN - DATASET DE COGUMELOS")
    print("    (Venenosos vs Comestíveis)")
    print("=" * 80)
    
    # Configurações
    nome_arquivo = 'mushrooms.csv'
    k = 5  # Número de vizinhos
    proporcao_treino = 0.8  # 80% para treino, 20% para teste
    
    # Carrega o dataset
    print(f"Carregando dataset do arquivo: {nome_arquivo}")
    dataset, cabecalho = carregar_dataset_cogumelos(nome_arquivo)
    
    if dataset is None:
        print("Não foi possível carregar o dataset. Encerrando programa.")
        return
    
    print(f"Dataset carregado com sucesso! Total de amostras: {len(dataset)}")
    
    # Processa o dataset (move coluna alvo para o final)
    print("Processando dataset...")
    dataset_processado, cabecalho_processado = processar_dataset_cogumelos(dataset, cabecalho)
    
    # Mostra algumas estatísticas do dataset
    classes = {}
    for amostra in dataset_processado:
        classe = amostra[-1]
        classes[classe] = classes.get(classe, 0) + 1
    
    print(f"Classes encontradas:")
    for classe, quantidade in classes.items():
        classe_nome = "Venenoso" if classe == 'p' else "Comestível"
        print(f"  - {classe_nome} ({classe}): {quantidade} amostras")
    
    # Cria e configura o classificador
    print(f"\nInicializando classificador KNN com k={k}...")
    classificador = KNNClassificadorCogumelos(k=k)
    
    # Aplica codificação one-hot
    print("Aplicando codificação one-hot para variáveis categóricas...")
    dataset_codificado = classificador.codificar_one_hot(dataset_processado, cabecalho_processado)
    
    # Calcula dimensões após codificação
    dimensoes_originais = len(cabecalho_processado) - 1  # Excluindo coluna alvo
    dimensoes_codificadas = len(dataset_codificado[0]) - 1  # Excluindo coluna alvo
    print(f"Dimensões: {dimensoes_originais} características originais → {dimensoes_codificadas} após one-hot encoding")
    
    # Divide o dataset em treino e teste
    print(f"\nDividindo dataset: {proporcao_treino*100:.0f}% treino, {(1-proporcao_treino)*100:.0f}% teste")
    dados_treino, dados_teste = dividir_dataset(dataset_codificado, proporcao_treino, embaralhar=True)
    
    print(f"Conjunto de treino: {len(dados_treino)} amostras")
    print(f"Conjunto de teste: {len(dados_teste)} amostras")
    
    # Treina o classificador
    print(f"\nTreinando classificador...")
    classificador.treinar(dados_treino)
    
    # Avalia o modelo
    print(f"\nIniciando avaliação do modelo:")
    acuracia, corretas, total = avaliar_modelo(classificador, dados_teste)
    
    # Mostra resultados finais
    print("\n" + "=" * 80)
    print("                    RESULTADOS FINAIS")
    print("=" * 80)
    print(f"Total de instâncias de teste: {total}")
    print(f"Predições corretas: {corretas}")
    print(f"Predições incorretas: {total - corretas}")
    print(f"Acurácia: {acuracia:.2f}%")
    
    # Interpretação dos resultados
    if acuracia >= 95:
        print("🎯 Excelente! O modelo tem performance muito alta.")
    elif acuracia >= 85:
        print("👍 Boa performance! O modelo é confiável.")
    elif acuracia >= 70:
        print("⚠️  Performance moderada. Considere ajustar parâmetros.")
    else:
        print("❌ Performance baixa. Revisão do modelo necessária.")
    
    # Avalia diferentes valores de k
    print(f"\n" + "-" * 80)
    print("COMPARAÇÃO COM DIFERENTES VALORES DE K")
    print("-" * 80)
    
    valores_k = [1, 3, 5, 7, 9, 11]
    melhor_k = k
    melhor_acuracia = acuracia
    
    for k_teste in valores_k:
        if k_teste != k:  # Não testa o k já usado
            classificador_teste = KNNClassificadorCogumelos(k=k_teste)
            classificador_teste.treinar(dados_treino)
            
            # Avalia sem imprimir detalhes
            corretas_teste = 0
            for instancia_teste in dados_teste:
                predicao = classificador_teste.predizer(instancia_teste)
                if predicao == instancia_teste[-1]:
                    corretas_teste += 1
            
            acuracia_teste = (corretas_teste / len(dados_teste)) * 100
            print(f"k={k_teste:2d}: {acuracia_teste:6.2f}% de acurácia")
            
            if acuracia_teste > melhor_acuracia:
                melhor_k = k_teste
                melhor_acuracia = acuracia_teste
        else:
            print(f"k={k:2d}: {acuracia:6.2f}% de acurácia (usado acima)")
    
    print(f"\nMelhor k encontrado: {melhor_k} com {melhor_acuracia:.2f}% de acurácia")
    
    # Informações sobre as características
    print(f"\n" + "-" * 80)
    print("INFORMAÇÕES SOBRE O DATASET")
    print("-" * 80)
    print(f"Características analisadas:")
    for i, caracteristica in enumerate(cabecalho_processado[:-1], 1):
        print(f"  {i:2d}. {caracteristica}")
    
    print(f"\nTotal de {len(cabecalho_processado)-1} características categóricas")
    print(f"Cada característica foi convertida em múltiplas variáveis binárias (one-hot encoding)")
    print(f"Resultado: {dimensoes_codificadas} variáveis numéricas para o algoritmo KNN")


# Execução principal
if __name__ == '__main__':
    # Define semente para reprodutibilidade dos resultados
    random.seed(42)
    main()
