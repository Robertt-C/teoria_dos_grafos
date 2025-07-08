import sys
import itertools

sys.path.insert(0, "../serie_3/codigos")

from estruturas_dados import Grafo




def grafos_isomorfos(grafo1: Grafo, grafo2: Grafo) -> bool:
  ###--- Verifica se dois grafos são isomorfos ---###
  if grafo1.numero_nos() != grafo2.numero_nos():
    return False
  if grafo1.numero_arestas() != grafo2.numero_arestas():
    return False

  ###--- Gerando lista de adjacência ---###
  grafo1.cria_lista_adjacencia()
  grafo2.cria_lista_adjacencia()
  
  vertices1 = list(grafo1.nos)
  vertices2 = list(grafo2.nos)

  ###--- Testa todas as permutações dos vértices do grafo 2 ---###
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



if __name__ == "__main__":
  # Exemplo de uso
  g1 = Grafo()
  g1.adiciona_no("A")
  g1.adiciona_no("B")
  g1.adiciona_no("C")
  g1.adiciona_aresta(("A", "B"))
  g1.adiciona_aresta(("B", "C"))
  g1.adiciona_aresta(("C", "A"))

  g2 = Grafo()
  g2.adiciona_no("X")
  g2.adiciona_no("Y")
  g2.adiciona_no("Z")
  g2.adiciona_aresta(("X", "Y"))
  g2.adiciona_aresta(("Y", "Z"))
  g2.adiciona_aresta(("Z", "X"))
  
  print(grafos_isomorfos(g1, g2))  # Deve retornar True


  g3 = Grafo()
  g3.adiciona_no("A")
  g3.adiciona_no("B")
  g3.adiciona_no("C")
  g3.adiciona_no("D")
  g3.adiciona_aresta(("A", "B"))
  g3.adiciona_aresta(("B", "C"))
  g3.adiciona_aresta(("C", "D"))  # Adiciona aresta extra

  print(grafos_isomorfos(g1, g3))  # Deve retornar False