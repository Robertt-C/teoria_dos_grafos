import random
from collections import deque
import itertools

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
  
  def carrega_arquivos_nos_e_arestas(self, caminho_nos: str, caminho_arestas: str) -> None:
    dados_nos = self.carrega_arquivo_csv(caminho_nos)
    dados_arestas = self.carrega_arquivo_csv(caminho_arestas)

    indice_coluna_rotulo_no = dados_nos[0].index("Label")
    indice_coluna_id_no = dados_nos[0].index("Id")

    indice_coluna_origem_aresta = dados_arestas[0].index("Source")
    indice_coluna_destino_aresta = dados_arestas[0].index("Target")
    indice_coluna_peso_aresta = dados_arestas[0].index("Weight")

    coluna_id_nos = [linha[indice_coluna_id_no] for linha in dados_nos]

    for linha in range(1, len(dados_nos)):
      self.adiciona_no(dados_nos[linha][indice_coluna_rotulo_no])

    for linha in range(1, len(dados_arestas)):
      id_no_origem = dados_arestas[linha][indice_coluna_origem_aresta]
      id_no_destino = dados_arestas[linha][indice_coluna_destino_aresta]

      indice_rotulo_no_origem = coluna_id_nos.index(id_no_origem)
      indice_rotulo_no_destino = coluna_id_nos.index(id_no_destino)

      rotulo_no = dados_nos[indice_rotulo_no_origem][indice_coluna_rotulo_no]
      rotulo_no_destino = dados_nos[indice_rotulo_no_destino][indice_coluna_rotulo_no]

      self.adiciona_aresta((rotulo_no, rotulo_no_destino, dados_arestas[linha][indice_coluna_peso_aresta]))

  def mostrar_vertices(self) -> None:
    print("Vértices:")
    for vertice in self.nos:
        print(f"- {vertice}")

  def mostrar_arestas(self) -> None:
    print("Arestas:")
    for origem, destino, peso in self.arestas:
        print(f"- {origem} --({peso})-- {destino}")

  def cria_matriz_adjacencia(self) -> None:
    nos = list(self.nos)
    arestas = list(aresta[:-1] for aresta in self.arestas)

    self.matriz_adjacencia = [[0 for _ in range(len(nos))] for _ in range(len(nos))]

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

    for aresta in arestas:
      self.lista_adjacencia[aresta[0]].append(aresta[1])
      self.lista_adjacencia[aresta[1]].append(aresta[0])

  def cria_grafo_com_matriz_adjacencia(self, caminho_matriz_adjacencia: str, nomes_nos: list[str]) -> None:
    dados = self.carrega_arquivo_csv(caminho_matriz_adjacencia)

    self.nos.clear()
    self.arestas.clear()

    for no in nomes_nos:
      self.adiciona_no(no)

    for i in range(len(dados)):
      for j in range(len(dados[i])):
        if dados[i][j] == '1':
          self.adiciona_aresta((nomes_nos[i], nomes_nos[j]))

  def cria_grafo_com_matriz_incidencia(self, caminho_matriz_incidencia: str, nomes_nos: list[str]) -> None:
    dados = self.carrega_arquivo_csv(caminho_matriz_incidencia)

    self.nos.clear()
    self.arestas.clear()

    for no in nomes_nos:
      self.adiciona_no(no)

    numero_nos = len(nomes_nos)
    numero_arestas = len(dados[0])

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
      if no not in self.nos:
        return False

    for aresta in arestas_subgrupo:
      if aresta not in self.arestas:
        return False

    return True

  def e_disjunto_aresta(self, arestas_subgrupo: set[tuple[str, str, object]]) -> bool:
    for aresta in arestas_subgrupo:
      if aresta in self.arestas:
        return False
    return True

  def e_disjunto_vertice(self, nos_subgrupo: set[str]) -> bool:
    for no in nos_subgrupo:
      if no in self.nos:
        return False
    return True

  def mostrar_cinco_subgrafos(self) -> None:
    if len(self.nos) < 2:
        print("Grafo muito pequeno para gerar subgrafos.")
        return

    nos_lista = list(self.nos)
    arestas_lista = list(self.arestas)

    print("\nCinco subgrafos encontrados:")

    for i in range(1, 6):
        quantidade_nos = random.randint(1, len(nos_lista))
        nos_subgrafo = set(random.sample(nos_lista, quantidade_nos))

        arestas_subgrafo = set()
        for aresta in arestas_lista:
            if aresta[0] in nos_subgrafo and aresta[1] in nos_subgrafo:
                arestas_subgrafo.add(aresta)

        print(f"\nSubgrafo {i}:")
        print(f"Nós: {nos_subgrafo}")
        print(f"Arestas: {arestas_subgrafo}")

  def matriz_adjacencia_rotulada(self) -> list[list[object]]:
    nos = list(self.nos)

    matriz_com_rotulos = [[""] + nos]

    for i, linha in enumerate(self.matriz_adjacencia):
        matriz_com_rotulos.append([nos[i]] + linha)

    return matriz_com_rotulos
  
  def matriz_incidencia_rotulada(self) -> list[list[object]]:
    nos = list(self.nos)
    arestas_lista = list(self.arestas)

    arestas_rotulos = [f"E{index+1}" for index in range(len(arestas_lista))]

    matriz_com_rotulos = [[""] + arestas_rotulos]

    for i, no in enumerate(nos):
        dados_linha = self.matriz_incidencia[i]
        matriz_com_rotulos.append([no] + dados_linha)

    return matriz_com_rotulos

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


