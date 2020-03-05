
class Vehicle(object):
    trans_type = 'SUV'

    def __init__(self, speed, size):
        self.speed = speed
        self.size = size

    def show_info(self):
        print('当前工具的速度为{0}km/h, 体积为{1}米'.format(self.speed, self.size))

    def move(self):
        print('我已向前移动了50米')

    def set_speed(self, new_speed):
        self.speed = new_speed

    def get_speed(self):
        if self.speed != None:
            print('我的时速为{0} km/h'.format(self.speed))

    def speed_up(self):
        self.speed += 10
        print('我的速度由{0} km/提升到了{1} km/h'.format(self.speed - 10, self.speed))

    def speed_down(self):
        self.speed -= 15
        print('我的速度由{0} km/下降到了{1} km/h'.format(self.speed + 15, self.speed))


def transport_identify(instance, judged_class):
    if isinstance(instance ,judged_class):
        print('类型匹配')
    else:
        print('类型不匹配')


tool_1 = Vehicle(20, '(3.6, 1.9, 1.75)')
tool_1.show_info()
tool_1.move()
tool_1.set_speed(40)
tool_1.get_speed()
tool_1.speed_up()
tool_1.speed_down()
transport_identify(tool_1, Vehicle)