class Solution:
    def permute(self, nums):
        res = []
        self.perm(nums, 0, res)
        return res

    def perm(self, lst, i, r):
        if i == len(lst):
            r.append(lst[:])
        else:
            for j in range(i, len(lst)):
                lst[i], lst[j] = lst[j], lst[i]
                print(lst)
                self.perm(lst, i + 1, r)
                lst[i], lst[j] = lst[j], lst[i]


if __name__ == "__main__":
    lst = Solution().permute([1, 2, 3])
    print(lst)