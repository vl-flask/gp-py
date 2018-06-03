# Functions as First-Class Objects

Original [here](https://dbader.org/blog/python-first-class-functions).  

# Basic Function and Usage
Function [`yell(text)`](first_class_func/yell.py)
```python
def yell(text):
    return text.upper() + "!"
```
Usage:
```
>>> yell("hello")
'HELLO!'
```
Now, there is a function object, and `yell` only references it.  
We can make more references to the same function object.
```
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
...
>>> def whisper(text):
...     return text.lower() + "..."
...
>>> def greet(func):
...     greeting = func("Hi, I'm a Python program")
...     print(greeting)
...
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
