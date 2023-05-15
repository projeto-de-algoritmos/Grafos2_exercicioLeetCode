class Solucao:
    def encontrarCidade(self, n: int, arestas: List[List[int]], distanciaLimite: int) -> int:
        # Cria um dicionário com as listas de adjacência do grafo
        grafo = {i: [] for i in range(n)}
        for u, v, w in arestas:
            grafo[u].append((v, w))
            grafo[v].append((u, w))

        # Função para o algoritmo de Dijkstra
        def dijkstra(inicio):
            # Cria uma lista com a distância mínima de cada nó até o início
            dist = [float('inf')] * n
            dist[inicio] = 0

            # Cria um conjunto para armazenar os nós não visitados
            naoVisitados = set(range(n))

            while naoVisitados:
                # Encontra o nó com a menor distância
                atual = min(naoVisitados, key=lambda x: dist[x])
                naoVisitados.remove(atual)

                # Para cada vizinho não visitado, atualiza a distância se for menor
                for vizinho, peso in grafo[atual]:
                    if vizinho in naoVisitados:
                        nova_dist = dist[atual] + peso
                        if nova_dist < dist[vizinho]:
                            dist[vizinho] = nova_dist

            # Conta quantos nós estão a uma distância menor ou igual a distanciaLimite
            contagem = 0
            for d in dist:
                if d <= distanciaLimite:
                    contagem += 1
            return contagem

        # Inicializa a menor contagem de vizinhos e o índice correspondente
        menor_contagem = float('inf')
        menor_indice = -1

        # Testa o algoritmo de Dijkstra para cada nó do grafo
        for i in range(n):
            contagem = dijkstra(i)
            if contagem <= menor_contagem:
                menor_contagem = contagem
                menor_indice = i

        return menor_indice
