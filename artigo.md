### Introdução

O problema do Caixeiro Viajante (Travelling Salesman Problem - TSP) é um dos desafios mais estudados na área de otimização combinatória e inteligência artificial. Ele consiste em determinar a rota mais curta para um caixeiro que deve visitar um conjunto de cidades, passando por cada uma delas exatamente uma vez e retornando à cidade de origem. Apesar de sua formulação simples, o TSP pertence à classe de problemas NP-difíceis, o que significa que à medida que o número de cidades cresce, a complexidade do problema aumenta exponencialmente, tornando a busca exaustiva inviável para instâncias maiores.

Dada a natureza complexa do TSP, uma ampla gama de abordagens tem sido proposta para encontrar soluções eficientes. Entre elas, os Algoritmos Genéticos (AGs) destacam-se como uma técnica meta-heurística poderosa, inspirada nos princípios da evolução natural. Esses algoritmos aplicam operadores de seleção, crossover e mutação em uma população de possíveis soluções, buscando evoluir para rotas mais curtas a cada geração. Em vez de garantir a solução exata, os AGs oferecem soluções aproximadas em tempo razoável, o que os torna apropriados para problemas de grande escala, como o TSP.

Neste trabalho, propomos a implementação de um AG para resolver o TSP utilizando como caso de estudo as cidades do estado do Tocantins. A escolha desse problema deve-se à sua aplicabilidade em diversas áreas, como planejamento de rotas de entrega, logística e transporte. O AG é construído com técnicas específicas para garantir diversidade e eficiência, incluindo a seleção por torneio, crossover de ordem (Order Crossover - OX) e mutação baseada na troca de cidades. A solução foi implementada em Python e testada com diferentes configurações genéticas, a fim de validar sua eficácia e analisar a influência dos parâmetros no desempenho do algoritmo.

### Revisão da Literatura

O Problema do Caixeiro Viajante (TSP) é amplamente reconhecido como um dos problemas fundamentais em otimização combinatória, dada sua aplicabilidade em diversas áreas, como roteamento de veículos, planejamento de produção, e otimização de redes. Desde que foi proposto, diversas abordagens exatas e heurísticas têm sido desenvolvidas para resolvê-lo. Métodos exatos, como programação linear inteira e algoritmos de branch and bound, são capazes de resolver instâncias pequenas do TSP de forma ótima, porém tornam-se impraticáveis para instâncias maiores devido ao crescimento exponencial do tempo de execução. Por isso, a utilização de métodos heurísticos e meta-heurísticos tem ganhado destaque, especialmente para grandes instâncias.

Dentre as abordagens meta-heurísticas, os **Algoritmos Genéticos (AGs)** se mostraram altamente promissores para o TSP. **Holland (1975)** introduziu os princípios fundamentais dos AGs, inspirados no processo de seleção natural de Darwin, e desde então, eles têm sido aplicados com sucesso em diversos problemas de otimização, incluindo o TSP. AGs são particularmente eficazes na busca por soluções aproximadas em problemas com grandes espaços de busca, já que mantêm uma população de soluções candidatas que evoluem ao longo do tempo, aplicando operadores de crossover, mutação e seleção.

No contexto do TSP, uma das primeiras aplicações de AGs foi realizada por **Goldberg (1989)**, que demonstrou a viabilidade dessa abordagem para resolver instâncias complexas do problema. Desde então, diversas modificações e aprimoramentos nos AGs foram propostos. Um dos desafios principais no uso de AGs para o TSP é lidar com a codificação de soluções. **Potvin (1996)** propôs o uso de técnicas específicas de crossover, como o **Order Crossover (OX)**, que mantém a ordem relativa das cidades em um caminho e evita duplicações, superando limitações das abordagens de crossover tradicionais.

Além do crossover, a escolha da técnica de seleção é crucial para o desempenho do AG. **Blickle e Thiele (1996)** compararam várias técnicas de seleção, destacando a eficiência da **seleção por torneio**, que garante que indivíduos mais aptos tenham maiores chances de serem selecionados, sem descartar completamente indivíduos menos aptos, permitindo maior diversidade genética. A **mutação** também é uma componente essencial para evitar a convergência prematura em soluções subótimas. Para o TSP, a mutação por troca de cidades tem sido amplamente utilizada, conforme sugerido por **Whitley et al. (1989)**, pois preserva a viabilidade da solução (uma única visita a cada cidade) e melhora a diversidade da população.

Outro aspecto fundamental no desempenho dos AGs aplicados ao TSP é a configuração dos parâmetros genéticos, como o tamanho da população, a taxa de crossover e a taxa de mutação. **Eiben e Smith (2003)** discutem que a escolha adequada desses parâmetros pode influenciar significativamente a convergência do algoritmo e a qualidade das soluções encontradas. Estudos empíricos, como os realizados por **Reeves (1993)**, sugerem que a combinação de uma alta taxa de crossover e uma baixa taxa de mutação tende a produzir bons resultados no TSP, promovendo uma exploração eficiente do espaço de soluções sem perder a diversidade.

