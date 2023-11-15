from silver_service_taxi import SilverServiceTaxi

# Test that it displays the same as the example
hummer = SilverServiceTaxi('Hummer', 200, 2)
print(hummer)

# Test the fare calculates correctly according to the example
print(f"After a trip of {hummer.drive(18)}km, fare total is: ${hummer.get_fare()}")
