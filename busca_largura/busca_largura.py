from collections import deque
import tkinter as tk
from tkinter import ttk, messagebox

# Definindo o grafo com cidades e conexões (ignora custos neste caso)
graph = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

# Função que implementa a Busca em Largura (BFS)
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        city = path[-1]

        if city == goal:
            return path, visited

        if city not in visited:
            visited.add(city)

            for neighbor in graph[city]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None, visited

# Coordenadas das cidades no mapa
city_coords = {
    'Arad': (92, 198),
    'Bucharest': (723, 546),
    'Craiova': (422, 629),
    'Dobreta': (244, 605),
    'Eforie': (1053, 620),
    'Fagaras': (533, 285),
    'Giurgiu': (671, 666),
    'Hirsova': (996, 498),
    'Iasi': (873, 167),
    'Lugoj': (244, 436),
    'Mehadia': (250, 522),
    'Neamt': (737, 102),
    'Oradea': (175, 29),
    'Pitesti': (561, 462),
    'Rimnicu Vilcea': (382, 370),
    'Sibiu': (329, 269),
    'Timisoara': (97, 372),
    'Urziceni': (838, 498),
    'Vaslui': (945, 297),
    'Zerind': (127, 113)
}

# Função para buscar o caminho e desenhar o mapa
def buscar_caminho():
    start_city = origem_var.get()
    goal_city = destino_var.get()
    if start_city == goal_city:
        messagebox.showinfo("Resultado", "A cidade de origem e destino são iguais.")
        desenhar_mapa([], set())
        return

    path, visited = bfs(graph, start_city, goal_city)

    if path:
        resultado = f"Caminho encontrado de {start_city} para {goal_city}: {' -> '.join(path)}"
        desenhar_mapa(path, visited)
    else:
        resultado = f"Não foi possível encontrar um caminho de {start_city} para {goal_city}"
        desenhar_mapa([], visited)
    resultado_var.set(resultado)

# Função para desenhar o mapa com o caminho encontrado
def desenhar_mapa(path, visited):
    canvas.delete("all")

    for cidade, vizinhos in graph.items():
        x1, y1 = city_coords[cidade]
        for vizinho in vizinhos:
            x2, y2 = city_coords[vizinho]
            canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)

    if path and len(path) > 1:
        for i in range(len(path)-1):
            x1, y1 = city_coords[path[i]]
            x2, y2 = city_coords[path[i+1]]
            canvas.create_line(x1, y1, x2, y2, fill="red", width=4)

    for cidade, (x, y) in city_coords.items():
        if path and cidade in path:
            cor = "red"
        elif cidade in visited: 
            cor = "orange" 
        else:
            cor = "blue"

        canvas.create_oval(x-7, y-7, x+7, y+7, fill=cor)
        canvas.create_text(x, y-15, text=cidade, font=("Arial", 12), fill="black")

# Interface gráfica
root = tk.Tk()
root.title("Busca em Largura - BFS")

cidades = list(graph.keys())

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky="nw")

ttk.Label(frame, text="Cidade de Origem:").grid(column=0, row=0, sticky=tk.W)
origem_var = tk.StringVar(value=cidades[0])
origem_menu = ttk.Combobox(frame, textvariable=origem_var, values=cidades, state="readonly")
origem_menu.grid(column=1, row=0)

ttk.Label(frame, text="Cidade de Destino:").grid(column=0, row=1, sticky=tk.W)
destino_var = tk.StringVar(value=cidades[1])
destino_menu = ttk.Combobox(frame, textvariable=destino_var, values=cidades, state="readonly")
destino_menu.grid(column=1, row=1)

buscar_btn = ttk.Button(frame, text="Buscar Caminho", command=buscar_caminho)
buscar_btn.grid(column=0, row=2, columnspan=2, pady=12)

resultado_var = tk.StringVar()
resultado_label = ttk.Label(frame, textvariable=resultado_var, wraplength=400)
resultado_label.grid(column=0, row=3, columnspan=2, pady=12)

canvas = tk.Canvas(root, width=1087, height=682, bg="white")
canvas.grid(row=0, column=1, padx=10, pady=12)

# Desenhar o mapa inicial
desenhar_mapa([], set())

root.mainloop()
