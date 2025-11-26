# 1)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[1:5])


# 2)
# slicing ში გამოაქვს რაიმე მითითებული ინდექსიდან მეორე ინდექსამდე მოცემული ელემენტები, indexing- ში კი ვუთითებთ კონკრეტულად და იმის მიხედვით გამოაქვს კონკრეტული ელემენტი


# 3)
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[1])

print(nums[1:3])
print(nums[2:])

nums.append(60)
print(nums)
nums.append(70)
print(nums)

nums[1] = 22
print(nums)
nums[2] = 31
print(nums)