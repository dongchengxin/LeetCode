class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        l1 = len(words[0])
        l2 = len(words)
        l3 = len(s)
        res = []
        d = {}
        for word in words:
            d[word] = d.setdefault(word,0) + 1
        if l3 < l1*l2:
            return res
        for j in range(l1):
            l4 = 0
            temp = []
            tmp = {}
            for i in range(j,l3,l1):
                if l3-i < (l2-l4)*l1:
                    break
                word = s[i:i+l1]
                if word in words:
                    temp.append(word)
                    l4 += 1
                    tmp[word] = tmp.setdefault(word,0) + 1
                    while tmp[word] > d[word]:
                        tmp[temp.pop(0)] -= 1
                        l4 -= 1
                    if l4 == l2:
                        res.append(i-(l2-1)*l1)
                else:
                    tmp.clear()
                    temp = []
                    l4 = 0
        return res