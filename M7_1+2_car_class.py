class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

       # Variables
        self._current_speed = 0        

    def accelerate(self, step=10):
        self._current_speed += step

    def decelerate(self, step=10):
        self._current_speed -= step

    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'

    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"

# >	  __gt__(self, other)  ang. greater than – większy niż
# >=  __ge__(self, other)  ang. greater or equal – większy lub równy
# <	  __lt__(self, other)  ang. less than – mniejszy niż
# <=  __le__(self, other)  ang. less or equal – mniejszy lub równy
# ==  __eq__(self, other)  ang. equal – równy

#    def __eq__(self, other):
#        return (
#            self.make == other.make and
#            self.model_name == other.model_name and
#            self.top_speed == other.top_speed and
#            self.color == other.color
#        )

    def __eq__(self, other):
        return all(
#        return any(
            (
                self.make == other.make,
                self.model_name == other.model_name,
                self.top_speed == other.top_speed,
                self.color == other.color
            )
        )

    def __gt__(self, other):
        return self.top_speed > other.top_speed

    #to co ma być zastąpione dekoratorem @property
    #def set_current_speed(self, value):
    #    if value <= self.top_speed:
    #        self.current_speed = value
    #    else:
    #        raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            try:                                                                               #moje usprawnienie
                raise ValueError()                                                             #wyciąłem f"Value {value} exceeds top speed of {self.top_speed}"
            except ValueError:                                                                 #moje usprawnienie
                print(f"Value {value} exceeds top speed of {self.top_speed}")                  #moje usprawnienie

class Truck(Car):
   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

#super() służy do odwołania się do klasy, którą odziedziczyliśmy - dodajemy tylko nową zmienną; równoważy poniższy zapis:
#class Truck(Car):
#   def __init__(self, make, model_name, top_speed, color, max_load):
#       self.make = make
#       self.model_name = model_name
#       self.top_speed = top_speed
#       self.color = color

      # Variables
#       self._current_speed = 0
#       self.max_load = max_load

mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
mustang2 = Car(make="Ford", model_name="Mustang", top_speed=250, color="Yellow")
mustang3 = Car(make="Ford", model_name="Mustang", top_speed=200, color="Red")

#print(mustang)

#print(mustang2)
#print(mustang.make)

#print(mustang == mustang2)
#print(mustang == mustang3)
#print(mustang2 < mustang3)

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]
by_speed = sorted(cars, key=lambda car: car.top_speed)
by_make = sorted(cars, key=lambda car: car.make)

#   def get_make(car):
#       return car.make
#inaczej
#   lambda car: car.make

#print(by_speed)
#print(by_make)

#print(mustang.current_speed)
mustang.accelerate()
#print(mustang.current_speed)
mustang.accelerate(50)
#print(mustang.current_speed)
mustang.decelerate(40)
#print(mustang.current_speed)

mustang.current_speed = 100
#print(mustang.current_speed)

mustang.current_speed = 400
#print(mustang.current_speed)

truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
print(truck)

print(truck.current_speed)
truck.accelerate()
print(truck.current_speed)

print(isinstance(mustang, Truck))
print(isinstance(mustang, Car))
print(isinstance(truck, Car))
print(issubclass(Truck, Car))
print(issubclass(Car, Truck))