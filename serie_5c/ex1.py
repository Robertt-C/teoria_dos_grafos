import networkx as nx
import matplotlib.pyplot as plt

class AdjacencyList:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {vertice: [] for vertice in range(len(vertices))}
        for i, (u, v) in enumerate(self.edges):
            u_index = self.vertices.index(u)
            v_index = self.vertices.index(v)
            self.adjacency_list[u_index].append(v)
            self.adjacency_list[v_index].append(u)
    
    def display_adjacency_list(self):
        self.render_graph()
        print("Lista de adjacência:")
        for v, neighbors in self.adjacency_list.items():
            print(f"Vertice {self.vertices[v]}: {neighbors}")
    
    def render_graph(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.vertices)
        graph.add_edges_from(self.edges)
        pos = nx.circular_layout(graph)
        nx.draw(graph, with_labels=True, pos=pos)
        plt.show()  

def graph_union(g1, g2):
    # União de vértices
    vertices_union = set(g1.vertices) | set(g2.vertices)
    # União de arestas
    edges_union = g1.edges.copy()
    for edge in g2.edges:
        if edge not in edges_union and (edge[1], edge[0]) not in edges_union:
            edges_union.append(edge)
    
    return AdjacencyList(list(vertices_union), edges_union)

def graph_intersection(g1, g2):
    # Interseção de vértices
    vertices_intersect = set(g1.vertices) & set(g2.vertices)
    # Interseção de arestas
    edges_intersect = [edge for edge in g1.edges if edge in g2.edges or (edge[1], edge[0]) in g2.edges]
    
    return AdjacencyList(list(vertices_intersect), edges_intersect)

def graph_symmetric_difference(g1, g2):
    # União dos grafos
    union = graph_union(g1, g2)
    # Interseção dos grafos
    intersection = graph_intersection(g1, g2)
    
    # Vértices na diferença simétrica
    vertices_symmetric_difference = union.vertices
    
    # Arestas na diferença simétrica
    edges_symmetric_difference = [edge for edge in union.edges if edge not in intersection.edges]
    
    return AdjacencyList(vertices_symmetric_difference, edges_symmetric_difference)

def remove_vertex(g1, vi):
    """
    Verifica se vi é vértice de G1 e, se for, gera G2 sem vi
    """
    # Verifica se vi é realmente um vértice de G1
    if vi not in g1.vertices:
        print(f"Erro: O vértice {vi} não existe no grafo G1")
        return None
    
    # Criar nova lista de vértices sem vi
    new_vertices = [v for v in g1.vertices if v != vi]
    
    # Criar nova lista de arestas sem as que contêm vi
    new_edges = []
    for edge in g1.edges:
        if vi not in edge:
            new_edges.append(edge)
        else:
            print(f"Removendo aresta {edge} que contém o vértice {vi}")
    
    # Criar e retornar o novo grafo G2
    g2 = AdjacencyList(new_vertices, new_edges)
    print(f"Grafo G2 criado sem o vértice {vi}")
    return g2

def remove_edge(g1, ei):
    """
    Verifica se ei é aresta de G1 e, se for, gera G2 sem ei
    """
    # Verifica se ei é realmente uma aresta de G1 (considerando ambas direções)
    if ei not in g1.edges and (ei[1], ei[0]) not in g1.edges:
        print(f"Erro: A aresta {ei} não existe no grafo G1")
        return None
    
    # Criar nova lista de arestas sem ei
    new_edges = []
    for edge in g1.edges:
        if edge != ei and edge != (ei[1], ei[0]):
            new_edges.append(edge)
        else:
            print(f"Removendo aresta {edge}")
    
    # Manter os mesmos vértices
    new_vertices = g1.vertices.copy()
    
    # Criar e retornar o novo grafo G2
    g2 = AdjacencyList(new_vertices, new_edges)
    print(f"Grafo G2 criado sem a aresta {ei}")
    return g2

