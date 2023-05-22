class intro:
    def __init__(self,name,age):
        '''初期化'''
        self.name = name
        self.age = age

    def name_out(self):
        nametext = "私の名前は、" + self.name + "です"
        return nametext
    
    def age_out(self):
        agetext = "年齢は、" + str(self.age) + "歳です"
        return agetext 