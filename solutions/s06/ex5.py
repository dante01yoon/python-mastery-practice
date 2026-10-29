# 원인 1: best를 0에서 시작해서, 음수만 있으면 0이 그대로 남는다 → 첫 값에서 시작
# 원인 2: n < best 는 작은 값을 고른다 → n > best
def biggest(nums):
    best = nums[0]
    for n in nums:
        if n > best:
            best = n
    return best


print(biggest([-5, -2, -9]))  # -2
