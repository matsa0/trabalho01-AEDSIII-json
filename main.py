""" import requests"""
from weighted_graph import WeightedGraph

g = WeightedGraph()

file_name = input("Informe o arquivo de votações > ")
print("Processando...")

#1 - Leitura do json
content = g.read_json_file(file_name)

#2 - Adicionando arestas e peso(relação de proximidade)
g.add_votes_edge(content)

#3 - Escrevendo no arquivo "deputados.txt" 
g.file_write_graph("deputados.txt")

#4 - Verificando quantas votações cada nó paricipou
votes_per_node = g.verify_votes(content)

#5 - Escrevendo no arquivo votos.txt
g.file_write_votes("votos.txt", votes_per_node)

print("O Grafo foi escrito nos arquivos: ")
print("\t-deputados.txt\n\t-votos.txt")




""" url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
resp = requests.get(url).json()

with open("deputados.txt", 'w') as file:
    for dept in resp['dados']:
        data = f"{dept['nome']} {dept['id']}\n"
        file.write(data) """

