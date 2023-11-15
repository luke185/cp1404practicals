from taxi import Taxi

my_taxi = Taxi('Pris 1', 100, 1.23)
my_taxi.drive(40)
print(f"{my_taxi}, current fare total is: ${my_taxi.get_fare()}")
my_taxi.start_fare()
my_taxi.drive(100)
print(f"{my_taxi}, current fare total is: ${my_taxi.get_fare()}")
