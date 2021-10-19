import networkx as nx
import matplotlib.pyplot as plt 

def exibir_grafo(grafo):
  options = {
      'node_color': '#0080FF',
      'edge_color': '#808080',
      'node_size': 600,
      'width': 2,
      'font_color': 'white',
      'font_weight': 'bold',
      'font_size': 10

  }
  plt.figure(1)
  nx.draw_networkx(
      grafo, 
      pos=nx.spring_layout(grafo), 
      with_labels=True,
      **options
  )
  plt.show()


def bfs(graph):
    visited = {node: False for node in graph.nodes}
    startNode = list(graph.nodes)[0]
    queue = [startNode]
    visited[startNode] = True
    explored = []
    result = []
    explored.append(startNode)
    while queue:
      currentNode = queue.pop(0)
      result.append(str(currentNode))
      for node in graph.neighbors(currentNode):
        if not visited[node]:
          queue.append(node)
          visited[node] = True
          explored.append(node)
    print("Result : ", "->".join(result))
    return explored


def eh_conexo(graph):
  graphValidation = list(bfs(graph))
  graphNodes = list(graph.nodes)
  for i in graphNodes:
    if (i not in graphValidation):
      return print("Não é conexo!")
  return print("É conexo!")



def bfs_final(graph,nodeInitial,nodeFinal):
    visited = {node: False for node in graph.nodes}
    queue = [nodeInitial]
    visited[nodeInitial] = True
    explored = []
    result = []
    explored.append(nodeInitial)
    while queue:
      currentNode = queue.pop(0)
      result.append(str(currentNode))
      if (all(visited[node] == True for node in graph.neighbors(currentNode))):
        result.remove(str(currentNode))
      for node in graph.neighbors(currentNode):
        if not visited[node]:
          queue.append(node)
          visited[node] = True
          explored.append(node)
      if (currentNode == nodeFinal and visited[nodeFinal] == True):  
        result.append(str(currentNode))
        return print("Result : ", "-> ".join(result))
    return print("none")