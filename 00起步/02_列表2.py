# # 2开始，达到“5”这个值停止
# for value in range(2, 5):
#     print(value)

# nums_range = range(2, 5)
# nums_list = list(nums_range)
# print(nums_range)
# print(nums_list)

# for value in range(2, 11, 2):
#     print(value)

# nums = list(range(2, 10, 2))
# print(nums)
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# squares = [value**2 for value in range(1, 11)]
# print(squares)

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:2])
print(players[2:])
# 创建副本
players2 = players[:]
print(players2)
