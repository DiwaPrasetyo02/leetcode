from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        # Split the nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # Create separate sets for negatives and positives for O(1) lookup time
        N, P = set(n), set(p)

        # If there is at least one zero in the list, add all cases where -num exists in N and num exists in P
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))
            # Check for the special case where there are at least three zeros
            if len(z) >= 3:
                res.add((0, 0, 0))

        # For all pairs of negative numbers (-3, -1), check to see if their complement exists in the positive set
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # For all pairs of positive numbers (1, 1), check to see if their complement exists in the negative set
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        # Convert the set of tuples to a list of lists and sort the results lexicographically
        return sorted([list(triplet) for triplet in res])
