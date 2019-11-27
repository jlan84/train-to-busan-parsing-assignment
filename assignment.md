# Python Assignment

The goal of this assignment is to familiarize you with advanced Python 
features so that you can write cleaner, more efficient code.

## Part 1: Fill in some functions

Fill in the functions in `src/functions.py` according to their docstrings. Some 
"right answers" for these functions have already been written for you in 
`tests/test_functions.py`. You should complete the functions in 
`src/functions.py` so that they pass the tests, and you should complete the 
function tests (some are incomplete) in `tests/test_functions.py`.

You can test your functions in `src/functions.py` using the tests written in 
`tests/test_functions.py` using the `unittest` module.

Here's how:
```shell
$ python -m unittest -v tests/test_functions.py
```

Are you writing Pythonic code?  Check your style according to pep8 guidelines:

```shell
$ pycodestyle functions.py
```

Sometimes debugging code can be challenging.  One way to debug code is the 
[Python Debugger](https://docs.python.org/3/library/pdb.html).  As described
in this [Real Python blog](https://realpython.com/python-debugging-pdb/) one
of the easiest way to implement the debugger is to insert `breakpoint()` into
your code immediately above the code you're having trouble with.

Once you're entered the debugger, [here](https://realpython.com/python-debugging-pdb/#essential-pdb-commands)
is a list of useful debugger commands.  If you're having difficulty with the
debugger please ask an instructor.  The debugger can make the rest of the
course much easier for you!

## Part 2: Efficiency

The file `src/efficiency.py` contains some poorly written code. It works 
correctly, but it could be made more efficient.

Run and time each function.  We've created the data for you in the `data` folder. 
The `word_dict` is saved as a pickle object, which is a way of saving a Python 
object so you can reload it easily.

There are two data files, `alice.txt` and `articles.txt`. We recommend testing 
with `alice.txt` first as it's smaller and most of the inefficient code will 
take an unreasonably long time on the larger file (though you can verify this 
for yourself and just do Ctrl-C when you're ready to give up). After you make 
the code more efficient, try it with the larger file.

We're also going to be using `timeit` to get a measure of how long the function 
takes.

Here's how to execute and time a function in IPython:

```python
In [1]: import pickle

In [2]: import efficiency

In [3]: word_dict = pickle.load(open("../data/word_dict.pkl","rb"))

In [4]: timeit efficiency.find_new_words(open("../data/alice.txt"), word_dict)
10.3 s ± 626 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

Whenever you change the code in `efficiency.py` make sure to run this command 
in IPython:

```python
In [5]: import importlib

In [6]: importlib.reload(efficiency)
```

For `list_of_words` and `find_new_words` you should be able to get a *big* 
improvement with a minor change. For `get_average_score` and `find_high_valued_words` 
the speedup will be less impressive.

**For each function, do the following:**

1. Run `timeit` to get a measure of how well the original version does. Make note of this value.
2. Make your change to the file.
3. Run `timeit` again and make note of the improved runtime.
4. Write a comment next to each function with the runtime speedup and explain why your version is faster.

**These are all very small changes and may be tricky to spot. If you can't find the issue in 5-10 minutes, ask a neighbor or instructor for a hint.**


## Extra credit: A Python Script

You are given two files which contain reviews from two different sources. The files are in the `data` folder: `reviews1.txt` and `reviews2.txt`.

Take a look at the data. In the command line, this is especially useful if you have large files:

```shell
head data/reviews1.txt
```

Or even just look at the first line:

```shell
head -n 1 data/reviews 1.txt
```

The line `il-Yamo   5` means that restaurant `Yamo` was given a rating of `5` 
by user `il`. Don't read too much into the review values, this was randomly 
generated "data". All of the places are local favorites :)

You would like to know for each restaurant their average rating from each source. 
You will create a file with lines like this: `yamo,3.25,2.2`. The lines should 
be in *sorted order*. Make sure that you match the names even if their 
capitalization isn't the same. If a restaurant is in one file, but not the other, 
you should still include it and give a reasonable value for the missing number. 
You can see an example output in `example_out.csv`.

You should write a python script which can be run on the command line like this:

```shell
python src/script.py data/reviews1.txt data/reviews2.txt out.csv
```

Notes:

1. Use functions to make your code clean and easy to read. Nothing besides import 
statements and the main block (`if __name__ == '__main__':`) should be outside of functions.
2. Use the `argparse` module for getting input (it's a little cleaner than just 
using `sys.argv`). Look at the [documentation](https://docs.python.org/3/howto/argparse.html) 
to figure out how to use it.
3. Use a `defaultdict` for storing all the restaurant reviews.
4. For extra credit, use the `re` module for parsing the line ([documentation](https://docs.python.org/3/library).
5. You can compare your result to ours with: `diff out.csv example_out.csv`
