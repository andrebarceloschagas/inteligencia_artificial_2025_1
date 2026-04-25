<h1 align="center">🧠 Inteligência Artificial 2025.1</h1>

<p align="center">
  Implementações práticas e educacionais de algoritmos fundamentais de<br>
  <b>Inteligência Artificial</b> e <b>Machine Learning</b>, desenvolvidas<br>
  ao longo da disciplina de IA na Universidade Federal do Tocantins.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-3776AB?style=flat&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/tkinter-GUI-FFD43B?style=flat&logo=python&logoColor=black" />
  <img src="https://img.shields.io/badge/algoritmo-BFS-4B8BBE?style=flat" />
  <img src="https://img.shields.io/badge/algoritmo-KNN-FF6F61?style=flat" />
  <img src="https://img.shields.io/badge/dataset-Iris-2E8B57?style=flat" />
  <img src="https://img.shields.io/badge/dataset-Mushroom-8B4513?style=flat" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
</p>

<p align="center">
  <a href="#-demo">Demo</a> •
  <a href="#-projetos">Projetos</a> •
  <a href="#-tecnologias">Tecnologias</a> •
  <a href="#-como-rodar">Como rodar</a> •
  <a href="#-resultados">Resultados</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## 📚 Sobre

Este repositório reúne os trabalhos práticos da disciplina **Inteligência Artificial 2025.1**, com foco em compreender e implementar **do zero** algoritmos clássicos de busca e classificação — sem depender de bibliotecas como Scikit-learn — para entender de fato o que acontece "por baixo do capô".

| Item | Detalhe |
|---|---|
| 🎓 Instituição | CCOMP / UFT |
| 📅 Semestre | 2025.1 |
| 👩‍🏫 Professora | Glenda Botelho |
| 👥 Integrantes | Antonio André, Helorrayne Cristine, Sophia Prado |

---

## 🎬 Demo

