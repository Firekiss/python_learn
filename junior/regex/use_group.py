import re

# 身份证号码
str = '320684199205030277'

# 编译身份证号码
p = re.compile(r'(?P<local>\d{6})((?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2}))\d{2}(?P<sex>\d)(\d|X)')
match_ret = p.match(str)
if match_ret:
  gs = match_ret.groups()
  gd = match_ret.groupdict()
  print(gs)
  print(gd)


