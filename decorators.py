# Here's your task:

# Create a global variable is_logged_in and set it to False.

# Create a decorator by the name of login_required. This decorator should modify the function it wraps to simply return False if the global value is_logged_in is set to False. Otherwise, it should call the function as normal.

# Create a new function generate_view and decorate it with the login_required generator. This function should simply return a string "Hello!".

# Call the generate_view function to see if you get False or the string "Hello!".

# Change global variable is_logged_in to True and call generate_view again. Check the result.


is_logged_in = True


def login_required(f):
    global is_logged_in

    def wrapper():

        if is_logged_in:
            return f()
        else:
            return is_logged_in
    return wrapper


@login_required
def generate_view():
    print("Hello")


if __name__ == "__main__":
    generate_view()
