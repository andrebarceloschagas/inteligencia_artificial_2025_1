from math import radians, sin, cos, sqrt, atan2

# Função para calcular a distância haversine entre duas coordenadas geográficas
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Raio da Terra em km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = R * c
    return distancia

# Exemplo de coordenadas (latitude, longitude) de algumas cidades do Tocantins
cidades_tocantins = {
    "Abreulândia": (-9.621706, -49.151857),
    "Aguiarnópolis": (-6.554518, -47.470219),
    "Aliança do Tocantins": (-12.615416, -48.936239),
    "Almas": (-11.570555, -47.179269),
    "Alvorada": (-12.479089, -49.124234),
    "Ananás": (-6.364780, -48.073499),
    "Angico": (-6.391237, -47.860688),
    "Aparecida do Rio Negro": (-9.941013, -47.963546),
    "Aragominas": (-7.159599, -48.529512),
    "Araguacema": (-8.807660, -49.556344),
    "Araguaçu": (-12.928977, -49.823404),
    "Araguaína": (-7.192377, -48.207447),
    "Araguanã": (-6.582984, -48.639978),
    "Araguatins": (-5.647034, -48.123231),
    "Arapoema": (-7.654337, -49.063655),
    "Arraias": (-12.928929, -46.935980),
    "Augustinópolis": (-5.468320, -47.886425),
    "Aurora do Tocantins": (-12.710110, -46.406151),
    "Axixá do Tocantins": (-5.612392, -47.770089),
    "Babaçulândia": (-7.209032, -47.761289),
    "Bandeirantes do Tocantins": (-7.756140, -48.583949),
    "Barra do Ouro": (-7.695963, -47.677163),
    "Barrolândia": (-9.834052, -48.725146),
    "Bernardo Sayão": (-7.874656, -48.889795),
    "Bom Jesus do Tocantins": (-8.963494, -48.165611),
    "Brasilândia do Tocantins": (-8.389190, -48.482651),
    "Brejinho de Nazaré": (-11.005375, -48.568104),
    "Buriti do Tocantins": (-5.314267, -48.227711),
    "Cachoeirinha": (-6.115864, -47.923084),
    "Campos Lindos": (-7.989340, -46.864664),
    "Cariri do Tocantins": (-11.888027, -49.160470),
    "Carmolândia": (-7.032776, -48.397007),
    "Carrasco Bonito": (-5.314171, -48.031260),
    "Caseara": (-9.276931, -49.952149),
    "Centenário": (-8.961256, -47.330696),
    "Chapada da Natividade": (-11.617587, -47.748690),
    "Chapada de Areia": (-10.141799, -49.140157),
    "Colinas do Tocantins": (-8.059972, -48.475824),
    "Colméia": (-8.724015, -48.763385),
    "Combinado": (-12.791710, -46.538243),
    "Conceição do Tocantins": (-12.220477, -47.295357),
    "Couto Magalhães": (-8.284625, -49.247544),
    "Cristalândia": (-10.598710, -49.194935),
    "Crixás do Tocantins": (-11.099721, -48.915932),
    "Darcinópolis": (-6.715746, -47.759535),
    "Dianópolis": (-11.624511, -46.820806),
    "Divinópolis do Tocantins": (-9.800366, -49.216684),
    "Dois Irmãos do Tocantins": (-9.255972, -49.063563),
    "Dueré": (-11.341741, -49.271942),
    "Esperantina": (-5.365927, -48.537800),
    "Fátima": (-10.760322, -48.907465),
    "Figueirópolis": (-12.131494, -49.174214),
    "Filadélfia": (-7.334745, -47.495554),
    "Formoso do Araguaia": (-11.797467, -49.531340),
    "Fortaleza do Tabocão": (-9.055500, -48.532647),
    "Goianorte": (-8.774424, -48.931599),
    "Goiatins": (-7.709036, -47.325428),
    "Guaraí": (-8.835830, -48.511911),
    "Gurupi": (-11.727500, -49.068611),
    "Ipueiras": (-11.232112, -48.459947),
    "Itacajá": (-8.393220, -47.772347),
    "Itaguatins": (-5.772853, -47.486203),
    "Itapiratins": (-8.379849, -48.107712),
    "Itaporã do Tocantins": (-8.571729, -48.689067),
    "Jaú do Tocantins": (-12.651667, -48.589383),
    "Juarina": (-8.119070, -49.064631),
    "Lagoa da Confusão": (-10.790245, -49.619819),
    "Lagoa do Tocantins": (-9.537679, -47.556868),
    "Lajeado": (-9.748422, -48.356896),
    "Lavandeira": (-12.784722, -46.509367),
    "Lizarda": (-9.590574, -46.673417),
    "Luzinópolis": (-6.177642, -47.858537),
    "Marianópolis do Tocantins": (-9.793528, -49.655538),
    "Mateiros": (-10.546204, -46.416777),
    "Maurilândia do Tocantins": (-5.951676, -47.512694),
    "Miracema do Tocantins": (-9.565176, -48.393937),
    "Miranorte": (-9.530487, -48.592200),
    "Monte do Carmo": (-10.760507, -48.892004),
    "Monte Santo do Tocantins": (-10.007235, -48.994191),
    "Muricilândia": (-7.146520, -48.609653),
    "Natividade": (-11.703944, -47.722004),
    "Nazaré": (-6.374519, -47.664432),
    "Nova Olinda": (-7.631510, -48.425420),
    "Nova Rosalândia": (-10.565685, -48.912460),
    "Novo Acordo": (-9.970336, -47.679594),
    "Novo Alegre": (-12.921476, -46.571034),
    "Novo Jardim": (-11.826952, -46.632611),
    "Oliveira de Fátima": (-10.707302, -48.908436),
    "Palmas": (-10.183056, -48.333611),
    "Palmeirante": (-7.864645, -47.924676),
    "Palmeiras do Tocantins": (-6.616998, -47.546558),
    "Palmeirópolis": (-13.044247, -48.402673),
    "Paraíso do Tocantins": (-10.175180, -48.882905),
    "Paranã": (-12.616226, -47.873462),
    "Pau d'Arco": (-7.539038, -49.367163),
    "Pedro Afonso": (-8.968982, -48.171681),
    "Peixe": (-12.024992, -48.539925),
    "Pequizeiro": (-8.593998, -48.932799),
    "Pindorama do Tocantins": (-11.131680, -47.572706),
    "Piraquê": (-6.768675, -48.295416),
    "Pium": (-10.442619, -49.187102),
    "Ponte Alta do Bom Jesus": (-12.085147, -46.482242),
    "Ponte Alta do Tocantins": (-10.748860, -47.527803),
    "Porto Alegre do Tocantins": (-11.618278, -48.410390),
    "Porto Nacional": (-10.347283, -48.389901),
    "Praia Norte": (-5.811677, -47.404946),
    "Presidente Kennedy": (-10.559919, -48.194416),
    "Rio da Conceição": (-10.677510, -48.679336),
    "Rio dos Bois": (-12.552590, -48.966230),
    "Rio do Sono": (-9.887747, -48.284353),
    "Sampaio": (-10.033177, -48.540221),
    "Sandolândia": (-12.150330, -46.572670),
    "Santa Fé do Araguaia": (-6.080363, -48.114867),
    "Santa Maria do Tocantins": (-12.373830, -47.728390),
    "Santa Rita do Tocantins": (-10.682215, -48.339340),
    "Santa Rosa do Tocantins": (-11.049490, -48.192100),
    "Santo Antônio do Descoberto": (-8.660336, -48.671104),
    "Santo Antônio do Tocantins": (-10.916478, -48.658131),
    "São Bento do Tocantins": (-12.013988, -46.759999),
    "São Félix do Tocantins": (-10.062622, -48.350785),
    "São José do Tocantins": (-10.592724, -48.060322),
    "São Salvador do Tocantins": (-12.376932, -46.817706),
    "São Sebastião do Tocantins": (-12.254453, -47.199243),
    "Sítio Novo do Tocantins": (-9.556434, -48.930034),
    "Tanhaçu": (-12.746222, -46.659926),
    "Tocantínia": (-9.781793, -48.697198),
    "Tocantinópolis": (-5.490920, -47.357514),
    "Wanderlândia": (-7.182363, -48.194870),
    "Wanderlândia do Tocantins": (-7.490852, -48.158794),
    "Xambioá": (-7.075598, -48.550448),
    "Xerente": (-10.938014, -47.454024),
    "Xingu do Tocantins": (-9.947090, -49.407293)
}

# Criar matriz de distâncias
def gerar_matriz_distancias(cidades):
    num_cidades = len(cidades)
    matriz_distancias = [[0.0] * num_cidades for _ in range(num_cidades)]
    nomes_cidades = list(cidades.keys())
    
    for i in range(num_cidades):
        for j in range(i, num_cidades):
            if i == j:
                matriz_distancias[i][j] = 0.0  # Distância da cidade para ela mesma é 0
            else:
                lat1, lon1 = cidades[nomes_cidades[i]]
                lat2, lon2 = cidades[nomes_cidades[j]]
                distancia = round(haversine(lat1, lon1, lat2, lon2), 2)  # Arredondar para 2 casas decimais
                matriz_distancias[i][j] = distancia
                matriz_distancias[j][i] = distancia  # Simetria na matriz
            
    return matriz_distancias, nomes_cidades
            
# Gerar a matriz de distâncias
matriz_distancias, nomes_cidades = gerar_matriz_distancias(cidades_tocantins)

# Exibir a matriz de distâncias
for i, cidade in enumerate(nomes_cidades):
    distancias_formatadas = [f"{dist:.2f}" for dist in matriz_distancias[i]]  # Formatar para 2 casas decimais
    print(f"{cidade}: {distancias_formatadas}")
