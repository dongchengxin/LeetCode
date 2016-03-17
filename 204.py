class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        count = 1
        isPrime = [True] * n
        for i in range(2,int(n ** 0.5) + 1):
            if not isPrime[i]:
                continue
            for j in range(i ** 2,n,i):
                isPrime[j] = False
        for i in range(3,n,2):
            if isPrime[i]:
                count += 1
        return count