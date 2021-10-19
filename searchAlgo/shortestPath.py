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

def shortestPath(graph,nodeSearch):
  startNode = nodeSearch
  path = {node: (False,0,'x') for node in graph.nodes}
  path[startNode] = (True,0,startNode)
  currentNode = startNode
  verify = False
  while verify == False :
    neighbors = graph.neighbors(currentNode)
    for node in neighbors:
      weigth = graph.get_edge_data(node,currentNode)
      weigth = list(weigth.values())[0]
      weigth = weigth + path[currentNode][1]
      if (path[node][1] > weigth or path[node][1] == 0 and path[node][0] == False):
        path[node] = (False,weigth,currentNode)
    smallerValue = 812374987198423712897
    for i in path:
      if(path[i][1] != 0 and path[i][1] < smallerValue and path[i][0] == False):
        currentNode = i
        smallerValue = path[i][1]
    path[currentNode] = (True,path[currentNode][1],path[currentNode][2])   
    validationArr = []
    for i in path:
      validationArr.append(path[i][0])
    if False not in validationArr:
      verify = True;

  
  print("Tabela de menor caminho do vertice:",nodeSearch)
  for i in path:
    print(i,':',path[i])
  table = []


def shortestPathFinal(graph,nodeSearch,nodeFinal):
  startNode = nodeSearch
  path = {node: (False,0,'x') for node in graph.nodes}
  path[startNode] = (True,0,startNode)
  currentNode = startNode
  verify = False
  while verify == False :
    neighbors = graph.neighbors(currentNode)
    for node in neighbors:
      weigth = graph.get_edge_data(node,currentNode)
      weigth = list(weigth.values())[0]
      weigth = weigth + path[currentNode][1]
      if (path[node][1] > weigth or path[node][1] == 0 and path[node][0] == False):
        path[node] = (False,weigth,currentNode)
    smallerValue = 812374987198423712897
    for i in path:
      if(path[i][1] != 0 and path[i][1] < smallerValue and path[i][0] == False):
        currentNode = i
        smallerValue = path[i][1]
    path[currentNode] = (True,path[currentNode][1],path[currentNode][2])   
    if path[nodeFinal][0] == True:
      verify = True;
  pathFinal = [nodeFinal]
  nodeCurrent = nodeFinal
  while True:
    nodeTest = path[nodeCurrent][2]
    pathFinal.append(nodeTest)
    if (nodeTest == nodeSearch):
      break
    else:
      nodeCurrent = nodeTest

  print("Menor caminho do vertice:",nodeSearch,"até o vertice",nodeFinal)
  print("Caminho: ",' -> '.join(list(reversed(pathFinal))))