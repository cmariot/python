# My-minipack Package

## Progress :

Progress bar generator
This function displays a progress bar for an iterable object and yields its items.

Parameters :
- iterable (list) : An iterable object.
- length (int, optional) : The length of the progress bar. Default is 50.
- fill (str, optional) : The character used to fill the progress bar.
- print_end (str, optional) : The character used to separate printed output.

Returns :
- generator: A generator that yields the items of the iterable object.

Example usage :

``` python
from my_minipack.progress import ft_progress

for i in ft_progress(range(100)):
    time.sleep(0.1)
```

## Logger :

This is a decorator that logs into a file called machine.log :
- the user who executed it
- the name of the function
- the time of execution of a function

Example usage:

``` python
from my_minipack.logger import log

@log
def your_function():
    your code ...
 ```
