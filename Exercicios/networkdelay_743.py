import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

    
        graph = [[] for i in range(n + 1)]
        for u, v, w in times:
          graph[u].append((v, w))

    
        pq = [(0, k)]

   
        while pq:   
             d, u = heapq.heappop(pq)
             if d > dist[u]:
                continue
             for v, w in graph[u]:  #ver os vizinhos
                 new_dist = dist[u] + w #calcular novo distancia
                 if new_dist < dist[v]:     #se novo distancia foi menor
                         dist[v] = new_dist 
                         heapq.heappush(pq, (new_dist, v)) #adcionar novo distancia na fila

  
        if any(d == float('inf') for d in dist[1:]):
            return -1


        return max(dist[1:])