from collections import defaultdict

class Solution:
    def integerReplacement(self, n: int) -> int:
        def count_ops(n):
            if n == 1:
                return 0
            if cache[n]:
                return cache[n]
            
            if n % 2 == 0:
                cache[n//2] = count_ops(n//2)
                cache[n] = 1 + cache[n//2]
                return cache[n]
            
            cache[n+1] = count_ops(n+1)
            cache[n-1] = count_ops(n-1)
            cache[n] = 1 + min(cache[n+1], cache[n-1])
            return cache[n]
        
        cache = defaultdict(int)
        
        return count_ops(n)
        
        