# Funções de serie_5 - grafos isomorfos
def grafos_isomorfos(grafo1: Grafo, grafo2: Grafo) -> bool:
  """Verifica se dois grafos são isomorfos"""
  if grafo1.numero_nos() != grafo2.numero_nos():
    return False
  if grafo1.numero_arestas() != grafo2.numero_arestas():
    return False

  grafo1.cria_lista_adjacencia()
  grafo2.cria_lista_adjacencia()
  
  vertices1 = list(grafo1.nos)
  vertices2 = list(grafo2.nos)

  for permutacao in itertools.permutations(vertices2):
    mapeamento = dict(zip(vertices1, permutacao))
    e_isomorfo = True
    for v in vertices1:
      vizinhos_mapeados = {mapeamento[n] for n in grafo1.lista_adjacencia[v]}
      if vizinhos_mapeados != set(grafo2.lista_adjacencia[mapeamento[v]]):
        e_isomorfo = False
        break
    if e_isomorfo:
      return True
    
  return False

# Funções de serie_5d - operações em grafos
def is_connected(grafo: Grafo) -> bool:
    """Verifica se um grafo é conexo"""
    if not grafo.nos:
        return True
    
    if not grafo.lista_adjacencia:
        grafo.cria_lista_adjacencia()
    
    visitados = set()
    nos = list(grafo.nos)
    start = nos[0]
    
    def dfs(v):
        visitados.add(v)
        for vizinho in grafo.lista_adjacencia[v]:
            if vizinho not in visitados:
                dfs(vizinho)
    
    dfs(start)
    return len(visitados) == len(grafo.nos)

def is_eulerian(grafo: Grafo) -> bool:
    """Verifica se um grafo é euleriano (todos os vértices têm grau par)"""
    if not is_connected(grafo):
        return False
    
    graus = grafo.graus_nos()
    return all(grau % 2 == 0 for grau in graus.values())

def has_hamiltonian_cycle(grafo: Grafo) -> bool:
    """Verifica se um grafo possui ciclo hamiltoniano"""
    if not is_connected(grafo):
        return False

    verts = list(grafo.nos)
    if not grafo.lista_adjacencia:
        grafo.cria_lista_adjacencia()
    
    for perm in itertools.permutations(verts):
        ciclo = True
        for i in range(len(perm)):
            u = perm[i]
            v = perm[(i + 1) % len(perm)]
            if v not in grafo.lista_adjacencia[u]:
                ciclo = False
                break
        if ciclo:
            return True
    return False

def graph_union(g1: Grafo, g2: Grafo) -> Grafo:
    """União de dois grafos"""
    resultado = Grafo()
    
    # União de vértices
    for no in g1.nos:
        resultado.adiciona_no(no)
    for no in g2.nos:
        resultado.adiciona_no(no)
    
    # União de arestas
    for aresta in g1.arestas:
        resultado.adiciona_aresta(aresta)
    for aresta in g2.arestas:
        resultado.adiciona_aresta(aresta)
    
    return resultado

