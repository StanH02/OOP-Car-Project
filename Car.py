class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        self.max_speed = 30

    def start(self):
        print("Car is now starting...")

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += 5
            print("The Car is now accelerating")

        else:
            print("Car is pass maximum speed...")

    def brake(self):
        if self.speed > 0:
            self.speed -= 5
            print("Car is braking...")
        else:
            print("Car is already stopped.")

    def currentSpeed(self):

         print(f"Current Speed: {self.speed}")


myCar = Car("Ford", "Mustang", 1999)
myCar.start()
myCar.accelerate()
myCar.currentSpeed()
myCar.brake()
myCar.currentSpeed()
myCar.accelerate()
myCar.accelerate()
myCar.accelerate()
myCar.accelerate()
myCar.accelerate()
myCar.accelerate()
myCar.currentSpeed()
myCar.accelerate()








