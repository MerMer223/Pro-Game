class Cars():
    def __init__(name,model,brand,speed):
        name.model = name
        name.brand = name
        name.speed = speed
    def printdetails(name):
        print(name.model,name.brand,name.speed)
    def changedetails(name):
        print(1,2,3)
        choice = int(input("type 1 to accelerate or decelerate"))
        if choice == 1:
            name.model = input("Enter new speed")
