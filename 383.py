class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ran = {}
        mag = {}
        for i in ransomNote:
            ran[i] = ran.setdefault(i, 0) + 1
        for i in magazine:
            mag[i] = mag.setdefault(i, 0) + 1
        for key in ran:
            if key not in mag or ran[key] > mag[key]:
                return False
        return True
