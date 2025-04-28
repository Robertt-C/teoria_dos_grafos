from estruturas_dados import Grafo




if __name__ == "__main__":
    grafo = Grafo()
    
    # print(grafo.carrega_arquivo_csv("./dados/teste_arestas.csv"))
    # print("\n\n\n")
    # print(grafo.carrega_arquivo_csv("./dados/teste_nos.csv"))

    grafo.carrega_arquivos_nos_e_arestas(caminho_nos = "./dados/teste_nos.csv", caminho_arestas = "./dados/teste_arestas.csv")

    print(grafo.nos_adjacentes("Fantine"))
    print(grafo.grau_no("Fantine"))