def calculate_fuel_efficeiency(distance_km,liters_used):
    try :
        distance = float(distance_km)
        fuel = float(liters_used)
        if distance < 0 or fuel <0 :
          raise ValueError 
          return " Distance and fuel cannot be negative."
        km_per_liter =distance / fuel

    except ZeroDivisionError:
        return "fuel  cannot  be zero"

    except ValueError as err:
        return f"value error {err}"

    except TypeError :
        return "Error: Unsupported input type provided"

    else :
        return f"Fuel efficiency: {km_per_liter :.2f} KM/L"

# print(calculate_fuel_efficeiency("450.5","32.4"))

# print(calculate_fuel_efficeiency("106",0))

print(calculate_fuel_efficeiency(400,40))
print(calculate_fuel_efficeiency("460.5","34.6"))
print(calculate_fuel_efficeiency(-10,5))

print(calculate_fuel_efficeiency(80,5))

print(calculate_fuel_efficeiency(-9,10))

print(calculate_fuel_efficeiency(80.4,8.5))
    

    
        