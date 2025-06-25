# Classificador KNN para Dataset de Cogumelos

Este projeto implementa o algoritmo K-Nearest Neighbors (K-Vizinhos Mais Próximos) para classificação de cogumelos como **venenosos** ou **comestíveis** usando Python.

## Descrição

O algoritmo KNN é aplicado ao famoso dataset de cogumelos, que contém características categóricas. O projeto utiliza **codificação one-hot** para converter variáveis categóricas em numéricas, permitindo o uso da distância euclidiana.

### Dataset de Cogumelos

O dataset contém informações sobre **8.124 amostras** de cogumelos com **22 características categóricas**:

#### Características Analisadas:
1. **cap-diameter**: Diâmetro do chapéu
2. **cap-shape**: Formato do chapéu  
3. **cap-surface**: Superfície do chapéu
4. **cap-color**: Cor do chapéu
5. **does-bruise-or-bleed**: Se machuca ou sangra
6. **gill-attachment**: Fixação das lamelas
7. **gill-spacing**: Espaçamento das lamelas
8. **gill-color**: Cor das lamelas
9. **stem-height**: Altura do caule
10. **stem-width**: Largura do caule
11. **stem-root**: Raiz do caule
12. **stem-surface**: Superfície do caule
13. **stem-color**: Cor do caule
14. **veil-type**: Tipo de véu
15. **veil-color**: Cor do véu
16. **has-ring**: Tem anel
17. **ring-type**: Tipo de anel
18. **spore-print-color**: Cor da impressão dos esporos
19. **habitat**: Habitat
20. **season**: Estação do ano

#### Classes:
- **p** (poisonous): Venenoso 🍄☠️
- **e** (edible): Comestível 🍄✅

## Arquivos

- `mushroom.py`: Código principal com a implementação do classificador KNN
- `mushrooms.csv`: Dataset de cogumelos com dados de treinamento e teste
- `README.md`: Este arquivo de documentação

## Como Executar

1. Certifique-se de ter Python 3 instalado no sistema
2. Navegue até o diretório do projeto:
   ```bash
   cd /caminho/para/knn/mushroom
   ```
3. Execute o programa:
   ```bash
   python3 mushroom.py
   ```

## Funcionalidades

### Classe KNNClassificadorCogumelos

- **`__init__(k=5)`**: Inicializa o classificador com o número de vizinhos
- **`distancia_euclidiana(ponto1, ponto2)`**: Calcula a distância euclidiana entre dois pontos
- **`obter_vizinhos(instancia_teste)`**: Encontra os k vizinhos mais próximos
- **`predizer_classificacao(vizinhos)`**: Prediz a classe baseada na votação majoritária
- **`codificar_one_hot(dataset, cabecalho)`**: Aplica codificação one-hot para variáveis categóricas
- **`treinar(dados_treino)`**: Treina o modelo com os dados de treino
- **`predizer(instancia_teste)`**: Faz predição para uma nova instância

### Funções Auxiliares

- **`carregar_dataset_cogumelos(nome_arquivo)`**: Carrega o dataset do arquivo CSV
- **`processar_dataset_cogumelos(dataset, cabecalho)`**: Processa e reorganiza o dataset
- **`dividir_dataset(dataset, proporcao_treino, embaralhar)`**: Divide dados em treino/teste
- **`avaliar_modelo(classificador, dados_teste)`**: Avalia performance do modelo

## Exemplo de Saída

```
================================================================================
    CLASSIFICADOR KNN - DATASET DE COGUMELOS
    (Venenosos vs Comestíveis)
================================================================================
Carregando dataset do arquivo: mushrooms.csv
Dataset carregado com sucesso! Total de amostras: 8124
Classes encontradas:
  - Venenoso (p): 3916 amostras
  - Comestível (e): 4208 amostras

Aplicando codificação one-hot para variáveis categóricas...
Dimensões: 22 características originais → 95 após one-hot encoding

Dividindo dataset: 80% treino, 20% teste
Conjunto de treino: 6499 amostras
Conjunto de teste: 1625 amostras

Avaliando modelo com k=5...
Teste   1: Esperado: Venenoso   | Predito: Venenoso   ✓
Teste   2: Esperado: Comestível | Predito: Comestível ✓
...

================================================================================
                    RESULTADOS FINAIS
================================================================================
Total de instâncias de teste: 1625
Predições corretas: 1625
Predições incorretas: 0
Acurácia: 100.00%
🎯 Excelente! O modelo tem performance muito alta.
```

## Características Técnicas

### Codificação One-Hot
- **Problema**: Variáveis categóricas não podem ser usadas diretamente com distância euclidiana
- **Solução**: Cada valor categórico é convertido em um vetor binário
- **Exemplo**: "cap-color: red" → [0, 0, 1, 0, 0] (se há 5 cores possíveis)

### Processamento de Dados
- **Limpeza**: Remove espaços em branco e linhas incompletas
- **Reorganização**: Move coluna alvo para o final para consistência
- **Validação**: Verifica integridade dos dados durante carregamento

### Avaliação
- **Divisão**: 80% treino, 20% teste (com embaralhamento)
- **Métricas**: Acurácia, número de predições corretas/incorretas
- **Comparação**: Testa diferentes valores de k automaticamente

## Características do Código

- **Orientado a objetos**: Implementação limpa usando classes
- **Documentação completa**: Todas as funções possuem docstrings explicativas
- **Tratamento robusto**: Verificação de erros e validação de dados
- **Interface intuitiva**: Saída formatada e emojis para interpretação
- **Reprodutibilidade**: Uso de semente aleatória para resultados consistentes
- **Escalabilidade**: Suporta datasets de diferentes tamanhos

## Parâmetros Configuráveis

No arquivo `mushroom.py`, você pode modificar:

- **k**: Número de vizinhos (padrão: 5)
- **proporcao_treino**: Proporção de dados para treino (padrão: 0.8)
- **valores_k**: Lista de valores k para comparação (padrão: [1, 3, 5, 7, 9, 11])

## Desafios Únicos deste Dataset

1. **Alta dimensionalidade**: 22 características → 95+ após one-hot encoding
2. **Variáveis categóricas**: Todas as características são categóricas
3. **Desequilíbrio leve**: Proporção quase igual entre classes
4. **Importância crítica**: Erro pode ser fatal (cogumelo venenoso)

## Requisitos

- Python 3.x
- Bibliotecas padrão: `csv`, `math`, `random`

## Performance Esperada

- **Acurácia típica**: 95-100%
- **Tempo de execução**: < 30 segundos (dataset completo)
- **Melhor k**: Geralmente entre 3-7

## Melhorias Futuras

- Implementação de outras métricas de distância (Hamming, Jaccard)
- Validação cruzada k-fold
- Análise de importância das características
- Otimização para grandes datasets
- Interface web para classificação interativa
- Visualização das características mais importantes

## Considerações de Segurança

⚠️ **IMPORTANTE**: Este é um projeto educacional. Nunca use este modelo para decisões reais sobre consumo de cogumelos. Sempre consulte especialistas em micologia para identificação segura de cogumelos selvagens.
