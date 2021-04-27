class Car():
	
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		self.odometer_reading = self.odometer_reading + miles
		
class EletricCar(Car):
	
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
		
class Battery():
	
	def __init__(self):
		self.battery_size = 70
		
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-KWh battery.")
		
	def get_range(self):
		if self.battery_size == 70:
			raange = 240
		elif self.battery_size == 85:
			raange = 270
		
		message = "This car can go approximately " + str(raange)
		message = message + " miles on a full charge."
		print(message)
		
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85

my_tesla = EletricCar('tesla', 'model s', 2016)

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


