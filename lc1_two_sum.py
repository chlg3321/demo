# 暴力法
class Solution:
    # Brute Force
    # @爱学习的饲养员
    # N is the size of nums
    # Time Complexity: O(N^2)
    # Space COmplexity: O(1)
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    def twoSum(self, nums, target) :
        result = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    result.append(i);
                    result.append(j);
                    return result
solution = Solution()
result = solution.twoSum([15,11,2,7],9)
print(result)

#哈希法
class Solution:
    # Hash Table
    # @爱学习的饲养员
    # N is the size of nums
    # Time Complexity: O(N)
    # Space COmplexity: O(N)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        result = []
        mapping = {}
        for i in range(0, len(nums)):
            mapping[nums[i]] = i
        for j in range(0, len(nums)):
            diff = target - nums[j]
            if (diff in mapping and mapping[diff] != j):
                result.append(j);
                result.append(mapping[diff]);
                return result

