class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = cows = 0
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                bulls += 1
                secret = secret[:i] + secret[i + 1:]
                guess = guess[:i] + guess[i + 1:]
            else:
                i += 1
        for c in guess:
            if c in secret:
                cows += 1
                i = secret.find(c)
                secret = secret[:i] + secret[i + 1:]
        return str(bulls) + 'A' + str(cows) + 'B'

secret = '1123'
guess = '0111'
s = Solution()
print s.getHint(secret,guess)