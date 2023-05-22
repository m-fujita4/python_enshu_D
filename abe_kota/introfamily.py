class Intro:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def name_out(self):
        nametxt="私の名前は、"+self.name+"です"
        return nametxt
    
    def age_out(self):
        agetxt="私の名前は、"+self.age+"歳です"
        return agetxt
    
class IntroFam(Intro):
    def __init__(self,name,age,cat_name):
        super.__init__(name,age)
        self.cat_name=cat_name

    def cat_name_out(self):
        cattxt="飼い猫の名前は、"+self.cat_name+"です"
        return cattxt
    
