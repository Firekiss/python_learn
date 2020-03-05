name = 'alex'
age = 23
m = {
  'name': name,
  'age': age
}
l = [name, age]
num = 459123456.1268662


print('my name is %s , my age is %d' % (name, age))
print('my name is {} , my age is {}'.format(name, age))
print('my name is {0} , my age is {1}'.format(name, age))
print('my name is {name} , my age is {age}'.format(name=name, age=age))
print('my name is {name} , my age is {age}'.format(**m))
print('my name is {} , my age is {}'.format(*l))


# 数字格式化
print('{:.2f}'.format(num))
print('{:,}'.format(num))
print('{:,.2f}'.format(num))