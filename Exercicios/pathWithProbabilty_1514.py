import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        graph = [[] for i in range(n)]
    
        for i, (a, b) in enumerate(edges):
            p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))
    
    # inicializar distnacas com infinidade negativo 
        distances = [-float('inf')] * n
        distances[start] = 1.0
    
# fil de priodade 
        pq = [(-1.0, start)]
    
        while pq:
             prob, node = heapq.heappop(pq)  #tirar o menor 
             prob = -prob
        
             if prob < distances[node]:    #pular no se caminho mais curto com maior probabilidade já foi encontrado
                continue
        #Explore os vizinhos do no atual
             for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
            
                if new_prob > distances[neighbor]:
                    distances[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
    
        return distances[end] if distances[end] > -float('inf') else 0.0