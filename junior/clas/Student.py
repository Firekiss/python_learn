
class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print('{}说:我{}岁'.format(self.name, self.age))


class Speaker(object):
    def __init__(self, name, career, topic):
        self.name = name
        self.career = career
        self.topic = topic
    
    def speak(self):
        print('我叫{},我是一个{},我演讲的主题是 {}'.format(self.name, self.career, self.topic))
    

class Student(People, Speaker):
    def __init__(self, name, age, career, topic):
        People.__init__(self, name, age)
        Speaker.__init__(self, name, career, topic)
    
    def speak(self):
        Speaker.speak(self)


s = Student('Jonh', 23, '演说家', 'Python')
s.speak()
print('Student是否为Speaker的子类: {}'.format(issubclass(Student, Speaker)))
print('Student是否为People的子类: {}'.format(issubclass(Student, People)))
