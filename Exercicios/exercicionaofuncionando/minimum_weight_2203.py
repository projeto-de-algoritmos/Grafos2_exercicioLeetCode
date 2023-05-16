import heapq


class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src1: int
        :type src2: int
        :type dest: int
        :rtype: int
        """

        graph = {}

        for edge in edges:
          source = edge[0]
          destination = edge[1]
          weight = edge[2]

          if source not in graph:
            graph[source] = {}

          if destination not in graph:
            graph[destination] = {}

          graph[source][destination] = weight
        def dijkstra(graph, start, end):
          distances = {node: float('inf') for node in graph}
          distances[start] = 0
          queue = [(0, start)]
    
          while queue:
              current_distance, current_node = heapq.heappop(queue)
        
              if current_distance > distances[current_node]:
                continue
        
              if current_node == end:
                return distances[end]
        
              for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
    
          return -1
        caminho1 =dijkstra(graph, src1, src2)
        caminho2 =dijkstra(graph, src2, dest)

        if  caminho1 == -1 or caminho2 ==-1:
            return -1
        return caminho1+caminho2