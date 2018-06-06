# Decorators

Decorators 'decorate' or 'wrap' another function and let you execute code before and after the wrapped function runs.  
Allow you to define blocks that can change or extend the behavior of other functions, without permanently modifying the wrapped function itself.  
Technically, a decorator is:
* a callable that takes a callable as input and returns another callable.

## Simplest Decorator - Does Nothing
Decorator function - does nothing other than wrap another function.  
```python
def null_decorator(func):
    return func
```
Usage:
```python
def greet():
    return "Hello!"

>>> greet = null_decorator(greet)
>>> greet()
'Hello!'
```
Another way to put it:
```python
>>> @null_decorator
... def greet():
...   return "Hello!"
...
>>> greet()
'Hello!'
```

## Decorators Can Modify Behavior
```python
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return "Hello!"
```
Now, let's run.
```python
>>> greet()
'HELLO!'
>>> greet
<function uppercase.<locals>.wrapper at 0x7f20ff6a0378>
>>> def null_decorator(func):
...     return func
>>> # `null_decorator()` doesn't change anything, so it uses the same function object
>>> null_decorator(greet)
<function uppercase.<locals>.wrapper at 0x7f20ff6a0378>
>>> # But here, it's a different function object. It replaces the input function with closure.
>>> uppercase(greet)
<function uppercase.<locals>.wrapper at 0x7f20ff6a0488>
```

## Apply Multiple Decorators
We can combine multiple decorators.
```python
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper
def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return "Hello"
```
We can run the function.
```python
>>> greet()
'<strong><em>Hello!</em></strong>'
```
Note that the decorators were applied from _bottom to top_.  
Basically, it equals to the following.
```python
decorated_greet = strong(emphasis(greet))
```
Impact on performance because of the nested function calls.

## Decorate Functions That Accept Arguments
Have to forward arguments to the input function.  
Won't work with functions like this.  
As a workaround, can use `*args` and `**kwargs`.
```python
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
Can expand the technique.
```python
def trace(func):
    def wrapper(*args, **kwargs):
        msg = f"TRACE: calling {func.__name__}() " + \
        f"with {args}, {kwargs}"
        print(msg)
        original_result = func(*args, **kwargs)
        msg2 = f"TRACE: {func.__name__}() " + \
        f"returned {original_result!r}"
        print(msg2)
        return original_result
    return wrapper
```
Now, let's use this one.
```python
@trace
def say(name, line):
    return f"{name}: {line}"

>>> say("Jane", "Hello world")
TRACE: calling say() with ('Jane', 'Hello world'), {}
TRACE: say() returned 'Jane: Hello world'
'Jane: Hello world'
```

## How to Write "Debuggable" Decorators
With a deco, what you really do is replace one function by another. This hides some of the metadata attached to the original (undecorated) data.  
Example:
```python
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

>>> @uppercase
... def greet():
...     '''Return a friendly greeting'''
...     return 'Hello'
...
>>> greet()
'HELLO'
```
No original name, no docstring.
```python
>>> greet.__name__
'wrapper'
>>> greet.__doc__
>>>
```
This makes debugging and working with Py interpreter more challenging.  
A quick fix: `functools.wraps`.
```python
>>> @uppercase
... def greet():
...   '''Return a friendly greeting'''
...   return "Hello"
...
>>> greet()
'HELLO'
>>> greet.__name__
'greet'
>>> greet.__doc__
'Return a friendly greeting'
```

Takeaways:
* Decorators are reusable functions that modify other functions.
* Most common shorthand. If multipledecorators, the order is bottom to top.
* For debugging, you can use `functools.wraps` to enable metadata.
