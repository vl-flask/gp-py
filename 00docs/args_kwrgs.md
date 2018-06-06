# Args and Kwargs (`*args` and `**kwargs`)

## Basic Example
```python
def foo(reqd, *args, **kwargs):
    print(reqd)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
```
Usage:
```python
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() missing 1 required positional argument: 'reqd'
>>> foo("abc")
abc
>>> foo("abc", 1,2,"bca")
abc
(1, 2, 'bca')
>>> foo("abc", 1,2,"bca", fname="Vassily", lname="Lapitsky")
abc
(1, 2, 'bca')
{'fname': 'Vassily', 'lname': 'Lapitsky'}
```

## Usage: Wrapper
Things like changing arguments for a function.
We can write some wrapper functions that modify or do snth to those arguments and then actually pass them on the original function.
```
def foo(x, *args, **kwargs):
    kwargs['name'] = "Alice"
    new_args = args + ('extra',)
    bar(x, *new_args, **kwargs)
```
Risks:
* Maintenance Nightmare

## Usage: Subclassing
You wanna extend the behavior of parent class, without having to replicate the full signature of its constructor in the child class.
And f.x. if you work with an API that changes outside
```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

def BlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'
```
