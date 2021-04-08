# Match-Ref
## Top-Level Variable References For Python's `match`

![zero dependencies](https://img.shields.io/badge/dependencies-0-orange)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/match-ref)
![PyPI](https://img.shields.io/pypi/v/match-ref)

---------------

## Objective

This library provides a convenient interface to variables in the local and global namespaces, using
qualified (dotted) names.

Python **3.10** introduced the [`match`-`case` structure](https://www.python.org/dev/peps/pep-0634/)
which allows you to write flow control code like this:

```python
my_choice = input("Your choice: ")
fruit_on_sale = "peach"

match my_choice:
    case "apple": print("Delivering an apple.")
    case "banana": print("Delivering a banana.")
    case fruit_on_sale:
        print("Good choice!")
```

If you now entered a value like `tomato`, he output would be `fruit_on_sale`. This is, because
`fruit_on_sale` is considered a [placeholder/capture pattern](https://www.python.org/dev/peps/pep-0634/#id16) and not a reference to a variable.

Therefore, we need another way to reference variables. We can accomplish this using dotted names (i.e. `fruit_data.fruit_on_sale`, because Python does not interpret these names as placeholders.

## Installation

You can install this package using `pip` :
- `pip install match-ref` on all platforms, if available
- `python3 -m pip install match-ref` on Unix
- `py -m pip install match-ref` on Windows

## Usage

```python
from matchref import ref

my_choice = "banana"
fruit_on_sale = "peach"
match my_choice:
    case ref.fruit_on_sale: print("Good choice!")
```

You can use the `ref` helper to resolve all variables in the current **local** and **global** namespaces which you could usually reference without using a dotted name.

You can use `ref.any_local_or_global_variable_name` in any expression, not only inside `case` conditions, if you need to.

Only value retrieval is supported, as attribute-setting is not the purpose of this library.

## How does this work?

`ref` is the default instance of the `ScopeReference` class, defined in match-ref. It has a method `__getattr__` which gets called whenever you request an attribute of `ref`. This method then starts looking up the local namespace it was called from (your script or your function) and, if it doesn't find the variable you're looking for, continues searching the global namespace as well.

If it doesn't find the variable you are looking for, the following error is being raised:
```
ValueError: referenced name '...' is not defined
```
