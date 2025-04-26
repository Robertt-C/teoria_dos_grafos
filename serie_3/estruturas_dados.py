class Grafo():
  def __init__(self) -> None:
    self.nos: set[str] = set()
    self.arestas: set[tuple[str, str, object]] = set()
    
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


  def adiciona_aresta(self, aresta: tuple[str, str] | tuple[str, str, object]) -> None:

    if len(aresta) == 2:
      aresta = (aresta[0], aresta[1], "")

    aresta_ordenada = tuple(sorted(aresta[:2]))
    aresta_ordenada = (aresta_ordenada[0], aresta_ordenada[1], aresta[2])
    self.arestas.add(aresta_ordenada)
  

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
    arestas = list(aresta[:-1] for aresta in self.arestas)

    self.matriz_adjacencia = [[0 for _ in range(len(nos))] for _ in range(len(nos))]

    ###--- Preenchendo a matriz de adjacência ---###
    for i in range(len(nos)):
      for j in range(len(nos)):
        if (nos[i], nos[j]) in arestas or (nos[j], nos[i]) in arestas:
          self.matriz_adjacencia[i][j] = 1
        else:
          self.matriz_adjacencia[i][j] = 0


  def cria_matriz_incidencia(self) -> None:
    nos = list(self.nos)
    arestas = list(aresta[:-1] for aresta in self.arestas)

    self.matriz_incidencia = [[0 for _ in range(len(arestas))] for _ in range(len(nos))]

    ###--- Preenchendo a matriz de incidência ---###
    for i in range(len(nos)):
      for j in range(len(arestas)):
        if nos[i] in arestas[j]:
          self.matriz_incidencia[i][j] = 1
        else:
          self.matriz_incidencia[i][j] = 0


  def cria_lista_adjacencia(self) -> None:
    nos = list(self.nos)
    arestas = list(aresta[:-1] for aresta in self.arestas)

    self.lista_adjacencia = {no: [] for no in nos}

    ###--- Preenchendo a lista de adjacência ---###
    for aresta in arestas:
      self.lista_adjacencia[aresta[0]].append(aresta[1])
      self.lista_adjacencia[aresta[1]].append(aresta[0])


  def cria_grafo_com_matriz_adjacencia(self, caminho_matriz_adjacencia: str, nomes_nos: list[str]) -> None:
    dados = self.carrega_arquivo_csv(caminho_matriz_adjacencia)

    self.nos.clear()
    self.arestas.clear()

    ###--- Adiciona nós de acordo com os nomes fornecidos ---###
    for no in nomes_nos:
      self.adiciona_no(no)

    ###--- Adiciona arestas de acordo com a matriz de adjacência ---###
    for i in range(len(dados)):
      for j in range(len(dados[i])):
        if dados[i][j] == '1':
          self.adiciona_aresta((nomes_nos[i], nomes_nos[j]))


  def cria_grafo_com_matriz_incidencia(self, caminho_matriz_incidencia: str, nomes_nos: list[str]) -> None:
    dados = self.carrega_arquivo_csv(caminho_matriz_incidencia)

    self.nos.clear()
    self.arestas.clear()

    ###--- Adiciona nós de acordo com os nomes fornecidos ---###
    for no in nomes_nos:
        self.adiciona_no(no)

    numero_nos = len(nomes_nos)
    numero_arestas = len(dados[0])

    ###--- Adiciona arestas de acordo com a matriz de incidência ---###
    for col in range(numero_arestas):
        nos_aresta = []
        for row in range(numero_nos):
            if dados[row][col] == "1":
                nos_aresta.append(nomes_nos[row])
        if len(nos_aresta) == 2:
            self.adiciona_aresta((nos_aresta[0], nos_aresta[1]))
        elif len(nos_aresta) == 1:
            self.adiciona_aresta((nos_aresta[0], nos_aresta[0]))













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