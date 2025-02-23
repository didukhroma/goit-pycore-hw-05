from functools import wraps

def input_error(func:"function")->"function":
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:            
            return f"Enter the argument for the command"
        except IndexError:            
            return f"Please check the number of arguments for the command {func.__name__}."
        except KeyError:            
            return f"Please enter a valid name of contact."
    return inner