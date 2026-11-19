class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i: [] for i in range(numCourses)}
        seen = set()
        done = set()
        res = []

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False
            if crs in done:
                return True
            seen.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            prereq[crs] = []
            done.add(crs)
            res.append(crs)
            return True 

        for crs in range(numCourses):
            if not dfs(crs):
                return [] 
        return res