def merge_vertices(g1, vi, vj):
    """
    Verifica se vi e vj são vértices de G1 e, se forem, gera G2 onde vi e vj foram fundidos
    """
    # Verifica se ambos os vértices existem em G1
    if vi not in g1.vertices:
        print(f"Erro: O vértice {vi} não existe no grafo G1")
        return None
    
    if vj not in g1.vertices:
        print(f"Erro: O vértice {vj} não existe no grafo G1")
        return None
    
    if vi == vj:
        print(f"Erro: Os vértices são iguais ({vi}). Não é possível fundir um vértice consigo mesmo.")
        return None
    
    
    # Criar nova lista de vértices (remove vj, mantém vi)
    new_vertices = [v for v in g1.vertices if v != vj]
    
    # Criar nova lista de arestas substituindo vj por vi
    new_edges = []
    for edge in g1.edges:
        u, v = edge
        
        # Substitui vj por vi nas arestas
        if u == vj:
            u = vi
        if v == vj:
            v = vi
        
        # Evita self-loops (aresta de um vértice para ele mesmo)
        if u != v:
            new_edge = (u, v)
            # Evita arestas duplicadas
            if new_edge not in new_edges and (v, u) not in new_edges:
                new_edges.append(new_edge)
                print(f"Aresta {edge} transformada em {new_edge}")
        else:
            print(f"Removendo self-loop que seria criado: ({u}, {v})")
    
    # Criar e retornar o novo grafo G2
    g2 = AdjacencyList(new_vertices, new_edges)
    print(f"Grafo G2 criado com vértices {vi} e {vj} fundidos")
    return g2

def demonstracao_completa():
    """Demonstração completa do programa com todas as funcionalidades"""
    print("="*60)
    print("           DEMONSTRAÇÃO")
    print("="*60)
    
    # Grafos originais do exemplo
    print("\nGrafos iniciais:")
    print("-" * 30)
    g1 = AdjacencyList([1, 2, 3], [(1, 2), (2, 3)])
    print("G1:")
    g1.display_adjacency_list()
    
    g2 = AdjacencyList([2, 3, 4], [(2, 3), (3, 4)])
    print("\nG2:")
    g2.display_adjacency_list()
    
    # Operações de conjunto
    print("\nOperações:")
    print("-" * 30)
    
    uniao = graph_union(g1, g2)
    print(f'\nUnião - Vértices: {uniao.vertices} / Arestas: {uniao.edges}')
    uniao.display_adjacency_list()
    
    intersecao = graph_intersection(g1, g2)
    print(f'\nInterseção - Vértices: {intersecao.vertices} / Arestas: {intersecao.edges}')
    intersecao.display_adjacency_list()
    
    diferenca_simetrica = graph_symmetric_difference(g1, g2)
    print(f'\nDiferença Simétrica - Vértices: {diferenca_simetrica.vertices} / Arestas: {diferenca_simetrica.edges}')
    diferenca_simetrica.display_adjacency_list()
    
    g_exemplo = AdjacencyList([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4), (1, 4)])
    print("\nCriando novo grafo para demonstrar funções de remoção/fusão:")
    g_exemplo.display_adjacency_list()
    
    print("\nRemoção de vértice:")
    g2_remove_vertex = remove_vertex(g_exemplo, 2)
    if g2_remove_vertex:
        print("Grafo após remoção do vértice 2:")
        g2_remove_vertex.display_adjacency_list()
    
    print("\nRemoção de aresta:")
    print("-" * 25)
    g2_remove_edge = remove_edge(g_exemplo, (1, 4))
    if g2_remove_edge:
        print("Grafo após remoção da aresta (1, 4):")
        g2_remove_edge.display_adjacency_list()
    
    print("\nFusão de vértices:")
    print("-" * 25)
    g2_merge = merge_vertices(g_exemplo, 1, 3)
    if g2_merge:
        print("Grafo após fusão dos vértices 1 e 3:")
        g2_merge.display_adjacency_list()
    
