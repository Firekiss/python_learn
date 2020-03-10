class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print('hello!我是{0}'.format(self.name))

    def relation(self):
        pass


class Student(Person):
    def __init__(self, name, gender, score, major, num=2018014002):
        super(Student, self).__init__(name, gender)
        self.score = score
        self.major = major
        self.__num = num

    def speak(self):
        super(Student, self).speak()
        print('我的学号为{0}，很高兴认识大家'.format(self.__num))
    
    def identify_stu(self):
        if self.__num == 2018014002:
            print('我的分组已经完成')
        else:
            print('请稍后，马上为你自动分组')

    def set_num(self, new_num):
        self.__num = new_num

    def relation(self):
        if issubclass(Student, Person):
            print('我的父类是Person')
        else:
            print('父类正在查询中······')


stu = Student('小明', '二年级', 98, '语文')
stu.speak()
stu.identify_stu()
stu.relation()
print('*' * 20)
stu_2 = Student('小红', '二年级', 98, '语文', 2019040625)
stu_2.speak()
stu_2.identify_stu()