import sys
sys.path.append('../')
print(sys.path)

from packg.ali_pay import tools
from out_packg import main

def ali_pay_apply():
    tools.pay()


 
if __name__ == '__main__':
    ali_pay_apply()
    main.main()