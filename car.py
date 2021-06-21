class Car:
    def __init__(self,color,company,speed_limit,model):
        self.color=color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print('Started')

    def stop(self):
        print('Stopped')

    def accelerate(self):
        print('Accelerating')

    def changeGear(self):
        print('Gear Changed')                
        
audi = Car("red","audi","130","audi a5")
#print(audi.color)
Car.start(audi)
