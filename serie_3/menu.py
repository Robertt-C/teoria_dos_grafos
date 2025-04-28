from estruturas_dados import Grafo

def criar_grafo_manual() -> Grafo:
    grafo = Grafo()
    numero_vertices = int(input("Digite o número de vértices: "))
    for _ in range(numero_vertices):
        no = input("Digite o nome do vértice: ")
        grafo.adiciona_no(no)

    while True:
        print("\n1 - Inserir aresta")
        print("2 - Encerrar inserção de arestas")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            origem = input("Digite o nó de origem: ")
            destino = input("Digite o nó de destino: ")
            grafo.adiciona_aresta((origem, destino))
        elif escolha == '2':
            break
        else:
            print("Opção inválida.")

    return grafo


def menu_operacoes(G: Grafo):
    while True:
        print("\nMenu de Operações:")
        print("1 - Número de vértices")
        print("2 - Número de arestas")
        print("3 - Vértices adjacentes de um nó")
        print("4 - Verificar existência de aresta entre dois nós")
        print("5 - Grau de um vértice")
        print("6 - Grau de todos os vértices")
        print("7 - Caminho simples entre dois vértices")
        print("8 - Ciclo que contém um vértice")
        print("9 - Verificar se um grafo é subgrafo de outro")
        print("10 - Encerrar operações")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print(f"Número de vértices: {G.numero_nos()}")

        elif escolha == '2':
            print(f"Número de arestas: {G.numero_arestas()}")

        elif escolha == '3':
            no = input("Digite o vértice: ")
            adjacentes = G.nos_adjacentes(no)
            print(f"Vértices adjacentes a {no}: {adjacentes}")

        elif escolha == '4':
            no1 = input("Digite o primeiro vértice: ")
            no2 = input("Digite o segundo vértice: ")
            existe = G.existe_aresta_entre(no1, no2)
            print("Existe aresta entre os nós." if existe else "Não existe aresta entre os nós.")

        elif escolha == '5':
            no = input("Digite o vértice: ")
            grau = G.grau_no(no)
            print(f"Grau do vértice {no}: {grau}")

        elif escolha == '6':
            graus = G.graus_nos()
            print("Graus dos vértices:")
            for no, grau in graus.items():
                print(f"{no}: {grau}")

        elif escolha == '7':
            no_inicio = input("Digite o vértice de início: ")
            no_fim = input("Digite o vértice de fim: ")
            caminho = G.caminho_simples_entre(no_inicio, no_fim)
            if caminho:
                print(f"Caminho encontrado: {caminho}")
            else:
                print("Não existe caminho entre os vértices.")

        elif escolha == '8':
            no = input("Digite o vértice: ")
            ciclo = G.ciclo_que_contem_no(no)
            if ciclo:
                print(f"Ciclo encontrado: {ciclo}")
            else:
                print("Não existe ciclo envolvendo o vértice.")

        elif escolha == '9':
            print("\n--- Verificar Subgrafo ---")
            print("1 - Digitar grafo G' manualmente")
            print("2 - Ler grafo G' de arquivo")
            escolha_subgrafo = input("Escolha uma opção: ")

            if escolha_subgrafo == '1':
                subG = criar_grafo_manual()

            elif escolha_subgrafo == '2':
                nome_arquivo_prime = input("Digite o nome do arquivo CSV para G': ")
                subG = Grafo()
                subG.cria_grafo_com_lista_adjacencia(nome_arquivo_prime)

            else:
                print("Opção inválida.")
                continue

            eh_subgrafo = G.e_subgrafo(subG.nos, subG.arestas)
            eh_subgrafo_inverso = subG.e_subgrafo(G.nos, G.arestas)

            if eh_subgrafo:
                print("G' é subgrafo de G.")
            elif eh_subgrafo_inverso:
                print("G é subgrafo de G'.")
            else:
                print("Nenhum é subgrafo do outro.")

        elif escolha == '10':
            print("Encerrando operações.")
            break

        else:
            print("Opção inválida.")


def menu_principal():
    G = Grafo()

    while True:
        print("\nMenu Principal:")
        print("1 - Digitar grafo")
        print("2 - Ler grafo de arquivo")
        print("3 - Encerrar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            G = criar_grafo_manual()
            print("\nGrafo criado com sucesso!")
            menu_operacoes(G)

        elif opcao == '2':
            nome_arquivo = input("Digite o nome do arquivo CSV: ")
            G.cria_grafo_com_lista_adjacencia(nome_arquivo)
            print("\nGrafo carregado com sucesso!")
            menu_operacoes(G)

        elif opcao == '3':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
