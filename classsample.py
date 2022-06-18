class MySampleClass:
    def hello(self,n):
        self.name=n
    def print_name(self):
        print(self.name)

x=MySampleClass()
y=MySampleClass()
name="TRASH"
x.hello(name)
y.hello("Sachu z403")

x.print_name()
y.print_name()

