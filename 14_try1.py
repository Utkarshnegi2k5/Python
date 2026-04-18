try:
    number = int(input("Enter a number: "))
    result = 10/number
except ValueError:
    print("Enter a valid number!!! BC")
except ZeroDivisionError:
    print("Cant divide number by zero you mf")
except Exception as e:
    print(f"An unexpected error : {e}")

else:
    print(f"The result is : {result}")

print("Happy coding")