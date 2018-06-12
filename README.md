# threading_decorators

Decorators for easy threading in Python

## Usage

Use Threaded_Function as a decorator for any function

```python
import threading_decorators as ThD

@ThD.Threaded_Function
def foo(my_arg, my_keyword_arg=100):
    # Do something
    print(my_arg)
    for i in range(my_keyword_arg):
        # Do something else
        ThD.check_stop()
    print(i)
```

Then call the function to rut it inside a Thread

```python
foo('Test')
```

if check_stop() where used inside the function, then calling the stop method will stop the execution of the function at the next check_stop() point 

```python
foo.stop()
```
