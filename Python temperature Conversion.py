

unit = input("Your Temperature in celsius(C) or Fehrenheit(F): ")
temp = float(input("Enter your temp: "))

if unit == "C":
    temp = round((temp *9) / 5 + 32, 1)
    print(f"Your temperature in F is: {temp}F")

elif unit == "F":
    temp = round(((temp - 32) * 5) / 9, 1)
    print(f"Your temperature in celsius is: {temp}C")

else:
    print(f"Your {unit} is invalid.")