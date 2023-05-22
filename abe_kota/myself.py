class Intro:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def name_out(self):
        nametxt="私の名前は、"+self.name+"です"
        return nametxt
    
    def age_out(self):
        agetxt="年齢は、"+self.age+"歳です"
        return agetxt
    
myself=Intro(name="太郎",age="35")

print(myself.name_out())
print(myself.age_out())
