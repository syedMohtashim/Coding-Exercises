# ------------------------------------------------------------------------------
# ********************************* { DAY 04 } *********************************
# ------------------------------------------------------------------------------

# QUESTION-1 : TWO SUM PROBLEM . https://leetcode.com/problems/two-sum/

nums = [2,7,11,15]
target = 9
def _2_sum(ls, target):
	hash_map = dict()
	for i in range(len(ls)):
		comp = target - nums[i]
		if nums[i] in hash_map:
			return [hash_map[nums[i]], i]
		else:
			hash_map[comp] = i

a = _2_sum(nums, target)
print(a)