> 💡 Substitua a imagem abaixo por um GIF mostrando a execução da Busca em Largura no mapa da Romênia (use [ScreenToGif](https://www.screentogif.com/) ou [Kap](https://getkap.co/)).

<p align="center">
  <img src="busca_largura/Captura%20de%20tela%202025-05-02%20214539.png" alt="Busca em Largura no mapa da Romênia" width="720" />
</p>

---

## 🚀 Projetos

### 🔎 1. Busca em Largura (BFS) — Mapa da Romênia

Implementação visual do algoritmo **Breadth-First Search** para encontrar o caminho mais curto (em número de passos) entre duas cidades no clássico mapa da Romênia, com interface gráfica em **Tkinter**.

- 📁 [`busca_largura/`](./busca_largura)
- 💻 [`busca_largura.py`](./busca_largura/busca_largura.py)
- 🖼️ [Captura de tela](./busca_largura/Captura%20de%20tela%202025-05-02%20214539.png)

**Destaques técnicos**
- Representação do grafo como dicionário de adjacências
- Visualização interativa do grafo e do caminho encontrado
- Animação passo a passo da expansão dos nós
- Interface gráfica feita do zero com Tkinter

---

### 🌸 2. KNN — Dataset Iris

Classificação de espécies de flores íris (*setosa*, *versicolor*, *virginica*) a partir de 4 medidas morfológicas, usando o algoritmo **K-Nearest Neighbors** implementado do zero.

- 📁 [`knn/iris/`](./knn/iris)
- 💻 Código: `knn/iris/iris.py`
- 📊 Dataset: `knn/iris/iris.csv` (150 amostras × 4 atributos × 3 classes)

**Destaques técnicos**
- Classe `KNNClassificador` orientada a objetos
- Distância euclidiana implementada manualmente
- Divisão automática treino/teste (80/20) com embaralhamento
- Comparação de múltiplos valores de `k` ([1, 3, 5, 7, 9])
- Acurácia típica: **~96.67%** com k=3

---

### 🍄 3. KNN — Dataset Mushroom (Venenoso vs. Comestível)

Classificação binária de **8.124 cogumelos** como venenosos (`p`) ou comestíveis (`e`) a partir de 22 características categóricas, com **codificação one-hot** implementada manualmente.

- 📁 [`knn/mushroom/`](./knn/mushroom)
- 💻 Código: `knn/mushroom/mushroom.py`
- 📊 Dataset: `knn/mushroom/mushrooms.csv` (8.124 amostras × 22 atributos categóricos)
- 📄 [Apresentação do Seminário 2](./knn/seminario_2.pdf)

**Destaques técnicos**
- Codificação **one-hot** do zero (22 atributos → 95+ dimensões)
- Limpeza, validação e reorganização do dataset
- Tratamento de variáveis categóricas com distância euclidiana
- Comparação de valores de `k` ([1, 3, 5, 7, 9, 11])
- Acurácia típica: **~100%** com k=5

> ⚠️ **Aviso**: este é um projeto educacional. **Nunca** use o modelo para decidir se um cogumelo selvagem é seguro para consumo — consulte sempre um especialista em micologia.

---

## 🛠️ Tecnologias

| Camada | Stack |
|---|---|
| **Linguagem** | Python 3.10+ |
| **Interface gráfica** | Tkinter |
| **Manipulação de dados** | `csv`, `math`, `random` (biblioteca padrão) |
| **Algoritmos** | BFS, KNN (do zero, sem Scikit-learn) |
| **Documentação** | Markdown + PDFs de apresentação |

---

## 🏗️ Estrutura do projeto

inteligencia_artificial_2025_1/
├── busca_largura/
│   ├── busca_largura.py
│   └── Captura de tela 2025-05-02 214539.png
├── knn/
│   ├── iris/
│   │   ├── iris.py
│   │   ├── iris.csv
│   │   └── README.md
│   ├── mushroom/
│   │   ├── mushroom.py
│   │   ├── mushrooms.csv
│   │   └── README.md
│   └── seminario_2.pdf
├── .gitignore
└── README.md

---

## 🚀 Como rodar

### Pré-requisitos
- Python 3.10+
- (recomendado) virtualenv

### Setup

```bash
# 1. Clone o repositório
git clone https://github.com/andrebarceloschagas/inteligencia_artificial_2025_1.git
cd inteligencia_artificial_2025_1

# 2. (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### Executando cada projeto

```bash
# 🔎 Busca em Largura (interface Tkinter)
python busca_largura/busca_largura.py

# 🌸 KNN - Iris
cd knn/iris
python iris.py

# 🍄 KNN - Mushroom
cd knn/mushroom
python mushroom.py
```

> Não há dependências externas: tudo usa apenas a biblioteca padrão do Python.

---

## 📊 Resultados

| Projeto | Algoritmo | Dataset | Melhor `k` | Acurácia |
|---|---|---|---|---|
| Mapa da Romênia | BFS | Grafo da Romênia | — | Caminho ótimo encontrado |
| KNN — Iris | KNN | 150 amostras | 3 | ~96.67% |
| KNN — Mushroom | KNN + One-Hot | 8.124 amostras | 5 | ~100% |

---

## 🗺️ Roadmap

- [x] Busca em Largura com visualização Tkinter
- [x] KNN no dataset Iris (do zero)
- [x] KNN no dataset Mushroom com one-hot encoding
- [ ] Validação cruzada (k-fold)
- [ ] Outras métricas de distância (Manhattan, Minkowski, Hamming, Jaccard)
- [ ] Normalização e padronização dos atributos numéricos
- [ ] Visualização das fronteiras de decisão (matplotlib)
- [ ] Comparação com `scikit-learn` como baseline
- [ ] Versão web interativa (Streamlit)

---

## 👥 Integrantes

| Nome | GitHub |
|---|---|
| Antonio André Barcelos Chagas | [@andrebarceloschagas](https://github.com/andrebarceloschagas) |
| Helorrayne Cristine | — |
| Sophia Prado | — |

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](LICENSE) para mais detalhes.

---

<p align="center">
  Feito com 🧠 e ☕ por <a href="https://github.com/andrebarceloschagas">Antonio André</a> — UFT 2025.1
</p>
