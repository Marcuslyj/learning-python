# # 关键字with在不再需要访问文件后将其关闭
# with open('text_files/pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# filename = 'text_files/pi_digits.txt'
# # with open(filename) as file_object:
# #     for line in file_object:
# #         print(line.rstrip())

# with open(filename) as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         print(line.rstrip())

# filename = 'text_files/programming.txt'
# # w表示以写入的方式打开文件
# # r表示以读取的方式打开文件
# # a表示以追加的方式打开文件
# # r+表示以读写方式打开文件
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")
#     file_object.write("I also love finding meaning in large datasets.\n")
#     file_object.write("I love creating apps that can run in a browser.\n")

# with open(filename, 'a') as file_object:
#     file_object.write("I also love finding meaning in large datasets.\n")

# 异常
first_number = input("\nFirst number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    # print("You can't divide by zero!")
    pass
else:
    print(answer)
