import json
class WeightedGraph:

    def __init__(self):
        self.adj_list = {}
        self.node_count = 0
        self.edge_count = 0

    def add_node(self, node):
        if node in self.adj_list:
            #print(f"WARN! The node {node} is already in the graph!")
            return
        self.adj_list[node] = {} 
        self.node_count += 1

    def add_edge(self, node1, node2, weight):
        if node1 not in self.adj_list:
            self.add_node(node1)
        if node2 not in self.adj_list:
            self.add_node(node2)
        self.adj_list[node1][node2] = weight
        self.edge_count += 1
    
    def there_is_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list[node1]:
            return True
        return False

    def increment_edge_weight(self, node1, node2):
        if self.there_is_edge(node1, node2):
            self.adj_list[node1][node2] += 1

    def add_two_way_edge(self, node1, node2, weight):
        self.add_edge(node1, node2, weight)
        self.add_edge(node2, node1, weight)

    def remove_edge(self, node1, node2):
        if node2 not in self.adj_list[node1]:
            print(f"WARN! There's no edge between {node1} and {node2}")
            return
        self.adj_list[node1].pop(node2)
        self.edge_count -= 1
    
    def read_json_file(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            content = json.load(file)
        return content

    def add_votes_edge(self, content):
        votes = {}
        for item in content['dados']:
            name = item['deputado_']['nome']
            vote_id = item['idVotacao']
            vote = item['voto']
            self.add_node(name)
    
            for key, value in votes.items():
                if value['idVotacao'] == vote_id and value['voto'] == vote:
                    if self.there_is_edge(name, key):
                        self.increment_edge_weight(name, key)
                    else:
                        self.add_edge(name, key, 1)
    
            votes[name] = {'idVotacao': vote_id, 'voto': vote}

    def file_write(self, file_name, content):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
    
    def file_write_graph(self, file_name):
        content = f"{self.node_count} {self.edge_count}\n"
        for node in self.adj_list:
            for node2, weight in self.adj_list[node].items():
                content += f"{node} {node2} {weight}\n"
        self.file_write(file_name, content)

        
    def verify_votes(self, content):
        votes_per_node = {}
        for item in content['dados']:
            name = item['deputado_']['nome']
            if name not in votes_per_node:
                votes_per_node[name] = 0
            votes_per_node[name] += 1
        return votes_per_node

    def file_write_votes(self, file_name, votes_per_node):
        content = ""
        for node in self.adj_list:
            votes = votes_per_node.get(node, 0)
            content += f"{node} {votes}\n"
        self.file_write(file_name, content)

    def __str__(self):
        output = ""
        for node in self.adj_list:
            output += str(node) + " -> "
            neighbors = self.adj_list[node]
            for neighbor, weight in neighbors.items():
                output += f"{neighbor} {weight}, "
            output = output.rstrip(", ") + "\n"
        return output