def graph_intersection(g1: Grafo, g2: Grafo) -> Grafo:
    """Interseção de dois grafos"""
    resultado = Grafo()
    
    # Interseção de vértices
    for no in g1.nos:
        if no in g2.nos:
            resultado.adiciona_no(no)
    
    # Interseção de arestas
    for aresta in g1.arestas:
        if any(set(aresta[:2]) == set(a[:2]) for a in g2.arestas):
            resultado.adiciona_aresta(aresta)
    
    return resultado

def graph_symmetric_difference(g1: Grafo, g2: Grafo) -> Grafo:
    """Diferença simétrica de dois grafos"""
    uniao = graph_union(g1, g2)
    intersecao = graph_intersection(g1, g2)
    
    resultado = Grafo()
    
    # Adiciona vértices da união
    for no in uniao.nos:
        resultado.adiciona_no(no)
    
    # Adiciona arestas que estão na união mas não na interseção
    for aresta in uniao.arestas:
        if not any(set(aresta[:2]) == set(a[:2]) for a in intersecao.arestas):
            resultado.adiciona_aresta(aresta)
    
    return resultado

def remove_vertex(g: Grafo, vi: str) -> Grafo:
    """Remove um vértice e suas arestas adjacentes"""
    if vi not in g.nos:
        print(f"Erro: O vértice {vi} não existe no grafo")
        return None
    
    resultado = Grafo()
    
    # Adiciona todos os vértices exceto vi
    for no in g.nos:
        if no != vi:
            resultado.adiciona_no(no)
    
    # Adiciona todas as arestas que não contêm vi
    for aresta in g.arestas:
        if vi not in aresta[:2]:
            resultado.adiciona_aresta(aresta)
    
    return resultado

def remove_edge(g: Grafo, ei: tuple) -> Grafo:
    """Remove uma aresta do grafo"""
    resultado = Grafo()
    
    # Adiciona todos os vértices
    for no in g.nos:
        resultado.adiciona_no(no)
    
    # Adiciona todas as arestas exceto ei
    for aresta in g.arestas:
        if set(aresta[:2]) != set(ei[:2]):
            resultado.adiciona_aresta(aresta)
    
    return resultado

def merge_vertices(g: Grafo, vi: str, vj: str) -> Grafo:
    """Funde dois vértices em um grafo"""
    if vi not in g.nos or vj not in g.nos:
        print(f"Erro: Um dos vértices não existe no grafo")
        return None
    
    if vi == vj:
        print(f"Erro: Os vértices são iguais. Não é possível fundir.")
        return None
    
    resultado = Grafo()
    
    # Adiciona todos os vértices exceto vj
    for no in g.nos:
        if no != vj:
            resultado.adiciona_no(no)
    
    # Adiciona arestas, substituindo vj por vi
    for origem, destino, peso in g.arestas:
        nova_origem = vi if origem == vj else origem
        novo_destino = vi if destino == vj else destino
        
        # Evita self-loops
        if nova_origem != novo_destino:
            resultado.adiciona_aresta((nova_origem, novo_destino, peso))
    
    return resultado

# Funções de serie_6_c_a - árvores
def e_arvore(grafo: Grafo) -> bool:
    """Verifica se um grafo é uma árvore (conexo e sem ciclos)"""
    if grafo.numero_arestas() != grafo.numero_nos() - 1:
        return False

    if not grafo.nos:
        return False

    nos = list(grafo.nos)
    inicio = nos[0]
    visitados = set()
    fila = deque([inicio])

    if not grafo.lista_adjacencia:
        grafo.cria_lista_adjacencia()

    while fila:
        atual = fila.popleft()
        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo.lista_adjacencia[atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)

    # Se visitou todos os nós, é conexo
    return len(visitados) == grafo.numero_nos()

def e_subgrafo_arvore(G: Grafo, A1: Grafo) -> bool:
    """Verifica se um grafo é subgrafo e árvore"""
    if not e_arvore(A1):
        return False

    return G.e_subgrafo(A1.nos, A1.arestas)

def e_arvore_abrangencia(G: Grafo, A1: Grafo) -> bool:
    """Verifica se é árvore de abrangência (subgrafo e contém todos os vértices)"""
    if not e_subgrafo_arvore(G, A1):
        return False
    return A1.nos == G.nos

