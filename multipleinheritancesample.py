class First:
    def display_first(self):
        print("hai")
class Second(First):
    def display_second(self):
        print("Second")
class Third(Second):
    def display_third(self):
        print("Third")


x=Third()
x.display_third()
x.display_first()