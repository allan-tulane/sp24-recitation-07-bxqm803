from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
      current = frontier.pop()
      neighbor = graph[current]
      for i in neighbor:
        if i not in result:
          result.add(i)
          frontier.add(i)
    return result





def connected(graph):
  start_node = next(iter(graph))   
  return len(reachable(graph, start_node)) == len(graph)





def n_components(graph):
  count=0
  visited=set()
  for i in graph:
     if i not in visited:
       node=reachable(graph,i)
       visited.update(node)
       count+=1
  return count

