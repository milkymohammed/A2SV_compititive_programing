class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        B = [val**2 for val in A]

        l, r = 0, len(B) - 1
        results = []

        while l <= r:
            if B[l] > B[r]:
                results.append(B[l])
                l += 1
            else:
                results.append(B[r])
                r -= 1

        return results[::-1]
