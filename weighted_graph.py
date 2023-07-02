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
        with open(file_name, 'r') as file:
            content = json.load(file)
        return content

    def write_in_file(self, file_name, infos):
        with open(file_name, 'w') as file:
            for info in infos:
                file.write(str(info) + '\n')

    def __str__(self):
        output = ""
        for node in self.adj_list:
            output += str(node) + " -> "
            neighbors = self.adj_list[node]
            for neighbor, weight in neighbors.items():
                output += f"{neighbor} {weight}, "
            output = output.rstrip(", ") + "\n"
        return output
'''        
    def read_file(self, file_name):
        with open(file_name, 'r') as file: #garante que o arquivo abra e seja fechado corretamente
            i = 0
            for line in file:   
                i += 1
                if i == 1:
                    continue
            content = line.strip().split(" ")
            u = content[0]
            v = content[1]
            w = int(content[2])
            self.add_edge(u, v, w)
'''
