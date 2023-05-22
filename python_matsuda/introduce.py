class Intro:
    '''自己紹介のクラス'''
    def __init__(self,name,age):
        '''初期化'''
        self.name = name
        self.age = age
    
    def name_out(self):
        '''名前の出力'''
        nametxt = "私の名前は、"+ self.name + "です"
        return nametxt
    
    def age_out(self):
        '''年齢の出力'''
        agetxt ="年齢は、"+ self.age + "歳です"
        return agetxt
