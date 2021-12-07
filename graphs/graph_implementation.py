"""
Graphs are data structures which contain nodes or vertices,
which are connected to each other through edges.
Tress and Linked Lists are basically graphs having nodes and connections between the nodes.

Now, graphs are primarily classified by three properties -
    - Cyclic/Acyclic,
    - Weighted/Unweighted/,
    - Directed/Undirected Graphs

There are many applications of graphs and many operations can be performed on them.
A graph can be represented in 3 ways -
    - Adjacency List,
    - Adjacency Matrix,
    - Edge List.

Adjacency list stores the nodes with which a particular node is connected to in a linked list or array.
All these lists or arrays can be stored in a hash table
with the keys being the nodes and the values being their respective lists

Adjacency matrix is a nXn matrix where n is the number of nodes.
M[i][j] = 1 if nodes i and j are connected otherwise 0

Edge list contains all the pairs of nodes which are connected,
and if the graph is weighted, then the weight of each edge as well

Here we will build an undirected graph using an adjacency list.
"""


class Graph:
    """
    Undirected graph
    """
    def __init__(self):
        """
        The constructor will initialize the number of vertices in the graph to zero and
        the adjacency list to an empty dictionary
        """
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def __str__(self):
        """
        For print graph in string view containing class variables
        :return:
        """
        return str(self.__dict__)

    def add_vertex(self, node):
        """
        Insert node method.
        Add the value of the node as a key in the adjacency list and
        initialize the value of the key to be an empty array
        :param node:
        :return:
        """
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        """
        Insert edge method where we will specify two nodes between which an edge is to be added.
        First check if an edge already exists
        by checking the adjacency list of either of the two nodes.
        If the other node is present it means the edge already exists,
        if not then the edge doesn't exist.
        So add the edge by adding the complimentary node in the adjacency list of either node
        :param node1:
        :param node2:
        :return:
        """
        if node2 not in self.adjacent_list[node1]:
            self.adjacent_list[node1].append(node2)
            self.adjacent_list[node2].append(node1)
            return
        return "Edge already exists"

    def show_connections(self):
        """
        Custom print method which will print the nodes and their connections
        :return:
        """
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            connections = ""
            print(f"{node} --> {' '.join(node_connections)}")


if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_vertex('0')
    my_graph.add_vertex('1')
    my_graph.add_vertex('2')
    my_graph.add_vertex('3')
    my_graph.add_vertex('4')
    my_graph.add_vertex('5')
    my_graph.add_vertex('6')

    my_graph.add_edge('3', '1')
    my_graph.add_edge('3', '4')
    my_graph.add_edge('4', '2')
    my_graph.add_edge('4', '5')
    my_graph.add_edge('1', '2')
    my_graph.add_edge('1', '0')
    my_graph.add_edge('0', '2')
    my_graph.add_edge('6', '5')

    my_graph.show_connections()
    print(my_graph)