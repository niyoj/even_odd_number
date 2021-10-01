"""
The purpose of this module is to show, how to find whether a number is
either an odd or even integer, by comparing the number with its lcm with 2.

The lcm of 2 and an even number is the even number itself, because 2 is a factor in the even number
whereas in the case of odd numbers, since 2 is a prime number and its not a factor of the odd number,
the lcm is 2 * odd_number, but we need not worry about this value, as we can simply put it together as


"The number is even if its lcm with 2 is the number itself, otherwise it is odd."

Examples
--------
This is an example on showing the usage of the is_even function

>>> is_even(42)
True

>>> is_even(23)
False

>>> is_even(-2)
True

>>> is_even(-9)
False

>>> is_even([1, 2, 3])
TypeError: Expected parameter (number) to be an integer, but got as list ([1, 2, 3])

Notes
-----
The is_even function can be verified by calling this script via the test.py program.

python test.py lcm.py (or) test lcm
"""

from math import lcm  # import only the lcm function from python's math library


def is_even(number: int) -> bool:
    """
    This is a function, which is used to check whether
    a giver number is either odd or even.

    Parameters
    ----------
    number : int
        The number which you want to check whether its even or odd.

    Returns
    -------
    is_even : bool
        Whether the number is even or not.

    Raises
    ------
    TypeError
        If the given value for number, is not an integer.
    """

    if not isinstance(number, int):  # Check if the given value is an integer
        # If so, then raise TypeError
        raise TypeError(f'Expected parameter (number) to be an integer, but got as {type(number).__name__} ({number})')

    # Now we verified that the given value is an integer.
    # Now, we check whether the lcm of 2 and the given number
    # is same as the absolute value of number and return the result.

    # Why absolute value?
    # (Example)
    #     The lcm of 2 and -4 is 4
    #     but the given number is -4
    #     we clearly know that 4 is not same as -4
    #     that's why we have to convert -4 to 4
    #     and if you didn't catch it by now,
    #     abs(-4) does exactly that.

    return lcm(2, number) == abs(number)


# What is this if statement over here?
#     Well, we want to make our lcm function reusable
#     so that we can just import the is_even function
#     and use it anywhere, but also we want our
#     program to run if we run this file directly.
#
#     If we didnt add this statement, then
#     our below programme will run everytime we import it.
#
#     So to avoid that python has __name__.
#     __name__ will be "__main__" if this program is run directly
#     otherwise it will not.

if __name__ == '__main__':
    # Preconfigure the question to ask.
    question = 'Enter any integer that, you would like to test if its even or odd - '

    while True:  # Constantly ask the user to provide a number, until they have given actual proper integer.
        input_number = input(question)  # Ask the question.

        # Try to convert the given value into an integer
        try:
            input_number = int(input_number)

        # If it fails
        except ValueError:
            # Reconfigure the question to ask the user to provide a proper integer.
            question = f'Could not convert "{input_number}" to an integer, please enter something else - '
            # There is no statement after this, so the program will go back to the start of the while loop
            # which is where it asks the user again to provide a proper integer.

        # If the conversion of the value to an integer succeeds
        else:
            # Call the is_even function and check if the given number is an even or odd integer.
            if is_even(input_number):
                print(f'{input_number} is an even integer.')  # it is even.
            else:
                print(f'{input_number} is an odd integer')  # it is odd.

            # Everything is complete, now stop asking the user to provide a number.
            break
