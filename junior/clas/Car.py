"""
Car类
"""

class Car(object):
    description = ['大众','丰田','广本','沃尔沃','凯迪拉克']

    def __init__(self, l, w, h, brand):
        self.L = l
        self.W = w
        self.H = h
        self.brand = brand

    def modify_des(self):
        if self.description != None:
            return self.description
        else:
            print('请输入您的车辆描述')
    
    @staticmethod
    def basic_parameters():
        print('已完成车辆基本参数信息的录入！')

    @classmethod
    def upkeep(cls, desc):
        if desc in cls.description:
            print('根据汽车保养的相关经验，{}品牌的车应于5000km/次的频率进行专业性保养'.format(desc))
        else:
            print('非常抱歉！{}品牌不在我们的保养范围内'.format(desc))
    


if __name__ == '__main__':
    car_1 = Car(3, 2, 1.5, '大众')
    car_1.basic_parameters()

    if car_1.modify_des():
        car_1.upkeep(car_1.brand)
    else:
        print('请正确填写相关的车辆信息')
    