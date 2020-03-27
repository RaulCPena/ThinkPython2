# Convert.py
#       A program to convert Celsius temps to Fahrenheit
#       by: Susan Computewell


def main():
    print("This program converts Celsius to Fahrenheit")

    celsius = eval(input("What is the celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()
