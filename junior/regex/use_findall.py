import re

# s = 'one123two145three423four5664five755six299seven119eight'
s = 'hello world'
 
# p = re.compile(r'\d+')
p = re.compile('(\w+) (\w+)')

# ret = p.search(s)
# if ret:
#     print(ret.group())

# ret = p.findall(s)
# print(ret)

# ret = p.split(s)
# print(ret)

# 使用字符串替换
# ret = p.sub('Fuck', s)
# print(ret)

# 使用匹配数进行替换
# ret = p.sub(r'\2 \1', s)
# print(ret)

# 使用函数进行修改替换
def chg(m):
    return m.group(2) + ' ' + m.group(1)
ret = p.sub(chg, s)
print(ret)
