
import Queue

class Edge(object):
    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.capacity = c
        self.rev_edge = None

    def __str__(self):
        return "{0}->{1}:{2}".format(self.u, self.v, self.capacity)
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.u == other.u and self.v == other.v
        return False

    def __hash__(self):
        return hash(str(self))

class Graph(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}

    def add_vertices(self, n):
        for i in xrange(n):
            self.adj[i] = []

    def add_edge(self, u, v, c=0):
        if u != v:
            edge = Edge(u, v, c)
            rev_edge = Edge(v, u, 0)
            self.adj[u].append(edge)
            self.adj[v].append(rev_edge)
            self.flow[edge] = 0
            self.flow[rev_edge] = 0;
            edge.rev_edge = rev_edge
            rev_edge.rev_edge = edge

    def get_path(self, source, sink, prev):
        if source != sink:
            path = []
            curr = sink
            while curr != source:
                u = prev[curr]
                path.append(filter(lambda edge: edge.v == curr, self.adj[u])[0])
                curr = u
            return path
        return None

    def find_path(self, source, sink):
        prev = {}
        for i in self.adj:
            prev[i] = -1
        
        q = Queue.Queue()
        q.put(source)
        while q.qsize():
            u = q.get()
            for edge in self.adj[u]:
                if edge.capacity > self.flow[edge] and prev[edge.v] == -1:
                    prev[edge.v] = u
                    if (edge.v == sink):
                        return self.get_path(source, sink, prev) 
                    q.put(edge.v)
        return None 

    def max_flow(self, source, sink):
        path = self.find_path(source, sink)
        while path:
            res_flow = [edge.capacity - self.flow[edge] for edge in path]
            add_flow = min(res_flow)
            for edge in path:
                self.flow[edge] += add_flow
                self.flow[edge.rev_edge] = -self.flow[edge]
            path = self.find_path(source, sink)
        return sum(self.flow[edge] for edge in self.adj[source])

    
if __name__ == '__main__':
    g = Graph()
    g.add_vertices(6)
    g.add_edge(0, 1, 3)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 4)
    g.add_edge(2, 4, 2)
    g.add_edge(4, 5, 3)
    g.add_edge(3, 4, 4)
    g.add_edge(3, 5, 2)
    print g.max_flow(0,5)

