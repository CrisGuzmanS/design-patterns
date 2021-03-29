class Car:

    def start(self):
        print("car has started.")

    def stop(self):
        print("Car has stopped.")

    def set_alarm(self):
        print("set alarm")

    def remove_alarm(self):
        print("alarm removed")

class ICommand:

    def execute(self):
        pass

# 
# 
# 

class CommandStart(ICommand):

    car = None

    def __init__(self, car):
        self.car = car

    # 
    # 
    # 

    def execute(self):
        self.car.start()

# 
# 
# 

class CommandStop(ICommand):

    def __init__(self, car):
        self.car = car

    # 
    # 
    # 

    def execute(self):
        self.car.stop() 

# 
# Is the invoker
# 

class RemoteControl:

    commands = []

    def __init__(self, car):
        self.commands.append( CommandStart(car) )
        self.commands.append( CommandStop(car) )

    def button(self, index):

        self.commands[index].execute()


car = Car()
remoteControl = RemoteControl(car)

remoteControl.button(0)
remoteControl.button(1)