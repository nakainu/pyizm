# スライスの基本

test_list = ['https', 'www', 'python', 'izm', 'com']

print(test_list[:])
print(test_list[::])


# 要素の取得

print(test_list[:4])

print(test_list[2:])

print(test_list[::2])

print(test_list[3:5])

print(test_list[-1:])   # 末尾からすべての要素
print(test_list[:-1])   # 末尾まですべての要素
print(test_list[::-1])  # 末尾から全ての逆順要素

print(test_list[:9999])


# 要素の代入

test_list[1:3] = ('WWW', 'PYTHON')

print(test_list)

# 複数行のコメントアウトのように扱う
'''
print("test1")
print("test2")
'''

print("hoge")

# ネストされた疑似複数行コメントアウト
'''
print("test3")
"""
print("test4")
"""
'''
