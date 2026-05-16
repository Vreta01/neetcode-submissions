class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def search(i,target):
            if (
                not(0<=i<len(s2)) or
                s2[i] not in target
            ):
                return False
            target.remove(s2[i])
            if len(target) == 0:
                return True
            i += 1
            if not search(i,target):
                return False
            return True
        target = list(s1)
        for i in range(len(s2)):
            if s2[i] in target:
                if search(i,target.copy()):
                    return True
        return False
