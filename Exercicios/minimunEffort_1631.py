class Solution:
    def minimumEffortPath(self, alturas: List[List[int]]) -> int:
            m = len(alturas)
            n = len(alturas[0])

            direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            fila_prioridade = [(0, 0, 0)]  # (esforço até o nó, linha, coluna)
            esforco = {(0, 0): 0} # Dicionário para armazenar o esforço mínimo para cada nó

            while fila_prioridade:
                _, linha, coluna = heapq.heappop(fila_prioridade)

                if linha == m - 1 and coluna == n - 1:
                    return esforco[(linha, coluna)] # Chegamos ao destino, retorna o esforço mínimo

                for d in direcoes:
                    nova_linha = linha + d[0]
                    nova_coluna = coluna + d[1]

                    if nova_linha < 0 or nova_linha >= m or nova_coluna < 0 or nova_coluna >= n:
                        continue # Posição fora dos limites do grid, ignorar

                    diferenca = abs(alturas[linha][coluna] - alturas[nova_linha][nova_coluna]) # Calcula a diferença de altura

                    novo_esforco = max(esforco[(linha, coluna)], diferenca) # Esforço para chegar ao novo nó

                    if (nova_linha, nova_coluna) not in esforco or novo_esforco < esforco[(nova_linha, nova_coluna)]:
                        esforco[(nova_linha, nova_coluna)] = novo_esforco # Atualiza o esforço mínimo para o novo nó
                        heapq.heappush(fila_prioridade, (novo_esforco, nova_linha, nova_coluna)) # Insere o novo nó na fila de prioridade

            return -1

