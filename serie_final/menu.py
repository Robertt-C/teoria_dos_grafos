from algoritmos import Grafo, e_arvore, e_subgrafo_arvore, e_arvore_abrangencia, encontrar_centros, excentricidades, recomendar_receitas_por_ingredientes
from algoritmos import grafos_isomorfos, is_connected, is_eulerian, has_hamiltonian_cycle
from algoritmos import graph_union, graph_intersection, graph_symmetric_difference
from algoritmos import remove_vertex, remove_edge, merge_vertices
from algoritmos import raio, gerar_arvore_abrangencia, gerar_k_arvores_abrangencia
from algoritmos import distancia_entre_arvores, arvore_central




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
            peso = input("Digite um peso para esta aresta (ou pressione Enter para nenhum): ")
            if peso:
                grafo.adiciona_aresta((origem, destino, peso))
            else:
                grafo.adiciona_aresta((origem, destino))
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

def menu_operacoes_basicas(G: Grafo):
    while True:
        print("\nMenu de Operações Básicas:")
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
        print("14 - Exportar arestas para CSV")
        print("15 - Voltar ao menu principal")
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
            subG1 = criar_grafo_manual()
            subG2 = criar_grafo_manual()

            eh_subgrafo_1 = G.e_subgrafo(subG1.nos, subG1.arestas)
            eh_subgrafo_2 = G.e_subgrafo(subG2.nos, subG2.arestas)
            eh_disjunto_aresta = subG1.e_disjunto_aresta(subG2.arestas)
            eh_disjunto_vertice = subG1.e_disjunto_vertice(subG2.nos)

            if eh_subgrafo_1 and eh_subgrafo_2:
                print("\nG1' e G2' são subgrafos de G.")
                if eh_disjunto_aresta:
                    print("G1' e G2' são disjuntos em arestas")
                if eh_disjunto_vertice:
                    print("G1' e G2' são disjuntos em vértices")
                else:
                    print("G1' e G2' não são disjuntos")
            else:
                if eh_subgrafo_1:
                    print("\nG1' é subgrafo de G, mas G2' não é subgrafo de G.")
                elif eh_subgrafo_2:
                    print("\nG2' é subgrafo de G, mas G1' não é subgrafo de G.")
                else:
                    print("\nNenhum é subgrafo de G.")
        elif escolha == '13':
            G.mostrar_cinco_subgrafos()
        elif escolha == '14':
            caminho_arquivo = input("Digite o caminho para salvar o arquivo CSV (ex: arestas_export.csv): ")
            G.exportar_arestas_csv(caminho_arquivo)
            print(f"Arquivo salvo com sucesso em: {caminho_arquivo}")
        elif escolha == '15':
            return
        else:
            print("Opção inválida.")

def menu_operacoes_grafos_isomorfos(G: Grafo):
    print("\n--- Verificar Isomorfismo ---")
    print("Criando grafo G' para comparação:")
    G_prime = criar_grafo_manual()
    
    if grafos_isomorfos(G, G_prime):
        print("Os grafos G e G' são isomorfos.")
    else:
        print("Os grafos G e G' não são isomorfos.")

def menu_operacoes_conectividade(G: Grafo):
    print("\n--- Verificar Propriedades ---")
    
    if is_connected(G):
        print("O grafo G é conexo.")
    else:
        print("O grafo G não é conexo.")
        
    if is_eulerian(G):
        print("O grafo G é euleriano.")
    else:
        print("O grafo G não é euleriano.")
        
    if has_hamiltonian_cycle(G):
        print("O grafo G possui ciclo hamiltoniano.")
    else:
        print("O grafo G não possui ciclo hamiltoniano.")

def menu_operacoes_conjuntos(G: Grafo):
    print("\n--- Operações de Conjunto ---")
    print("Criando grafo G' para operações:")
    G_prime = criar_grafo_manual()
    
    while True:
        print("\nEscolha a operação:")
        print("1 - União")
        print("2 - Interseção")
        print("3 - Diferença Simétrica")
        print("4 - Voltar")
        op = input("Opção: ").strip()
        
        if op == "1":
            resultado = graph_union(G, G_prime)
            print("\nResultado da União:")
            resultado.mostrar_vertices()
            resultado.mostrar_arestas()
        elif op == "2":
            resultado = graph_intersection(G, G_prime)
            print("\nResultado da Interseção:")
            resultado.mostrar_vertices()
            resultado.mostrar_arestas()
        elif op == "3":
            resultado = graph_symmetric_difference(G, G_prime)
            print("\nResultado da Diferença Simétrica:")
            resultado.mostrar_vertices()
            resultado.mostrar_arestas()
        elif op == "4":
            return
        else:
            print("Opção inválida!")
        
        usar_resultado = input("\nDeseja usar este resultado como grafo atual? (s/n): ").strip().lower()
        if usar_resultado == 's':
            return resultado
    
    return G

