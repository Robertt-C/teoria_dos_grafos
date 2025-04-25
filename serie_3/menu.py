from estruturas_dados import Grafo




if __name__ == "__main__":
    grafo = Grafo()
    
    grafo.carrega_arquivo_nos("./dados/nos.csv")
    grafo.carrega_arquivo_arestas("./dados/arestas.csv")

    grafo.print_nos()
    grafo.print_arestas()
    
    print("\n\n")
    grafo.cria_matriz_adjacencia()
    grafo.print_matriz_adjacencia()
    

    print("\n\n")
    grafo.cria_matriz_incidencia()
    grafo.print_matriz_incidencia()

    print("\n\n")
    grafo.cria_lista_adjacencia()
    grafo.print_lista_adjacencia()