# Classificador KNN para Dataset Iris

Este projeto implementa o algoritmo K-Nearest Neighbors (K-Vizinhos Mais Próximos) para classificação do famoso dataset Iris em Python.

## Descrição

O algoritmo KNN é um método de classificação não-paramétrico que classifica novos pontos de dados baseado na classe mais comum entre os k vizinhos mais próximos no espaço de características.

### Dataset Iris

O dataset Iris contém 150 amostras de flores íris com 4 características:
- **sepal_length**: Comprimento da sépala (cm)
- **sepal_width**: Largura da sépala (cm) 
- **petal_length**: Comprimento da pétala (cm)
- **petal_width**: Largura da pétala (cm)

E 3 classes de espécies:
- **setosa**
- **versicolor** 
- **virginica**

## Arquivos

- `iris.py`: Código principal com a implementação do classificador KNN
- `iris.csv`: Dataset Iris com os dados de treinamento e teste
- `README.md`: Este arquivo de documentação

## Como Executar

1. Certifique-se de ter Python 3 instalado no sistema
2. Navegue até o diretório do projeto:
   ```bash
   cd /caminho/para/knn/iris
   ```
3. Execute o programa:
   ```bash
   python3 iris.py
   ```

## Funcionalidades

### Classe KNNClassificador

- **`__init__(k=3)`**: Inicializa o classificador com o número de vizinhos
- **`distancia_euclidiana(ponto1, ponto2)`**: Calcula a distância euclidiana entre dois pontos
- **`obter_vizinhos(instancia_teste)`**: Encontra os k vizinhos mais próximos
- **`predizer_classificacao(vizinhos)`**: Prediz a classe baseada na votação majoritária
- **`treinar(dados_treino)`**: Treina o modelo com os dados de treino
- **`predizer(instancia_teste)`**: Faz predição para uma nova instância

### Funções Auxiliares

- **`carregar_dataset_iris(nome_arquivo)`**: Carrega o dataset do arquivo CSV
- **`dividir_dataset(dataset, proporcao_treino, embaralhar)`**: Divide dados em treino/teste
- **`avaliar_modelo(classificador, dados_teste)`**: Avalia performance do modelo

## Exemplo de Saída

```
============================================================
    CLASSIFICADOR KNN - DATASET IRIS
============================================================
Carregando dataset do arquivo: iris.csv
Dataset carregado com sucesso! Total de amostras: 150
Classes encontradas:
  - setosa: 50 amostras
  - versicolor: 50 amostras
  - virginica: 50 amostras

Dividindo dataset: 80% treino, 20% teste
Conjunto de treino: 120 amostras
Conjunto de teste: 30 amostras

Avaliando modelo com k=3...
Teste  1: Esperado: virginica    | Predito: virginica    ✓
...

============================================================
              RESULTADOS FINAIS
============================================================
Total de instâncias de teste: 30
Predições corretas: 29
Predições incorretas: 1
Acurácia: 96.67%
```

## Características do Código

- **Orientado a objetos**: Implementação limpa usando classes
- **Documentação completa**: Todas as funções possuem docstrings explicativas
- **Tratamento de erros**: Verificação robusta de arquivos e dados
- **Avaliação automática**: Testa diferentes valores de k automaticamente
- **Interface amigável**: Saída formatada e fácil de entender
- **Reprodutibilidade**: Uso de semente aleatória para resultados consistentes

## Parâmetros Configuráveis

No arquivo `iris.py`, você pode modificar:

- **k**: Número de vizinhos (padrão: 3)
- **proporcao_treino**: Proporção de dados para treino (padrão: 0.8)
- **valores_k**: Lista de valores k para comparação (padrão: [1, 3, 5, 7, 9])

## Requisitos

- Python 3.x
- Bibliotecas padrão: `csv`, `math`, `random`

## Melhorias Futuras

- Validação cruzada k-fold
- Diferentes métricas de distância (Manhattan, Minkowski)
- Normalização/padronização dos dados
- Visualização dos resultados
- Interface gráfica