def menu_operacoes_modificacao(G: Grafo):
    while True:
        print("\n--- Modificação de Grafo ---")
        print("1 - Remover vértice")
        print("2 - Remover aresta")
        print("3 - Fundir vértices")
        print("4 - Voltar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            vertice = input("Digite o vértice a ser removido: ")
            novo_grafo = remove_vertex(G, vertice)
            if novo_grafo:
                print("Vértice removido com sucesso!")
                return novo_grafo
        elif escolha == '2':
            u = input("Digite o primeiro vértice da aresta: ")
            v = input("Digite o segundo vértice da aresta: ")
            novo_grafo = remove_edge(G, (u, v))
            if novo_grafo:
                print("Aresta removida com sucesso!")
                return novo_grafo
        elif escolha == '3':
            vi = input("Digite o primeiro vértice: ")
            vj = input("Digite o segundo vértice: ")
            novo_grafo = merge_vertices(G, vi, vj)
            if novo_grafo:
                print("Vértices fundidos com sucesso!")
                return novo_grafo
        elif escolha == '4':
            return G
        else:
            print("Opção inválida!")
    
    return G

def menu_operacoes_arvores(G: Grafo):
    while True:
        print("\n--- Operações com Árvores ---")
        print("1 - Verificar se o grafo é uma árvore")
        print("2 - Verificar árvore de abrangência")
        print("3 - Encontrar centro(s) da árvore")
        print("4 - Calcular excentricidades")
        print("5 - Voltar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            if e_arvore(G):
                print("O grafo G é uma árvore.")
            else:
                print("O grafo G não é uma árvore.")
        elif escolha == '2':
            print("Criando subgrafo A para verificar árvore de abrangência:")
            A = criar_grafo_manual()
            if e_arvore_abrangencia(G, A):
                print("A é uma árvore de abrangência de G.")
            else:
                if e_subgrafo_arvore(G, A):
                    print("A é subgrafo árvore de G, mas não contém todos os vértices.")
                else:
                    print("A não é subgrafo árvore de G.")
        elif escolha == '3':
            if e_arvore(G):
                centros = encontrar_centros(G)
                print(f"Centro(s) da árvore: {centros}")
            else:
                print("O grafo G não é uma árvore. Não é possível encontrar centro(s).")
        elif escolha == '4':
            if e_arvore(G):
                exc = excentricidades(G)
                print("Excentricidades:")
                for vertice, valor in exc.items():
                    print(f"{vertice}: {valor}")
            else:
                print("O grafo G não é uma árvore. Não é possível calcular excentricidades.")
        elif escolha == '5':
            return
        else:
            print("Opção inválida!")

def menu_operacoes_arvores_avancadas(G: Grafo):
    while True:
        print("\n--- Operações Avançadas com Árvores ---")
        print("1 - Calcular o raio de uma árvore")
        print("2 - Gerar uma árvore de abrangência")
        print("3 - Gerar k árvores de abrangência usando trocas cíclicas")
        print("4 - Calcular distância entre duas árvores")
        print("5 - Determinar a árvore central")
        print("6 - Voltar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            if e_arvore(G):
                r = raio(G)
                print(f"O raio da árvore é: {r}")
            else:
                print("O grafo atual não é uma árvore. Deseja criar uma árvore?")
                resp = input("(s/n): ").lower()
                if resp == 's':
                    arvore = criar_grafo_manual()
                    if e_arvore(arvore):
                        r = raio(arvore)
                        print(f"O raio da árvore é: {r}")
                    else:
                        print("O grafo criado não é uma árvore.")
                
        elif escolha == '2':
            arvore = gerar_arvore_abrangencia(G)
            if arvore.nos:
                print("\nÁrvore de abrangência gerada:")
                arvore.mostrar_vertices()
                arvore.mostrar_arestas()
                
                salvar = input("Deseja salvar esta árvore como grafo atual? (s/n): ").lower()
                if salvar == 's':
                    return arvore
            
        elif escolha == '3':
            try:
                k = int(input("Digite o número de árvores de abrangência a gerar: "))
                if k <= 0:
                    print("Por favor, digite um número positivo.")
                    continue
                    
                print("Gerando árvores, por favor aguarde...")
                arvores = gerar_k_arvores_abrangencia(G, k)
                
                print(f"\nForam geradas {len(arvores)} árvores de abrangência:")
                for i, arvore in enumerate(arvores):
                    print(f"\nÁrvore {i+1}:")
                    arvore.mostrar_arestas()
                    
                salvar = input("\nDeseja salvar alguma das árvores como grafo atual? (1-{}/n): ".format(len(arvores)))
                try:
                    idx = int(salvar)
                    if 1 <= idx <= len(arvores):
                        return arvores[idx-1]
                except:
                    pass
            except ValueError:
                print("Por favor, digite um número válido.")
                
        elif escolha == '4':
            print("Calculando distância entre duas árvores.")
            print("Criando primeira árvore:")
            A1 = criar_grafo_manual()
            
            if not e_arvore(A1):
                print("O primeiro grafo não é uma árvore.")
                continue
                
            print("\nCriando segunda árvore:")
            A2 = criar_grafo_manual()
            
            if not e_arvore(A2):
                print("O segundo grafo não é uma árvore.")
                continue
                
            dist = distancia_entre_arvores(A1, A2)
            if dist >= 0:
                print(f"A distância entre as árvores é: {dist}")
                
        elif escolha == '5':
            num = 10
            try:
                num = int(input("Digite o número de árvores a considerar (padrão: 10): ") or 10)
            except:
                pass
                
            print("Calculando árvore central, por favor aguarde...")
            arvore = arvore_central(G, num)
            if arvore and arvore.nos:
                print("\nÁrvore central encontrada:")
                arvore.mostrar_arestas()
                excs = excentricidades(arvore)
                diametro = max(excs.values()) if excs else 0
                print(f"Diâmetro da árvore central: {diametro}")
                
                salvar = input("Deseja salvar esta árvore como grafo atual? (s/n): ").lower()
                if salvar == 's':
                    return arvore
            else:
                print("Não foi possível determinar uma árvore central.")
                
        elif escolha == '6':
            return G
        else:
            print("Opção inválida!")
    
    return G

def menu_recomendacao_receitas(G: Grafo):
    """Menu para recomendação de receitas baseada nos ingredientes disponíveis."""
    print("\n--- Recomendação de Receitas ---")
    print("Digite os ingredientes disponíveis separados por vírgula:")
    
    ingredientes_input = input("> ")
    ingredientes = [i.strip() for i in ingredientes_input.split(',')]
    
    if not ingredientes:
        print("Nenhum ingrediente fornecido.")
        return
    
    try:
        top_n = int(input("Quantidade de receitas para recomendar (padrão: 5): ") or "5")
    except ValueError:
        top_n = 5
    
    recomendacoes = recomendar_receitas_por_ingredientes(G, ingredientes, top_n)
    
    if recomendacoes:
        print("\nReceitas recomendadas com base nos seus ingredientes:")
        print("----------------------------------------------------")
        
        for i, (receita, porcentagem, faltantes) in enumerate(recomendacoes, 1):
            print(f"{i}. {receita}")
            print(f"   Compatibilidade: {porcentagem:.1f}%")
            
            if faltantes:
                print(f"   Ingredientes faltantes ({len(faltantes)}): {', '.join(faltantes)}")
            else:
                print("   Você tem todos os ingredientes necessários!")
            print()
    else:
        print("Não foi possível encontrar receitas compatíveis com os ingredientes informados.")

def menu_principal():
    G = Grafo()
    
    while True:
        print("\n========== SISTEMA DE GRAFOS ==========")
        print("1 - Criar grafo manualmente")
        print("2 - Ler grafo de arquivo")
        print("3 - Operações básicas com grafos")
        print("4 - Verificar isomorfismo entre grafos")
        print("5 - Verificar conectividade e ciclos")
        print("6 - Operações de conjunto com grafos")
        print("7 - Modificar grafo")
        print("8 - Operações com árvores")
        print("9 - Operações avançadas com árvores")
        print("10 - Recomendação de receitas")
        print("0 - Sair")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '0':
            print("Encerrando o programa...")
            break
        elif escolha == '1':
            G = criar_grafo_manual()
            print("\nGrafo criado com sucesso!")
        elif escolha == '2':
            ler_arquivos_de_grafos(G)
        elif escolha == '3':
            if not G.nos:
                print("Grafo vazio! Por favor, crie um grafo primeiro.")
                continue
            menu_operacoes_basicas(G)
        elif escolha == '4':
            if not G.nos:
                print("Grafo vazio! Por favor, crie um grafo primeiro.")
                continue
            menu_operacoes_grafos_isomorfos(G)
        elif escolha == '5':
            if not G.nos:
                print("Grafo vazio! Por favor, crie um grafo primeiro.")
                continue
            menu_operacoes_conectividade(G)
        elif escolha == '6':
            if not G.nos:
                print("Grafo vazio! Por favor, crie um grafo primeiro.")
                continue
            resultado = menu_operacoes_conjuntos(G)
            if resultado != G:
                G = resultado
                print("Grafo atual atualizado com o resultado da operação.")
        elif escolha == '7':
            if not G.nos:
                print("Grafo vazio! Por favor, crie um grafo primeiro.")
                continue
            G = menu_operacoes_modificacao(G)
        elif escolha == '8':
            if not G.nos:
                print("Grafo vazio! Por favor, crie um grafo primeiro.")
                continue
            menu_operacoes_arvores(G)
        elif escolha == '9':
            if not G.nos:
                print("Grafo vazio! Por favor, crie um grafo primeiro.")
                continue
            G = menu_operacoes_arvores_avancadas(G)
        elif escolha == '10':
            if not G.nos:
                print("Carregue um grafo de receitas primeiro (opção 2).")
                continue
            menu_recomendacao_receitas(G)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
