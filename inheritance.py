


class BaseClass:
    def display(self,name):
        self.name=name




class SubClass(BaseClass):
    def welcome(self):
        print("Welcome")

    def display_name(self):
        print("Name: "+self.name)



y=SubClass()
y.welcome()
y.set_name("Dilshad")
y.display_name()