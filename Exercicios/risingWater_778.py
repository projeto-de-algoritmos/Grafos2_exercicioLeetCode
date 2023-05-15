class Solucao:
    def nadarNaAgua(self, grid: List[List[int]]) -> int:
        # Tamanho do grid
        n = len(grid)

        # Criação de um conjunto para acompanhar os vértices visitados
        visitados = set()

        # Inicialização do conjunto de bordas com o primeiro vértice
        bordas = {(0, 0)}

        # Inicialização do custo mínimo com o valor do vértice inicial
        custo_minimo = grid[0][0]

        # Direções para percorrer o grid
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Executa o algoritmo de Prim
        while bordas:
            # Seleciona o vértice com o menor custo entre as bordas
            atual = min(bordas, key=lambda x: grid[x[0]][x[1]])
            bordas.remove(atual)
            visitados.add(atual)

            # Atualiza o custo mínimo
            custo_minimo = max(custo_minimo, grid[atual[0]][atual[1]])

            # Verifica se chegou ao destino
            if atual == (n - 1, n - 1):
                return custo_minimo

            # Relaxa as arestas adjacentes
            linha, coluna = atual
            for d in direcoes:
                nova_linha = linha + d[0]
                nova_coluna = coluna + d[1]

                # Verifica se a posição está dentro do grid
                if nova_linha < 0 or nova_linha >= n or nova_coluna < 0 or nova_coluna >= n:
                    continue

                # Verifica se o vértice já foi visitado
                if (nova_linha, nova_coluna) in visitados:
                    continue

                # Adiciona o vértice à borda e atualiza seu custo
                bordas.add((nova_linha, nova_coluna))

        # Se não encontrou um caminho até o destino, retorna -1
        return -1
