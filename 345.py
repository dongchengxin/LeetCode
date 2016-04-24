class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        pattern = re.compile(r'[aeiou]', re.I)
        vowels = re.findall(pattern, s)
        return re.sub(pattern, lambda m: vowels.pop(), s)
