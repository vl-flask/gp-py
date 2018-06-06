def trace(func):
    def wrapper(*args, **kwargs):
        msg = f"TRACE: calling {func.__name__}() " + \
        f"with {args}, {kwargs}"
        print(msg)

        original_result = func(*args, **kwargs)

        msg2 = f"TRACE: {func.__name__}() " + \
        f"returned {original_result!r}"
        print(msg)

        return original_result
    return wrapper

@trace
def say(name, line):
    return f"{name}: {line}"
