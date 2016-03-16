class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        s1 = (C - A) * (D - B)
        s2 = (G - E) * (H - F)
        if A >= G or B >= H or C <= E or D <= F:
            s3 = 0
        else:
            I = max(A,E)
            J = max(B,F)
            K = min(C,G)
            L = min(D,H)
            s3 = (K - I) * (L - J)
        return s1 + s2 - s3