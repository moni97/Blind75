def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      adjacency = {a: [] for a in range(numCourses)}
      for c, pre in prerequisites:
          adjacency[c].append(pre)
      visited = set()
      def dfs(crs):
          # print("crs: ", crs)
          if crs in visited:
              return False
          if adjacency[crs] == []:
              return True
          visited.add(crs)
          for a in adjacency[crs]:
              # print("adj: ", a)
              if not dfs(a): return False
          visited.remove(crs)
          adjacency[crs] = []
          return True
      for crs in range(numCourses):
          if not dfs(crs): return False
      return True
