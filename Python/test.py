"""
The purpose of this module is to verify
the validity of the is_even solution.

Usage
-----
python test.py [path of file to check]

(Example - python test.py lcm.py)

Notes
-----
This program assumes that the module in question,
runs by asking input to the user and displays
whether its even or not in the next line.

Example of Valid Program
------------------------
Enter your number - (input)
Your number is even.

Example of Invalid Program
------------------------
Enter your number - (input)
Please wait while i am calculating.
Your number is even.
"""
import sys  # import python's core system module.
import traceback
from collections.abc import Callable
from io import StringIO  # StringIO is like an in-memory file.

# We are going to override the stdin and stdout of python,
# so we will just store the originals to revert back if needed.
old_stdin, old_stdout = sys.stdin, sys.stdout


# Create an in-memory file which supports reading and writing.
class Buffer(StringIO):
    """
    A python file like object.

    We will use this as the new stdin and stdout of python.
    """
    def __init__(self):
        """
        Initiates the buffer to be writeable,
        and sets the next input to return as empty.
        """
        super().__init__()  # Initiate the parent StringIO which is the writing part.
        self.input_val = ''  # This is the value which is going to be sent if the buffer is read.

    def readline(self, *args, **kwargs) -> str:
        """
        This is the method which supports the reading part.

        Returns
        -------
        input : str
            The pre-configured input.

        Raises
        ------
        ValueError
            If there is no input or no valid input.
        """
        inp = self.input_val  # Backup the original input_val, because we are going to reset it before sending.

        # Check if the input_val is a non-empty string.
        if not isinstance(inp, str) or not inp:
            # If not, then raise ValueError.
            raise ValueError('No string input in buffer.')

        # Past this point this method is 100% going to return an output.
        #
        # Suppose the program asks a number, then this number will return the input to be checked,
        # then we want to check the next line if the program prints (even) or (odd), so we have to clear all
        # the previous lines, and also to stop the program from asking more input (because we don't know
        # what input its asking now), we reset the input_val also.
        self.reset()

        # Now we return the backed up input_val, because we resetted it.
        return inp

    def reset(self):
        """
        This function is supposed to reset the
        previous output, and the input val.

        But fortunately the __init__ method does exactly that.
        So this function is just a wrapper to that.
        """
        self.__init__()


# Create the in-memory file.
buffer = Buffer()
# stdin - is where python reads the input from.
# stdout - is where python prints the output to.
# We change these two to our buffer.
sys.stdin, sys.stdout = buffer, buffer

# Check if the user passed any file.
# Of course, we need a file to check.
# If any file is passed, it will be present in sys.argv[1].
# So we check if there is sys.argv[1].
if len(sys.argv) < 2:
    # If not, raise ValueError.
    raise ValueError('No file passed to check')

# Normally if we want to check if a function is working,
# we just import the function from the module and check it.
# But I don't want the user to be limited to creating a function.
# So I read the contents of the module and load it.
with open(sys.argv[1]) as file:
    # We get the contents from the file, and
    # compile it into a python code object,
    # which can be than executed.
    compiled = compile(file.read(), 'to_check', 'exec')


def run(method: Callable, *args):
    """
    The function to run the compiled code.

    Parameters
    ----------
    method : Callable
        The function to call after executing the program.
    args : Any
        The args to pass to the method.
    """
    # noinspection PyBroadException
    try:
        # Its good to have the (if __name__ == '__main__') statement,
        # but in our case since, the program is being executed from test.py,
        # the __name__ will not be '__main__' in the other program,
        # but since we want the code inside that block also to be run,
        # we explicitly set __name__ = '__main__' as globals in exec.
        exec(compiled, {'__name__': '__main__'})
    except Exception:
        # Despite the error occurred, we want our program to run
        # and display all the errors to the user.
        traceback.print_exc(file=old_stdout)
    finally:
        # Call the post run method with the args.
        method(*args)


# Create a list to store all the functions
# that will check the program's validity.
test_functions = []


def tester(*values: str) -> Callable[[Callable[[str]]], Callable[[]]]:
    """
    This function simplifies the
    writing of the test functions.

    Parameters
    ----------
    values : str
        The values which are to be used as input for testing.

    Notes
    -----
    The values passed will not be run as a single test.

    Each value will be mapped to its own test,
    but with the same method passed.
    """

    # We have the values to check, now all we need is a function
    # that will process the results of the other program.
    # So we return a function which gets the post process function.
    def get_method(method: Callable[[str]]) -> Callable[[]]:
        """
        This function is a decorator which will return the main function
        which runs the program and the post process function.

        Parameters
        ----------
        method : Callable
            This is the function which be called after executing the other program.
        """
        def run_function():
            """
            This is the main function, for each value passed,
            it runs the compiled program and the post process function.
            """

            # Loop through the values.
            for value in values:
                buffer.input_val = value  # Set the input_val to the current val in loop.
                run(method, value)  # Run the test.

        # Add this function to our test_functions so that,
        # we can execute all the functions from that list.
        test_functions.append(run_function)
        return run_function
    return get_method


# All the tests.
@tester('2', '-2')
def test_even(value: str):
    """
    Test if the program properly displays "even",
    for these small even integers(positive and negative).

    Parameters
    ----------
    value : str
        The value which was used as input for the compiled program.
    """

    # Gets the first line from the output after the program asked for input.
    first_line = ''.join(buffer.getvalue().split('\n')[:1])

    # Check if "even" is in the first line.
    if 'even' not in first_line:
        # If not just print that the test verification for the number failed
        print(f'Failed to verify {value} as an even integer.\n', file = old_stdout)


@tester('1', '-1')
def test_odd(value: str):
    """
    Test if the program properly displays "odd",
    for these small odd integers(positive and negative).

    Parameters
    ----------
    value : str
        The value which was used as input for the compiled program.
    """

    # Gets the first line from the output after the program asked for input.
    first_line = ''.join(buffer.getvalue().split('\n')[:1])

    # Check if "odd" is in the first line.
    if 'odd' not in first_line:
        # If not just print that the test verification for the number failed
        print(f'Failed to verify {value} as an odd integer.\n', file = old_stdout)


@tester('89898', '-89898')
def test_even_large(value: str):
    """
    Test if the program properly displays "even",
    for these large even integers(positive and negative).

    Parameters
    ----------
    value : str
        The value which was used as input for the compiled program.
    """

    # Gets the first line from the output after the program asked for input.
    first_line = ''.join(buffer.getvalue().split('\n')[:1])

    # Check if "even" is in the first line.
    if 'even' not in first_line:
        # If not just print that the test verification for the number failed
        print(f'Failed to verify {value} as an even integer.\n', file = old_stdout)


@tester('98989', '-98989')
def test_odd_large(value: str):
    """
    Test if the program properly displays "odd",
    for these large odd integers(positive and negative).

    Parameters
    ----------
    value : str
        The value which was used as input for the compiled program.
    """

    # Gets the first line from the output after the program asked for input.
    first_line = ''.join(buffer.getvalue().split('\n')[:1])

    # Check if "odd" is in the first line.
    if 'odd' not in first_line:
        # If not just print that the test verification for the number failed
        print(f'Failed to verify {value} as an odd integer.\n', file = old_stdout)


# Since we already added all the test functions to this list,
# we can just iterate through the list and run the function
for function in test_functions:
    function()
