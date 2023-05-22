from introduce import Intro


class IntroFam(Intro):
    def __init__(self, name, age, cat):
        super().__init__(name, age)
        self.cat = cat

    def cat_out(self):
        cattxt = "飼い猫の名前は、" + self.cat + "です"
        return cattxt
