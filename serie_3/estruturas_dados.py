class Grafo():
  def __init__(self) -> None:
    self.nos: set[str] = set()
    self.arestas: set[tuple[str, str]] = set()
    
    self.matriz_adjacencia: list[list[object]] = []
    self.matriz_incidencia: list[list[object]] = []
    self.lista_adjacencia: dict[str, list[str]] = {}




  def carrega_arquivo_csv(self, caminho: str) -> list[str] | list[list[str]]:
    dados_tratados = []

    with open(caminho, 'r', encoding = "UTF-8") as arquivo:
      dados = arquivo.readlines()

      for linha in dados:
        linha = linha.split(",")
        linha = [item.strip() for item in linha]
        dados_tratados.append(linha)
      
      return dados_tratados
  



  def adiciona_no(self, no: str) -> None:
    self.nos.add(no)


  def adiciona_aresta(self, aresta: tuple[str, str]) -> None:
    self.arestas.add(aresta)
  

  def carrega_arquivo_nos(self, caminho: str) -> None:
    dados = self.carrega_arquivo_csv(caminho)

    for linha in dados:
      for no in linha:
        self.adiciona_no(no)
  

  def carrega_arquivo_arestas(self, caminho: str) -> None:
    dados = self.carrega_arquivo_csv(caminho)

    for linha in dados:
      self.adiciona_aresta(tuple(linha))





  def cria_matriz_adjacencia(self) -> None:
    nos = list(self.nos)
    arestas = list(self.arestas)

    self.matriz_adjacencia = [[0 for _ in range(len(nos) + 1)] for _ in range(len(nos) + 1)]

    ###--- Preenchendo a primeira linha e coluna com os nós ---###
    for i in range(1, len(nos) + 1):
      self.matriz_adjacencia[0][i] = nos[i - 1]
      self.matriz_adjacencia[i][0] = nos[i - 1]

    ###--- Preenchendo a matriz de adjacência ---###
    for i in range(1, len(nos) + 1):
      for j in range(1, len(nos) + 1):
        if (nos[i - 1], nos[j - 1]) in arestas or (nos[j - 1], nos[i - 1]) in arestas:
          self.matriz_adjacencia[i][j] = 1
        else:
          self.matriz_adjacencia[i][j] = 0


  def cria_matriz_incidencia(self) -> None:
    nos = list(self.nos)
    arestas = list(self.arestas)

    self.matriz_incidencia = [[0 for _ in range(len(arestas) + 1)] for _ in range(len(nos) + 1)]

    ###--- Preenchendo a primeira linha e coluna com os nós e arestas ---###
    for i in range(1, len(nos) + 1):
      self.matriz_incidencia[i][0] = nos[i - 1]
    
    for j in range(1, len(arestas) + 1):
      self.matriz_incidencia[0][j] = arestas[j - 1]

    ###--- Preenchendo a matriz de incidência ---###
    for i in range(1, len(nos) + 1):
      for j in range(1, len(arestas) + 1):
        if nos[i - 1] in arestas[j - 1]:
            self.matriz_incidencia[i][j] = 1
        else:
            self.matriz_incidencia[i][j] = 0


  def cria_lista_adjacencia(self) -> None:
    nos = list(self.nos)
    arestas = list(self.arestas)

    self.lista_adjacencia = {no: [] for no in nos}

    for aresta in arestas:
      self.lista_adjacencia[aresta[0]].append(aresta[1])
      self.lista_adjacencia[aresta[1]].append(aresta[0])





  def print_nos(self) -> None:
      print(self.nos)
  
  def print_arestas(self) -> None:
      print(self.arestas)
  
  def print_matriz_adjacencia(self) -> None:
      for linha in self.matriz_adjacencia:
        print(linha)
  
  def print_matriz_incidencia(self) -> None:
      for linha in self.matriz_incidencia:
        print(linha)
  
  def print_lista_adjacencia(self) -> None:
      for no, lista in self.lista_adjacencia.items():
        print(f"{no}: {lista}")