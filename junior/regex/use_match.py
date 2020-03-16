import re

# match 只会从第一个位置开始匹配 再后面匹配到的
pattern = re.compile(r'hello')
ret = pattern.match('hello world')
print(ret)

