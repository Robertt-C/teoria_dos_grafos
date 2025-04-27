from estruturas_dados import Grafo




if __name__ == "__main__":
    grafo = Grafo()
    
    # grafo.carrega_arquivo_nos("./dados/nos.csv")
    # grafo.carrega_arquivo_arestas("./dados/arestas.csv")

    # grafo.print_nos()
    # grafo.print_arestas()
    
    # print("\n\n")
    # grafo.cria_matriz_adjacencia()
    # grafo.print_matriz_adjacencia()
    

    # print("\n\n")
    # grafo.cria_matriz_incidencia()
    # grafo.print_matriz_incidencia()

    # print("\n\n")
    # grafo.cria_lista_adjacencia()
    # grafo.print_lista_adjacencia()

    # print(grafo.carrega_arquivo_csv("./dados/matriz_adjacencia.csv"))

    # grafo.cria_grafo_com_matriz_adjacencia("./dados/matriz_adjacencia.csv", ["A", "B", "C"])
    # grafo.print_nos()
    # grafo.print_arestas()

    # grafo.cria_grafo_com_matriz_incidencia("./dados/matriz_incidencia.csv", ["A", "B", "C"])
    # grafo.print_nos()
    # grafo.print_arestas()
    # grafo.cria_matriz_adjacencia()
    # grafo.print_matriz_adjacencia()

    # grafo.cria_grafo_com_lista_adjacencia("./dados/lista_adjacencia.csv")
    # grafo.print_nos()
    # grafo.print_arestas()
    # print()
    # grafo.cria_lista_adjacencia()
    # grafo.print_lista_adjacencia()
    # print()
    # grafo.cria_matriz_adjacencia()
    # grafo.print_matriz_adjacencia()
    # print()
    # grafo.cria_matriz_incidencia()
    # grafo.print_matriz_incidencia()

    grafo.carrega_arquivo_nos("./dados/nos.csv")
    grafo.carrega_arquivo_arestas("./dados/arestas.csv")

    grafo.print_nos()
    grafo.print_arestas()
    # print(grafo.numero_nos())
    # print(grafo.numero_arestas())

    # print(grafo.nos_adjacentes("A"))

    # grafo.print_lista_adjacencia()

    # print(grafo.existe_aresta_entre("A", "S"))
    # print(grafo.grau_no("A"))
    # print(grafo.graus_nos())
    # print(grafo.caminho_simples_entre("A", "A"))
    # print(grafo.ciclo_que_contem_no("A"))

    print(grafo.e_subgrafo(nos_subgrupo = set(["A", "B", "C"]), arestas_subgrupo = set([("A", "B", '1'), ("B", "C", '1')])))