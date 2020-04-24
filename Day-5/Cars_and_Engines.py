class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def printDetails(self):
        print("Model :", self.model)
        print("Color :", self.color)

class SedanEngine:
    def start(self):
        print("Car has started")

    def stop(self):
        print("Car has stopped")

class Sedan(Car):
    def __init__(self, model, color):
        super().__init__(model, color)
        self.engine = SedanEngine()

    def setStart(self):
        return self.engine.start()

    def setStop(self):
        return self.engine.stop()

car1 = Sedan("Toyota","Grey")
car1.setStart()
car1.printDetails()
car1.setStop()
