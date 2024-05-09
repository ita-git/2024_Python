from introduce import Intro

#基底クラスに「intro」を持つ派生クラス「intro_fm」を定義
class IntroFam(Intro):
    def __init__(self, name, age, cat):
        self.name = name
        self.age = age
        self.cat = cat

    #飼い猫の名前を編集するメソッドを定義    
    def cat_out(self):
        cattxt = "飼い猫の名前は、" + self.cat + "です"
        return cattxt 