Mais recentemente, o uso de AGs foi combinado com outras técnicas, como algoritmos meméticos e estratégias híbridas. **Merz e Freisleben (2000)** introduziram a ideia de combinar AGs com busca local, criando uma abordagem híbrida que aprimora ainda mais a qualidade das soluções para o TSP. Nesse modelo, o AG realiza a busca global, enquanto uma estratégia de busca local é aplicada para refinar as soluções em cada geração. Esses métodos têm demonstrado melhor desempenho em termos de tempo de execução e qualidade das soluções em comparação com AGs tradicionais.

Portanto, a literatura destaca a robustez dos Algoritmos Genéticos para resolver o TSP, especialmente quando técnicas específicas de codificação, crossover e mutação são aplicadas. A combinação de AGs com estratégias híbridas tem se mostrado uma tendência promissora, sugerindo que o campo continua a evoluir, adaptando-se para resolver instâncias cada vez maiores e mais complexas do problema.

Aqui está o código Python do Algoritmo Genético (AG) estruturado de acordo com os pontos que você solicitou, seguindo a organização descrita:

### Desenvolvimento

1. **Codificação (alfabeto genético adotado)**:
    - A solução é codificada como uma permutação das cidades. Cada cromossomo é uma lista de números, onde cada número corresponde a uma cidade, e a sequência indica a ordem em que as cidades serão visitadas.

2. **Cromossomos (quantidade de genes em cada indivíduo)**:
    - O número de genes em cada cromossomo é igual ao número de cidades, pois o cromossomo representa uma rota completa.

3. **Função de Avaliação**:
    - A função de avaliação calcula o custo total da rota (soma das distâncias entre as cidades na sequência dada pelo cromossomo).

4. **Operador de Seleção**:
    - Seleção por torneio: Seleciona o melhor indivíduo entre um grupo aleatório de indivíduos da população.

5. **Operador de Cruzamento (tipo de cruzamento e taxa de cruzamento)**:
    - O crossover utilizado é o **Order Crossover (OX)**, que mantém a ordem relativa das cidades, e a taxa de cruzamento é definida pelo usuário.

6. **Mutação (como ocorre e taxa de mutação)**:
    - A mutação é realizada trocando duas cidades aleatórias dentro de um cromossomo, com uma determinada probabilidade (taxa de mutação).

7. **Substituição**:
    - A nova população substitui completamente a antiga, exceto pelo elitismo, que preserva o melhor indivíduo da geração anterior.

8. **Parâmetros Genéticos**:
    - **Tamanho da população**: Quantidade de cromossomos em cada geração.
    - **Geração da população inicial**: A população inicial é gerada aleatoriamente.
    - **Condição de parada**: O algoritmo para após um número fixo de gerações ou se não houver melhora após várias gerações.

### Explicação dos Componentes

1. **Codificação (alfabeto genético adotado)**:
    - Cada indivíduo (rota) é representado como uma lista de números inteiros, onde cada número corresponde a uma cidade. Exemplo de cromossomo para 5 cidades: `[0, 2, 1, 4, 3]`.

2. **Cromossomos (quantidade de genes em cada indivíduo)**:
    - O número de genes em cada cromossomo é igual ao número de cidades. Se houver 10 cidades, cada cromossomo terá 10 genes.

3. **Função de Avaliação**:
    - A função `calcular_custo_rota` soma as distâncias entre as cidades visitadas na ordem determinada pelo cromossomo, incluindo o retorno à cidade inicial.

4. **Operador de Seleção**:
    - A **seleção por torneio** escolhe o melhor indivíduo entre um grupo aleatório da população, com o tamanho do torneio configurável (neste caso, 3).

5. **Operador de Cruzamento**:
    - O **Order Crossover (OX)** garante que os descendentes mantenham a ordem relativa das cidades dos pais, evitando duplicação de cidades na rota.

6. **Mutação**:
    - A mutação troca a posição de duas cidades em um cromossomo com uma determinada probabilidade, controlada pela `taxa_mutacao`.

7. **Substituição**:
    - A nova geração substitui completamente a antiga, exceto pelo uso do **elitismo**, que mantém a melhor solução encontrada até o momento.

8. **Parâmetros Genéticos**:
    - **Tamanho da população**: Controlado pelo parâmetro `tamanho_populacao`, que determina o número de indivíduos em cada geração.
    - **Geração da população inicial**: Geração aleatória de cromossomos com permutações de cidades.
    - **Condição de parada**: O algoritmo é configurado para rodar por um número fixo de gerações (`num_geracoes`), ou pode ser ajustado para outras condições.
