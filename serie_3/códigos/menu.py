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
            origem = input("Digite o primeiro nó: ")
            destino = input("Digite o segundo nó: ")
            peso = input("Digite um peso para esta aresta: ")
            grafo.adiciona_aresta((origem, destino, peso))
        elif escolha == '2':
            break
        else:
            print("Opção inválida.")

    return grafo

def ler_arquivos_de_grafos(G: Grafo):
    nome_arquivo_nos = input("Digite o nome do arquivo contendo nos: ")
    nome_arquivo_arestas = input("Digite o nome do arquivo contendo arestas: ")
    G.carrega_arquivos_nos_e_arestas(nome_arquivo_nos, nome_arquivo_arestas)
    print("\nGrafo carregado com sucesso!")

def menu_operacoes(G: Grafo):
    while True:
        print("\nMenu de Operações:")
        print("1 - Mostrar vértices")
        print("2 - Mostrar arestas")
        print("3 - Número de vértices")
        print("4 - Número de arestas")
        print("5 - Vértices adjacentes de um nó")
        print("6 - Verificar existência de aresta entre dois nós")
        print("7 - Grau de um vértice")
        print("8 - Grau de todos os vértices")
        print("9 - Caminho simples entre dois vértices")
        print("10 - Ciclo que contém um vértice")
        print("11 - Verificar se um grafo é subgrafo de outro")
        print("12 - Verificar se dois grafos são subgrafo de outro e se são disjuntos")
        print("13 - Mostrar 5 subgrafos")
        print("14 - Encerrar operações")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            G.mostrar_vertices()

        elif escolha == '2':
            G.mostrar_arestas()

        elif escolha == '3':
            print(f"Número de vértices: {G.numero_nos()}")

        elif escolha == '4':
            print(f"Número de arestas: {G.numero_arestas()}")

        elif escolha == '5':
            no = input("Digite o vértice: ")
            adjacentes = G.nos_adjacentes(no)
            print(f"Vértices adjacentes a {no}: {adjacentes}")

        elif escolha == '6':
            no1 = input("Digite o primeiro vértice: ")
            no2 = input("Digite o segundo vértice: ")
            existe = G.existe_aresta_entre(no1, no2)
            print("Existe aresta entre os nós." if existe else "Não existe aresta entre os nós.")

        elif escolha == '7':
            no = input("Digite o vértice: ")
            grau = G.grau_no(no)
            print(f"Grau do vértice {no}: {grau}")

        elif escolha == '8':
            graus = G.graus_nos()
            print("Graus dos vértices:")
            for no, grau in graus.items():
                print(f"{no}: {grau}")

        elif escolha == '9':
            no_inicio = input("Digite o vértice de início: ")
            no_fim = input("Digite o vértice de fim: ")
            caminho = G.caminho_simples_entre(no_inicio, no_fim)
            if caminho:
                print(f"Caminho encontrado: {caminho}")
            else:
                print("Não existe caminho entre os vértices.")

        elif escolha == '10':
            no = input("Digite o vértice: ")
            ciclo = G.ciclo_que_contem_no(no)
            if ciclo:
                print(f"Ciclo encontrado: {ciclo}")
            else:
                print("Não existe ciclo envolvendo o vértice.")

        elif escolha == '11':
            print("\n--- Verificar Subgrafo ---")
            print("1 - Digitar grafo G' manualmente")
            print("2 - Ler grafo G' de arquivo")
            escolha_subgrafo = input("Escolha uma opção: ")

            if escolha_subgrafo == '1':
                subG = criar_grafo_manual()

            elif escolha_subgrafo == '2':
                subG = Grafo()
                ler_arquivos_de_grafos(subG)
                print(subG.arestas)
                print(subG.nos)

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

        elif escolha == '12':
            print("\n--- Verificar Subgrafos ---")
            print("1 - Digitar grafo G1' manualmente")
            print("2 - Ler grafo G1' de arquivo")
            escolha_subgrafo = input("Escolha uma opção: ")

            if escolha_subgrafo == '1':
                subG1 = criar_grafo_manual()

            elif escolha_subgrafo == '2':
                subG1 = Grafo()
                ler_arquivos_de_grafos(subG1)
                print(subG1.arestas)
                print(subG1.nos)

            else:
                print("Opção inválida.")
                continue

            print("\n1 - Digitar grafo G2' manualmente")
            print("2 - Ler grafo G2' de arquivo")
            escolha_subgrafo = input("Escolha uma opção: ")

            if escolha_subgrafo == '1':
                subG2 = criar_grafo_manual()

            elif escolha_subgrafo == '2':
                subG2 = Grafo()
                ler_arquivos_de_grafos(subG2)
                print(subG2.arestas)
                print(subG2.nos)

            else:
                print("Opção inválida.")
                continue

            eh_subgrafo_1 = G.e_subgrafo(subG1.nos, subG1.arestas)
            eh_subgrafo_2 = G.e_subgrafo(subG2.nos, subG2.arestas)
            eh_disjunto_aresta = subG1.e_disjunto_aresta(subG2.arestas)
            eh_disjunto_vertice = subG1.e_disjunto_vertice(subG2.nos)

            if eh_subgrafo_1 and eh_subgrafo_2:
                print("G1' e G2' são subgrafos de G.")
                if eh_disjunto_aresta:
                    print("G1' e G2' são disjuntos em arestas")
                if eh_disjunto_vertice:
                    print("G1' e G2' são disjuntos em vértices")
                else:
                    print("G1' e G2' não são disjuntos")
            else:
                if eh_subgrafo_1:
                    print("G1' é subgrafo de G, mas G2' não é subgrafo de G.")
                elif eh_subgrafo_2:
                    print("G2' é subgrafo de G, mas G1' não é subgrafo de G.")
                else:
                    print("Nenhum é subgrafo de G.")

        elif escolha == '13':
            G.mostrar_cinco_subgrafos()

        elif escolha == '14':
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
            ler_arquivos_de_grafos(G)
            menu_operacoes(G)

        elif opcao == '3':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