def encontrar_centros(A: Grafo) -> list[str]:
    """Encontra o(s) centro(s) de uma árvore"""
    if not e_arvore(A):
        return []

    if A.numero_nos() <= 2:
        return list(A.nos)

    if not A.lista_adjacencia:
        A.cria_lista_adjacencia()

    graus = {}
    folhas = []

    for no, vizinhos in A.lista_adjacencia.items():
        grau = len(vizinhos)
        graus[no] = grau

        if grau == 1:
            folhas.append(no)

    vertices_restantes = A.numero_nos()
    while vertices_restantes > 2:
        novas_folhas = []
        for folha in folhas:
            vertices_restantes -= 1
            for vizinho in A.lista_adjacencia[folha]:
                graus[vizinho] -= 1
                if graus[vizinho] == 1:
                    novas_folhas.append(vizinho)
        folhas = novas_folhas

    return folhas

def excentricidades(A: Grafo):
    """Calcula as excentricidades dos vértices de uma árvore"""
    excentricidades = {}

    if not e_arvore(A):
        return excentricidades

    if not A.lista_adjacencia:
        A.cria_lista_adjacencia()

    lista_adjacencia = A.lista_adjacencia

    for vertice_inicial in lista_adjacencia:
        distancias = {v: -1 for v in lista_adjacencia}
        fila = deque([(vertice_inicial, 0)])
        distancias[vertice_inicial] = 0
        max_distancia = 0

        while fila:
            vertice_atual, dist_atual = fila.popleft()
            max_distancia = max(max_distancia, dist_atual)

            for vizinho in lista_adjacencia[vertice_atual]:
                if distancias[vizinho] == -1:
                    distancias[vizinho] = dist_atual + 1
                    fila.append((vizinho, dist_atual + 1))

        excentricidades[vertice_inicial] = max_distancia

    return excentricidades

def raio(A: Grafo) -> int:
    """Calcula o raio de uma árvore (mínima excentricidade entre todos os vértices)"""
    if not e_arvore(A):
        print("O grafo fornecido não é uma árvore.")
        return -1
    
    excs = excentricidades(A)
    if not excs:
        return -1
    
    return min(excs.values())

