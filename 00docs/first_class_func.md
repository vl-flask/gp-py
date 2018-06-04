# Functions as First-Class Objects

Original [here](https://dbader.org/blog/python-first-class-functions).  

# Basic Function and Usage
Function [`yell(text)`](first_class_func/yell.py)
```python
def yell(text):
    return text.upper() + "!"
```
Usage:
```python
>>> yell("hello")
'HELLO!'
```
Now, there is a function object, and `yell` only references it.  
We can make more references to the same function object.
```python
>>> bark = yell
>>> bark("woof")
'WOOF!'
```
We can delete a reference, but the function can still be available under a different alias.
```python
>>> del yell
>>> yell("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'yell' is not defined
>>> bark("hey")
'HEY!'
```
Still, we can find the original name using the `__name__` attribute. You can't use it though.
```python
>>> bark.__name__
'yell'
```
## Can Be Stored in Data Structures
```python
>>> funcs = [bark, str.lower, str.capitalize]
>>> funcs
[<function yell at 0x7f916180de18>, <method 'lower' of 'str' objects>, <method 'capitalize' of 'str' objects>]
>>> for f in funcs: print(f, f('hey there'))
...
<function yell at 0x7f916180de18> HEY THERE!
<method 'lower' of 'str' objects> hey there
<method 'capitalize' of 'str' objects> Hey there
>>> funcs[0]('heyho')
'HEYHO!'
```

## Can Pass Functions to Other Functions
```python
>>> def yell(text):
...     return text.upper() + "!"
>>> def whisper(text):
...     return text.lower() + "..."
>>> def greet(func):
...     greeting = func("Hi, I'm a Python program")
...     print(greeting)
>>> greet(yell)
HI, I'M A PYTHON PROGRAM!
>>> greet(whisper)
hi, i'm a python program...
>>> a = ['hello', 'hey', 'hi']
>>> b = [yell(el) for el in a]
>>> b
['HELLO!', 'HEY!', 'HI!']
>>> c = list(map(yell, a))
>>> c
['HELLO!', 'HEY!', 'HI!']
```

## Functions Can Be Nested
```python
>>> def speak(txt):
...     def whisper(t):
...         return t.lower() + "..."
...     return whisper(txt)
...
>>> speak("Hello, World")
'hello, world...'
```
Inner functions can't be accessed outside the function.
```python
>>> whisper("yo")
...
NameError: name 'whisper' is not defined
>>> speak.whisper
...
AttributeError: 'function' object has no attribute 'whisper'
```
But inner functions can be returned.
```python
>>> def get_speak_func(volume):
...   def whisper(text):
...     return text.lower() + "..."
...   def yell(text):
...     return text.upper() + "!"
...   if volume > 0.5:
...     return yell
...   else:
...     return whisper
>>> get_speak_func(0.3)
<function get_speak_func.<locals>.whisper at 0x7f1d96a2e6a8>
>>> get_speak_func(0.7)
<function get_speak_func.<locals>.yell at 0x7f1d9696e400>
>>> speak_low = get_speak_func(0.3)
>>> speak_loud = get_speak_func(0.8)
>>> h = "Hello"
>>> speak_low(h)
'hello...'
>>> speak_loud(h)
'HELLO!'

# Functions Can Capture Local State
Not only can functions can return other functions, but these inner functions can also _capture and carry some of the pater function's state_ with them.
```python
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + "..."
    def yell():
        return text.upper() + "!"
    if volume > 0.5:
        return yell
    else:
        return whisper

>>> get_speak_func('Hello, World', 0.7)()
'HELLO, WORLD!'
```
So, you can choose a function to return, based on some conditions.  
But you can also return a function and pre-configure it.
```python
def make_adder(n):
    def add(x):
        return x + n
    return add
plus_3 = make_adder(3)
plus_5 = make_adder(5)
plus_3(4)
plus_5(4)
```
```python
>>> plus_3 = make_adder(3)
>>> plus_5 = make_adder(5)
>>> plus_3(4)
7
>>> plus_5(4)
9
```

## Objects as Function
Objects can be made _callable_.
Use `__call__()` method.
```python
class Adder:
  def __init__(self, n):
    self.n = n
  def __call__(self, x):
    return self.n + x
```
Output:
```python
>>> plus_3 = Adder(3)
>>> plus_3(4)
7
```
You can check, whether an object is callable using function `callable()`.
```python
>>> callable(plus_3)
True
>>> callable(False)
False
```

Key Takeaways:
* Everything in Python is an object. Can assign them to variables, store them in structures, pass or return them to or from other functions.
* Can be nested. Can capture and carry some the parent function's state.
* Objects can be made callable.
