# not object oriented!!

class Node:
    def __init__(self, code: str) -> None:
        self.code = code
        
class DAG:
    def __init__(self) -> None:
         self.nodes = []
         self.arcs = []


    def incomming_arcs(self, v: Node):
        # Discuss performance

        inarcs = []
        for a in self.arcs:
            if (a.to_node == v):
                inarcs.append(a)
        return inarcs

    def SP(self, s : Node, v: Node) -> int:
        # Discuss performance

        min = None
        for a in self.incomming_arcs(v):
            length = a.distance + self.SP(s, a.from_node)
            if (min is None or length < min):
                min = length

        if (min is None):
            return 0

        return min
    
class Arc:
    def __init__(self, from_node: Node, to_node: Node, distance: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.distance = distance

d = DAG()

d.nodes.append(Node(1))
d.nodes.append(Node(2))         
d.nodes.append(Node(3))

d.arcs.append(Arc(d.nodes[0], d.nodes[1], 3))
d.arcs.append(Arc(d.nodes[0], d.nodes[2], 10))
d.arcs.append(Arc(d.nodes[1], d.nodes[2], 5))

# Really. Not object oriented!!
print (d.SP(d.nodes[0], d.nodes[2]))