def gerar_arvore_abrangencia(G: Grafo) -> Grafo:
    """Gera uma árvore de abrangência usando BFS"""
    if not G.nos:
        return Grafo()
    
    if not is_connected(G):
        print("O grafo não é conexo. Não é possível gerar árvore de abrangência.")
        return Grafo()
    
    A = Grafo()
    for no in G.nos:
        A.adiciona_no(no)
    
    if not G.lista_adjacencia:
        G.cria_lista_adjacencia()
    
    start = next(iter(G.nos))
    visitados = {start}
    fila = deque([start])
    
    while fila:
        atual = fila.popleft()
        for vizinho in G.lista_adjacencia[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                # Encontra o peso da aresta, se houver
                peso = None
                for aresta in G.arestas:
                    if {aresta[0], aresta[1]} == {atual, vizinho}:
                        peso = aresta[2]
                        break
                A.adiciona_aresta((atual, vizinho, peso))
    
    return A

def gerar_k_arvores_abrangencia(G: Grafo, k: int) -> list[Grafo]:
    """
    Gera k árvores de abrangência diferentes usando trocas cíclicas
    Retorna uma lista de árvores de abrangência
    """
    if not is_connected(G):
        print("O grafo não é conexo. Não é possível gerar árvores de abrangência.")
        return []
    
    # Cria a primeira árvore de abrangência
    A1 = gerar_arvore_abrangencia(G)
    arvores = [A1]
    
    # Se o grafo é uma árvore, não há outras árvores de abrangência
    if G.numero_arestas() == G.numero_nos() - 1:
        print("O grafo já é uma árvore. Não há outras árvores de abrangência.")
        return arvores
    
    # Armazena arestas não utilizadas na árvore inicial
    arestas_nao_utilizadas = []
    for aresta in G.arestas:
        existe = False
        for a_aresta in A1.arestas:
            if {aresta[0], aresta[1]} == {a_aresta[0], a_aresta[1]}:
                existe = True
                break
        if not existe:
            arestas_nao_utilizadas.append(aresta)
    
    tentativas = 0
    max_tentativas = 100  # Limite para evitar loops infinitos
    
    while len(arvores) < k and tentativas < max_tentativas and arestas_nao_utilizadas:
        # Escolhe uma aresta não utilizada aleatoriamente
        idx = random.randint(0, len(arestas_nao_utilizadas) - 1)
        aresta_adicionar = arestas_nao_utilizadas[idx]
        
        # Cria uma nova árvore temporária adicionando a aresta
        nova_arvore = Grafo()
        for no in A1.nos:
            nova_arvore.adiciona_no(no)
        for aresta in A1.arestas:
            nova_arvore.adiciona_aresta(aresta)
        
        nova_arvore.adiciona_aresta(aresta_adicionar)
        
        # A adição formou um ciclo; precisamos encontrá-lo e remover uma aresta
        if not e_arvore(nova_arvore):
            # Encontra o ciclo que contém a aresta adicionada
            u, v = aresta_adicionar[0], aresta_adicionar[1]
            
            # Gera lista de adjacência
            nova_arvore.cria_lista_adjacencia()
            
            # BFS para encontrar caminho de u a v sem usar a aresta (u,v)
            caminho = []
            visitados = {u}
            fila = deque([(u, [u])])
            
            while fila:
                atual, path = fila.popleft()
                for vizinho in nova_arvore.lista_adjacencia[atual]:
                    # Não use diretamente a aresta adicionada
                    if {atual, vizinho} == {u, v}:
                        continue
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        novo_caminho = path + [vizinho]
                        if vizinho == v:
                            caminho = novo_caminho
                            break
                        fila.append((vizinho, novo_caminho))
                if caminho:
                    break
            
            if caminho:
                # Escolhe uma aresta do ciclo para remover
                for i in range(len(caminho) - 1):
                    u_ciclo, v_ciclo = caminho[i], caminho[i+1]
                    # Encontra a aresta completa com peso
                    aresta_remover = None
                    for aresta in nova_arvore.arestas:
                        if {aresta[0], aresta[1]} == {u_ciclo, v_ciclo}:
                            aresta_remover = aresta
                            break
                    
                    if aresta_remover:
                        # Remove a aresta e verifica se é uma nova árvore
                        temp = remove_edge(nova_arvore, (aresta_remover[0], aresta_remover[1]))
                        
                        # Verifica se esta árvore já existe na lista
                        nova = True
                        for a in arvores:
                            edges_a = {(e[0], e[1]) for e in a.arestas}
                            edges_temp = {(e[0], e[1]) for e in temp.arestas}
                            if edges_a == edges_temp:
                                nova = False
                                break
                        
                        if nova:
                            arvores.append(temp)
                            break
        
        tentativas += 1
        if tentativas >= max_tentativas:
            print(f"Atingido limite de tentativas. Geradas {len(arvores)} árvores.")
    
    return arvores

def distancia_entre_arvores(A1: Grafo, A2: Grafo) -> int:
    """
    Calcula a distância entre duas árvores (número de arestas diferentes)
    """
    if not e_arvore(A1) or not e_arvore(A2):
        print("Um dos grafos fornecidos não é uma árvore.")
        return -1
    
    if A1.nos != A2.nos:
        print("As árvores não têm os mesmos vértices.")
        return -1
    
    # Conta arestas exclusivas de cada árvore
    distancia = 0
    
    # Cria conjuntos de arestas (sem considerar pesos)
    edges_A1 = {frozenset([a[0], a[1]]) for a in A1.arestas}
    edges_A2 = {frozenset([a[0], a[1]]) for a in A2.arestas}
    
    # Calcula a diferença simétrica
    return len(edges_A1.symmetric_difference(edges_A2))

def arvore_central(G: Grafo, num_arvores: int = 10) -> Grafo:
    """
    Determina a árvore central de um grafo (a árvore de abrangência com menor diâmetro)
    """
    if not is_connected(G):
        print("O grafo não é conexo. Não é possível determinar árvore central.")
        return Grafo()
    
    # Gera várias árvores de abrangência
    arvores = gerar_k_arvores_abrangencia(G, num_arvores)
    
    melhor_arvore = None
    menor_diametro = float('inf')
    
    for arvore in arvores:
        excs = excentricidades(arvore)
        if excs:
            diametro = max(excs.values())
            if diametro < menor_diametro:
                menor_diametro = diametro
                melhor_arvore = arvore
    
    return melhor_arvore if melhor_arvore else (arvores[0] if arvores else Grafo())