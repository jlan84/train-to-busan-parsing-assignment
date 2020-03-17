# Assignment overview

You're tasked with creating a text pre-processing pipeline for movie description 
clustering.  Your script should read in a movie description and write a condensed 
version that will be the input for another script that clusters the movie descriptions.  You 
aren't responsible for creating the clustering script.

Let's make the assignment more specific using an example. The `data` folder 
contains a Wikipedia movie description of the 2016 South Korean thriller  
**Train to Busan**.  The description is in the text file `train_to_busan_description.txt`.

<p align="center">
    <img width="300" src="./images/train_to_busan_poster.png">
</p>

<p align="center">source: Wikipedia</p>

You will create a script `src/description_parser.py` that takes as an input 
argument a text file (in this case `data/train_to_busan_description.txt`)
and writes a condensed version of the text file as output (in this case `parsed/train_to_busan.txt`).
Note that the three files mentioned above exist in different directories, as indicated
by the text preceding the forward slash:  
* `src/`  The source directory where Python scripts (`*.py`) are stored.  
* `data/` The directory where the text descriptions (`*.txt`) are stored.
* `parsed/` The directory where parsed text versions (`*.txt`) of the movie descriptions will be stored.
            Your script will create this directory if it doesn't already exist.

The script needs to run from Terminal (the command line) in the root directory of the project like so:  
```bash
$ python src/description_parser.py data/train_to_busan_description.txt  
```

This results in the creation of `parsed/train_to_busan.txt`. Showing just the first
three lines, the images below shows how your `src/description_parser.py` should tranform the 
text from the description to the parsed version.

`data/train_to_busan_description.txt`  
![image][image]

`parsed/train_to_busan.txt`  
![image][image]

As you can see, `train_to_busan.txt` is a line-by-line transcription of the 
`train_to_busan_description.txt` but with the following modifications:
* it's in a different directory (`parsed` instead of `data`)
* all the text has been lower-cased
* punctuation has been removed
* words that are common (e.g "at", "the", "for") have been removed
* people's names have been replaced with "person"

This assigment will walk you through creating this application.

## Part 1 - Explore the data (and Introduction to Jupyter Notebooks)  

Before jumping to making the application we should first get a sense for what the 
data are like.  In this case, you can simply navigate to the text file and read it
using the command line utility `less`.  Try it:  
```bash
$ less train_to_busan_description.txt
```

But let's it explore it in a more quantitative way using Python.  Data exploration
is a perfect use-case for Jupyter Notebooks.

### Jupyter Notebooks
As described in the [Jupyter Notebook Quickstart Guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html):
> Jupyter Notebook documents (or “notebooks”, all lower case) are documents produced by 
> the Jupyter Notebook App, which contain both computer code (e.g. Python) and 
> rich text elements (paragraph, equations, figures, links, etc…). Notebook 
> documents are both human-readable documents containing the analysis description 
> and the results (figures, tables, etc..) as well as executable documents which 
> can be run to perform data analysis. 

Jupyter Notebooks run the IPython interactive kernel in "Code" cells, but then allow for 
text formatting and use of sophisticated Latex rendering using MathJax (see these [examples](https://www.tuhh.de/MathJax/test/sample.html)) in "Markdown" cells.  This makes them a good candidate for
Python lectures to technical audiences.

One distinguishing characteristic of Jupyter Notebooks is that code is executed in cells.
Therefore you can execute a bit of code, and then in the next or (_horror_) preceding cell
query the results of code execution.

Jupyter Notebooks are also visually-pleasing graphical environments.  Plots show up naturally.

Their non-linear, iterative, cellular, and visual nature make Jupyter Notebooks a powerful
tool for rapid data exploration and visualization.  However, these same characteristics (as
well as poor git tracking/merging) sabotage their use as a way to create a sequential operating
script executable from the command line.

Very often an project will start with exploration in a Jupyter Notebook but end with an
application deployed as a script.

Let's demonstrate the use of a Jupyter Notebook to explore the `train_to_busan_description.txt`
file.  In Terminal, navigate to the `notebooks` folder of this repository.  Once inside,
open the Jupyter notebook inside and execute cell-by-cell sequentially using `shift-enter`,
carefully reading the comments and observing the syntax along the way.  Don't be afraid to add
cells and perform your own exploration and analysis.

Here's how you open a Jupyter Notebook from the command line:  
```bash
$ jupyter notebook explore_movie_description.ipynb
```

You know a file is Jupyter Notebook from its `*.ipynb` file extension.

## Part 2 - Fill in the `text_parsing_functions.py` functions  

Now that you've explored the text and gained some familiarity with functions (in the
Jupyter Notebook) that could be used to clean it, let's transition to writing scripts for
the application.

The `description_parser.py` file will need text parsing functions to condense
the movie descriptions.  These functions _could_ be written in the `description_parser.py` 
file itself, but these text parsing functions could be useful in other applications too.
So let's develop and test the text parsing functions in a separate script - `text_parsing_functions.py` -
and then once they are working as desired _import_ them into the `description_parser.py` file 
for use.

1.  One

Goal: Write a Python application that takes a text file as an argument and parses
it line-by-line into text tokens of interest.  As the
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
4. For extra credit, use the `re` module for parsing the line ([documentation](https://docs.python.org/3/library/re.html)).
5. You can compare your result to ours with: `diff out.csv example_out.csv`
