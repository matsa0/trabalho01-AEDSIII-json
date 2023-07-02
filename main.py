""" import requests"""
import json
from weighted_graph import WeightedGraph

g = WeightedGraph()

file_name = input("Informe o arquivo de votações > ")
print("Processando...")

#1 - Leitura do json
with open(file_name, 'r', encoding='utf-8') as file:
    content = json.load(file)

#2 - Adicionando arestas e peso(relação de proximidade)
votes = {}
for item in content['dados']:
    name = item['deputado_']['nome']
    vote_id = item['idVotacao']
    vote = item['voto']
    g.add_node(name)

    for key, value in votes.items():
        if value['idVotacao'] == vote_id and value['voto'] == vote:
            if g.there_is_edge(name, key):
                g.increment_edge_weight(name, key)
            else:
                g.add_edge(name, key, 1)

    votes[name] = {'idVotacao': vote_id, 'voto': vote}

#3 - Escrevendo no arquivo "deputados.txt" 
with open("deputados.txt", 'w', encoding='utf-8') as file:
    file.write(f"{g.node_count} {g.edge_count}\n")
    for node1 in g.adj_list:
        for node2, weight in g.adj_list[node1].items():
            file.write(f"{node1} {node2} {weight}\n")

#4 - Verificando quantas votações cada nó paricipou
votes_per_node = {}
for item in content['dados']:
    name = item['deputado_']['nome']
    if name not in votes_per_node:
        votes_per_node[name] = 0
    votes_per_node[name] += 1

#5 - Escrevendo no arquivo votos.txt
with open("votos.txt", 'w', encoding='utf-8') as file:
    for node in g.adj_list:
        votes = votes_per_node.get(node, 0)
        file.write(f"{node} {votes}\n")

print("O Grafo foi escrito nos arquivos: ")
print("\t-deputados.txt\n\t-votos.txt")


""" url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
resp = requests.get(url).json()

with open("deputados.txt", 'w') as file:
    for dept in resp['dados']:
        data = f"{dept['nome']} {dept['id']}\n"
        file.write(data) """

