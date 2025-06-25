
import csv
import math
import random


class KNNClassificador:
    """
    Implementação do algoritmo K-Nearest Neighbors (K-Vizinhos Mais Próximos)
    para classificação do dataset Iris.
    """
    
    def __init__(self, k=3):
        """
        Inicializa o classificador KNN.
        
        Args:
            k (int): Número de vizinhos a considerar para classificação
        """
        self.k = k
        self.dados_treino = []
    
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
    
    def treinar(self, dados_treino):
        """
        Treina o classificador com os dados de treino.
        
        Args:
            dados_treino: Lista com os dados de treinamento
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


def carregar_dataset_iris(nome_arquivo):
    """
    Carrega o dataset Iris de um arquivo CSV.
    
    Args:
        nome_arquivo (str): Caminho para o arquivo CSV
        
    Returns:
        list: Dataset carregado com características numéricas e rótulos
    """
    dataset = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            cabecalho = next(leitor_csv)  # Pula a linha de cabeçalho
            print(f"Cabeçalho encontrado: {cabecalho}")
            
            linha_num = 1  # Começa em 1 pois já lemos o cabeçalho
            for linha in leitor_csv:
                linha_num += 1
                # Pula linhas vazias
                if not linha or len(linha) == 0:
                    continue
                
                # Verifica se a linha tem o número correto de colunas
                if len(linha) < 5:
                    print(f"Aviso: Linha {linha_num} tem menos de 5 colunas: {linha}")
                    continue
                
                try:
                    # Converte características numéricas para float e mantém espécie como string
                    amostra = [float(x.strip()) for x in linha[:-1]] + [linha[-1].strip()]
                    dataset.append(amostra)
                except ValueError as e:
                    print(f"Erro na linha {linha_num}: {e}")
                    print(f"Conteúdo da linha: {linha}")
                    continue
                    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado!")
        return None
    except Exception as e:
        print(f"Erro ao carregar dataset: {e}")
        return None
    
    if len(dataset) == 0:
        print("Erro: Nenhum dado foi carregado do arquivo!")
        return None
    
    print(f"Carregadas {len(dataset)} amostras do dataset")
    return dataset


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
    print("-" * 50)
    
    for i, instancia_teste in enumerate(dados_teste):
        predicao = classificador.predizer(instancia_teste)
        rotulo_real = instancia_teste[-1]
        predicoes.append(predicao)
        
        print(f'Teste {i+1:2d}: Esperado: {rotulo_real:15s} | Predito: {predicao:15s}', end='')
        
        if predicao == rotulo_real:
            predicoes_corretas += 1
            print(' ✓')
        else:
            print(' ✗')
    
    acuracia = (predicoes_corretas / len(dados_teste)) * 100
    return acuracia, predicoes_corretas, len(dados_teste)

def main():
    """
    Função principal que executa o algoritmo KNN no dataset Iris.
    """
    print("=" * 60)
    print("    CLASSIFICADOR KNN - DATASET IRIS")
    print("=" * 60)
    
    # Configurações
    nome_arquivo = 'iris.csv'
    k = 3  # Número de vizinhos
    proporcao_treino = 0.8  # 80% para treino, 20% para teste
    
    # Carrega o dataset
    print(f"Carregando dataset do arquivo: {nome_arquivo}")
    dataset = carregar_dataset_iris(nome_arquivo)
    
    if dataset is None:
        print("Não foi possível carregar o dataset. Encerrando programa.")
        return
    
    print(f"Dataset carregado com sucesso! Total de amostras: {len(dataset)}")
    
    # Mostra algumas estatísticas do dataset
    classes = {}
    for amostra in dataset:
        classe = amostra[-1]
        classes[classe] = classes.get(classe, 0) + 1
    
    print(f"Classes encontradas:")
    for classe, quantidade in classes.items():
        print(f"  - {classe}: {quantidade} amostras")
    
    # Divide o dataset em treino e teste
    print(f"\nDividindo dataset: {proporcao_treino*100:.0f}% treino, {(1-proporcao_treino)*100:.0f}% teste")
    dados_treino, dados_teste = dividir_dataset(dataset, proporcao_treino, embaralhar=True)
    
    print(f"Conjunto de treino: {len(dados_treino)} amostras")
    print(f"Conjunto de teste: {len(dados_teste)} amostras")
    
    # Cria e treina o classificador
    print(f"\nTreinando classificador KNN com k={k}...")
    classificador = KNNClassificador(k=k)
    classificador.treinar(dados_treino)
    
    # Avalia o modelo
    print(f"\nIniciando avaliação do modelo:")
    acuracia, corretas, total = avaliar_modelo(classificador, dados_teste)
    
    # Mostra resultados finais
    print("\n" + "=" * 60)
    print("              RESULTADOS FINAIS")
    print("=" * 60)
    print(f"Total de instâncias de teste: {total}")
    print(f"Predições corretas: {corretas}")
    print(f"Predições incorretas: {total - corretas}")
    print(f"Acurácia: {acuracia:.2f}%")
    
    # Avalia diferentes valores de k
    print(f"\n" + "-" * 60)
    print("COMPARAÇÃO COM DIFERENTES VALORES DE K")
    print("-" * 60)
    
    valores_k = [1, 3, 5, 7, 9]
    melhor_k = k
    melhor_acuracia = acuracia
    
    for k_teste in valores_k:
        if k_teste != k:  # Não testa o k já usado
            classificador_teste = KNNClassificador(k=k_teste)
            classificador_teste.treinar(dados_treino)
            
            # Avalia sem imprimir detalhes
            corretas_teste = 0
            for instancia_teste in dados_teste:
                predicao = classificador_teste.predizer(instancia_teste)
                if predicao == instancia_teste[-1]:
                    corretas_teste += 1
            
            acuracia_teste = (corretas_teste / len(dados_teste)) * 100
            print(f"k={k_teste}: {acuracia_teste:.2f}% de acurácia")
            
            if acuracia_teste > melhor_acuracia:
                melhor_k = k_teste
                melhor_acuracia = acuracia_teste
        else:
            print(f"k={k}: {acuracia:.2f}% de acurácia (usado acima)")
    
    print(f"\nMelhor k encontrado: {melhor_k} com {melhor_acuracia:.2f}% de acurácia")


# Execução principal
if __name__ == '__main__':
    # Define semente para reprodutibilidade dos resultados
    random.seed(42)
    main()
