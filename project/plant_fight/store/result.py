

class Score(object):
    # 游戏积分类
    
    def __init__(self):
        # 积分值
        self.__score = 0
    
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if new_score < 0:
            return None
        self.__score = new_score

