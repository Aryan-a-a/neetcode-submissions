class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        seen = set()

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False
            if prereq[crs] == []:
                return True
            seen.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            prereq[crs] = []
            return True 

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
