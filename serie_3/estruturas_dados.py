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
      aresta = (aresta[0], aresta[1], None)

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


  def cria_grafo_com_lista_adjacencia(self, caminho_lista_adjacencia: str) -> None:
    dados = self.carrega_arquivo_csv(caminho_lista_adjacencia)

    self.nos.clear()
    self.arestas.clear()


    for linha in dados:
      if not linha:
        continue

      no_principal = linha[0]
      vizinhos = linha[1:]

      self.adiciona_no(no_principal)

      for vizinho in vizinhos:
        self.adiciona_no(vizinho)
        self.adiciona_aresta((no_principal, vizinho))




  def numero_nos(self) -> int:
    return len(self.nos)
  

  def numero_arestas(self) -> int:
    return len(self.arestas)


  def nos_adjacentes(self, no: str) -> list[str]:
    if not self.lista_adjacencia:
      self.cria_lista_adjacencia()

    if no not in self.nos:
      print(f"O nó {no} não existe no grafo.")

    return self.lista_adjacencia[no] if no in self.lista_adjacencia else []


  def existe_aresta_entre(self, no1: str, no2: str) -> bool:
    return any({aresta[0], aresta[1]} == {no1, no2} for aresta in self.arestas)


  def grau_no(self, no: str) -> int:
    if no not in self.nos:
      print(f"O nó {no} não existe no grafo.")
      return 0

    if not self.lista_adjacencia:
      self.cria_lista_adjacencia()

    return len(self.lista_adjacencia[no]) if no in self.lista_adjacencia else 0


  def graus_nos(self) -> dict[str, int]:
    if not self.lista_adjacencia:
      self.cria_lista_adjacencia()

    resultado = {}
    for no in self.nos:
      resultado[no] = len(self.lista_adjacencia[no]) if no in self.lista_adjacencia else 0
        
    return resultado


  def caminho_simples_entre(self, no_inicio: str, no_fim: str) -> list[str]:
    if no_inicio not in self.nos or no_fim not in self.nos:
      return []

    if not self.lista_adjacencia:
      self.cria_lista_adjacencia()

    visitados = set()
    fila = [(no_inicio, [no_inicio])]

    while fila:
      atual, caminho = fila.pop(0)
      if atual == no_fim:
        return caminho

      if atual not in visitados:
        visitados.add(atual)
        for vizinho in self.lista_adjacencia[atual]:
          if vizinho not in visitados:
            fila.append((vizinho, caminho + [vizinho]))

    return []


  def ciclo_que_contem_no(self, no_inicio: str) -> list[str]:
    if no_inicio not in self.nos:
      return []
    if not self.lista_adjacencia:
      self.cria_lista_adjacencia()

    visitados = set()
    caminho = []

    def dfs(atual):
      caminho.append(atual)
      visitados.add(atual)
      for vizinho in self.lista_adjacencia[atual]:
        if vizinho == no_inicio and len(caminho) > 2:
          return caminho + [vizinho]
        if vizinho not in visitados:
          resultado = dfs(vizinho)
          if resultado:
            return resultado
      caminho.pop()

      return []

    return dfs(no_inicio)


  def e_subgrafo(self, nos_subgrupo: set[str], arestas_subgrupo: set[tuple[str, str, object]]) -> bool:
    for no in nos_subgrupo:
      print(no)
      if no not in self.nos:
        return False

    for aresta in arestas_subgrupo:
      if aresta not in self.arestas:
        return False

    return True











  

  def matriz_adjacencia_rotulada(self) -> list[list[object]]:
    nos = list(self.nos)

    ###--- Cria a primeira linha com os rótulos dos nós ---###
    matriz_com_rotulos = [[""] + nos]

    ###--- Cria cada linha com o nome do nó na primeira coluna ---###
    for i, linha in enumerate(self.matriz_adjacencia):
        matriz_com_rotulos.append([nos[i]] + linha)

    return matriz_com_rotulos

  
  def matriz_incidencia_rotulada(self) -> list[list[object]]:
    nos = list(self.nos)
    arestas_lista = list(self.arestas)

    ###--- Cria rótulos para as arestas ---###
    arestas_rotulos = [f"E{index+1}" for index in range(len(arestas_lista))]

    ###--- Cria a primeira linha com os rótulos das arestas ---###
    matriz_com_rotulos = [[""] + arestas_rotulos]

    ###--- Cria cada linha com o nome do nó na primeira coluna ---###
    for i, no in enumerate(nos):
        dados_linha = self.matriz_incidencia[i]
        matriz_com_rotulos.append([no] + dados_linha)

    return matriz_com_rotulos
  

  def lista_adjacencia(self) -> dict[str, list[str]]:
    return self.lista_adjacencia

  
  










  def print_nos(self) -> None:
    print(self.nos)
  

  def print_arestas(self) -> None:
    print(self.arestas)


  def print_matriz_adjacencia(self) -> None:
    for linha in self.matriz_adjacencia_rotulada():
      print(linha)
  

  def print_matriz_incidencia(self) -> None:
    for linha in self.matriz_incidencia_rotulada():
      print(linha)
  

  def print_lista_adjacencia(self) -> None:
    for no, vizinhos in self.lista_adjacencia.items():
      print(f"{no}: {vizinhos}")