def menu_interativo():
    """Menu interativo para usar as funções manualmente"""
    print("="*60)
    print("           MENU")
    print("="*60)
    
    # Grafo padrão para começar
    grafo_atual = AdjacencyList([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4), (1, 4)])
    
    while True:
        print(f"\nGrafo atual - Vértices: {grafo_atual.vertices} / Arestas: {grafo_atual.edges}")
        print("\nEscolha uma opção:")
        print("1. Visualizar grafo atual")
        print("2. Criar novo grafo")
        print("3. Remover vértice")
        print("4. Remover aresta")
        print("5. Fundir vértices")
        print("6. Operações de conjunto (união, interseção, diferença simétrica)")
        print("0. Sair")
        
        try:
            opcao = input("\nDigite sua opção: ").strip()
            
            if opcao == "0":
                print("Saindo do programa...")
                break
                
            elif opcao == "1":
                print("\nGrafo atual:")
                grafo_atual.display_adjacency_list()
                
            elif opcao == "2":
                print("\nCriando novo grafo:")
                vertices_str = input("Digite os vértices separados por vírgula (ex: 1,2,3,4): ")
                vertices = [int(v.strip()) for v in vertices_str.split(",")]
                
                print("Digite as arestas no formato (u,v), separadas por ponto e vírgula")
                print("Exemplo: (1,2);(2,3);(3,4)")
                arestas_str = input("Arestas: ")
                
                arestas = []
                for aresta_str in arestas_str.split(";"):
                    aresta_str = aresta_str.strip().replace("(", "").replace(")", "")
                    u, v = map(int, aresta_str.split(","))
                    arestas.append((u, v))
                
                grafo_atual = AdjacencyList(vertices, arestas)
                print("Novo grafo criado com sucesso!")
                grafo_atual.display_adjacency_list()
                
            elif opcao == "3":
                print("\nRemover vértice:")
                vertice = int(input("Digite o vértice a ser removido: "))
                novo_grafo = remove_vertex(grafo_atual, vertice)
                if novo_grafo:
                    grafo_atual = novo_grafo
                    print("Vértice removido com sucesso!")
                    
            elif opcao == "4":
                print("\nRemover aresta:")
                u = int(input("Digite o primeiro vértice da aresta: "))
                v = int(input("Digite o segundo vértice da aresta: "))
                novo_grafo = remove_edge(grafo_atual, (u, v))
                if novo_grafo:
                    grafo_atual = novo_grafo
                    print("Aresta removida com sucesso!")
                    
            elif opcao == "5":
                print("\nFundir vértices:")
                vi = int(input("Digite o primeiro vértice: "))
                vj = int(input("Digite o segundo vértice: "))
                novo_grafo = merge_vertices(grafo_atual, vi, vj)
                if novo_grafo:
                    grafo_atual = novo_grafo
                    print("Vértices fundidos com sucesso!")
                    
            elif opcao == "6":
                print("\nOperações de conjunto:")
                print("Você precisa criar um segundo grafo primeiro.")
                
                vertices_str = input("Digite os vértices do segundo grafo separados por vírgula: ")
                vertices2 = [int(v.strip()) for v in vertices_str.split(",")]
                
                print("Digite as arestas do segundo grafo no formato (u,v), separadas por ponto e vírgula")
                arestas_str = input("Arestas: ")
                
                arestas2 = []
                for aresta_str in arestas_str.split(";"):
                    aresta_str = aresta_str.strip().replace("(", "").replace(")", "")
                    u, v = map(int, aresta_str.split(","))
                    arestas2.append((u, v))
                
                grafo2 = AdjacencyList(vertices2, arestas2)
                print("\nSegundo grafo:")
                grafo2.display_adjacency_list()
                
                print("\nEscolha a operação:")
                print("1. União")
                print("2. Interseção")
                print("3. Diferença simétrica")
                
                op = input("Opção: ").strip()
                
                if op == "1":
                    resultado = graph_union(grafo_atual, grafo2)
                    print("\nResultado da União:")
                elif op == "2":
                    resultado = graph_intersection(grafo_atual, grafo2)
                    print("\nResultado da Interseção:")
                elif op == "3":
                    resultado = graph_symmetric_difference(grafo_atual, grafo2)
                    print("\nResultado da Diferença Simétrica:")
                else:
                    print("Opção inválida!")
                    continue
                    
                resultado.display_adjacency_list()
                
                usar_resultado = input("\nDeseja usar este resultado como grafo atual? (s/n): ").strip().lower()
                if usar_resultado == 's':
                    grafo_atual = resultado
                    print("Grafo atual atualizado!")
                    
            else:
                print("Opção inválida! Tente novamente.")
                
        except ValueError:
            print("Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"Erro: {e}")
        
        input("\nPressione Enter para continuar...")

def main():
    """Função principal com menu de escolha"""
    print("\nEscolha uma opção:")
    print("1. Ver demonstração completa do programa")
    print("2. Usar as funções manualmente")
    print("3. Sair")
    
    while True:
        try:
            opcao = input("\nDigite sua opção: ").strip()
            
            if opcao == "1":
                demonstracao_completa()
                break
            elif opcao == "2":
                menu_interativo()
                break
            elif opcao == "3":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida! Digite 1,2 ou 3.")
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
