"""
Devin Bulawa
SDEV 300 6381
5/24/2024

"""
import string
import secrets
from datetime import date
import math


class PositiveIntegerException(Exception):
    """A user-defined exception class that catches if a positive integer was not entered"""


class InvalidInputException(Exception):
    """A user-defined exception class that validate the input entered for the selection menu"""


class ConstraintException(Exception):
    """A user-defined exception class that validates the input constraints for the
    password application"""


def cylinder_volume():
    """calculates the volume of a right circular cylinder given a radius
    and a height"""

    while True:
        try:
            radius = int(input("Enter a positive integer for the radius of the cylinder:"))
            if radius < 0:
                # stops the program if the integer entered is not positive
                raise PositiveIntegerException
            height = int(input("Enter a positive integer for the height of the cylinder:"))
            if height < 0:
                # stops the program if the integer entered is not positive
                raise PositiveIntegerException

            # calculates the volume of the cylinder
            volume = math.pi * pow(radius, 2) * height

            # prints the result with a formatted decimal precision of 2
            print(f"{volume:.2f}", "is the volume of the Right Circular Cylinder")
            return False  # stops the loop

        # defines what happens when the exceptions are raised
        except PositiveIntegerException:
            print("The integer you entered is not positive.")
        except ValueError:
            print("you input an invalid constraint value. Values should be positive integers.")


def law_of_cosines():
    """Uses the law of cosines to determine the length of line c in a triangle
    given user input for lines a, b, and angle y"""

    while True:
        try:
            a = int(input("Enter a positive integer for line a <-> c length:"))
            if a < 0:
                # raises this exception if a is not a positive integer
                raise PositiveIntegerException
            b = int(input("Enter a positive integer for line b <-> c length:"))
            if b < 0:
                # raises this exception if b is not a positive integer
                raise PositiveIntegerException
            y = int(input("Enter a positive integer for angle of C in the triangle:"))
            if y < 0:
                # raises this exception if y is not a positive integer
                raise PositiveIntegerException

            # calculates the length of c using the law of cosines formula
            c = math.sqrt((pow(a, 2) + pow(b, 2)) - (2 * ((a * b) * math.cos(math.radians(y)))))
            # formats the result to 2 decimals of precision
            print(f"{c:.2f} is the length of c")
            return False  # stops the loop

        # defines what happens when the exceptions are raised
        except PositiveIntegerException:
            print("The integer you entered is not positive.")
        except ValueError:
            print("you input an invalid constraint value. Values should be positive integers.")


def days_until():
    """calculates the amount of days until July 4, 2025"""
    # sets today as today's date
    today = date.today()
    # sets the desired date for the calculation to july 4, 2025
    d = date(2025, 7, 4)
    # calculates the difference between the target date and today
    difference = d - today
    # formats the result to the difference of days and displays the
    # target date as day of the week, month, day, and year
    print(difference.days, "days until", d.strftime("%A %B %d, %Y"))


def calculate_percent():
    """calculates a percentage to a certain decimal precision given a user
    input of a numerator, denominator, and level of precision"""

    while True:
        try:
            numerator = int(input("Enter a positive integer numerator:"))
            if numerator < 0:
                # raises this exception if the numerator is not a positive integer
                raise PositiveIntegerException
            denominator = int(input("Enter a positive integer denominator"))
            if denominator < 0:
                # raises this exception if the denominator is not a positive integer
                raise PositiveIntegerException
            precision = int(input("enter a positive integer float precision:"))
            if precision < 0:
                # raises this exception if the precision is not a positive integer
                raise PositiveIntegerException

            # calculates the percentage
            result = (numerator / denominator) * 100
            # formats the percentage to the desired precision
            print(numerator, "/", denominator, "yields", f"{result:.{precision}f}", "percent")
            return False  # stops the loop

        # defines what happens when the exceptions are raised
        except PositiveIntegerException:
            print("The integer you entered is not positive.")
        except ValueError:
            print("you input an invalid constraint value. Values should be positive integers.")


def generate_secure_pass():
    """generates a secure password given a password length, minimum number of
     uppercase/lowercase letters, numbers, and special characters"""

    # defines the alphabet to be used with all ascii letters, digits, and
    # special characters
    alphabet = string.ascii_letters + string.digits + string.punctuation
    try:
        pass_length = int(input("How long should the password be?"))
        if pass_length <= 0:
            # raises this exception if password length is not a positive integer
            raise PositiveIntegerException
        min_upper = int(input("Minimum number of upper case characters?"))
        if min_upper < 0:
            # raises this exception if the minimum
            # number of upper case characters is not a positive integer
            raise PositiveIntegerException
        min_lower = int(input("Minimum number of lower case characters?"))
        if min_lower < 0:
            # raises this exception if the minimum number
            # of lower case letters is not a positive integer
            raise PositiveIntegerException
        min_digit = int(input("Minimum number of digit characters?"))
        if min_digit < 0:
            # raises this exception if the minimum number
            # of digits is not a positive integer
            raise PositiveIntegerException
        min_special = int(input("Minimum number of special characters?"))
        if min_special < 0:
            # raises this exception if the minimum number
            # of special characters is not a positive integer
            raise PositiveIntegerException

        if sum([min_upper, min_lower, min_digit, min_special]) > pass_length:
            # raises this exception if the sum of all the constraints
            # are greater than the password length
            raise ConstraintException

        while True:
            # generates a password using the defined alphabet within
            # the desired length
            password = ''.join(secrets.choice(alphabet) for i in range(pass_length))

            # determines if the generated password meets the
            # constraints provided by the user
            if(sum(c.islower() for c in password) >= min_lower
                    and sum(c.isupper() for c in password) >= min_upper
                    and sum(c.isdigit() for c in password) >= min_digit
                    and sum(not c.isalpha() for c in password) >= min_special):
                break  # stops the loop if the constraints are met
        print(password)

    # defines what happens when the exceptions are raised
    except ConstraintException:
        print("You input constraints that are greater than your password length")
    except PositiveIntegerException:
        print("you input an invalid constraint value. Values should be positive integers.")
    except ValueError:
        print("you input an invalid constraint value. Values should be positive integers.")


def main():
    """main function for running the lab 2 application"""

    running = True
    print("Welcome to the Python SDEV300 Lab 2 Application")

    while running:
        try:
            # creates the menu of options for the user to select from
            print("What would you like to do today?")
            print("""    a. Generate Secure Password
    b. Calculate and Format a Percentage
    c. How many days from today until July 4, 2025?
    d. Use the Law of Cosines to calculate the leg of a triangle.
    e. Calculate the volume of a Right Circular Cylinder
    f. Exit program""")

            response = input("Please make a selection (a-f):")
            if not response.lower() in ['a', 'b', 'c', 'd', 'e', 'f']:
                # raise this exception if the user does not input a valid option
                # of a-f
                raise InvalidInputException

            # starts the secure password generator application
            if response.lower() == "a":
                generate_secure_pass()

            # starts the percentage calculator application
            elif response.lower() == "b":
                calculate_percent()

            # starts the days until july 4, 2025 application
            elif response.lower() == "c":
                days_until()

            # starts the law of cosines application
            elif response.lower() == "d":
                law_of_cosines()

            # starts the cylinder volume application
            elif response.lower() == "e":
                cylinder_volume()

            # quit option
            elif response.lower() == "f":
                running = False  # quits the loop if f is selected

        # defines what happens when the exception is raised
        except InvalidInputException:
            print("Please enter a valid option a - f.")


main()  # calls the main function to run the application
