
#Exception of division by zero#

b=int(input("Enter a number for dividing 20 :"))

try:
    a=20/b
    print(a)
    print('Try completed!')
except ZeroDivisionError:
    print("Can't be divided by ZERO!")
print("MISSION COMPLETED!")    