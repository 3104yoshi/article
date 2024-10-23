# Ruff


- it is said extremely fast python linter and code formatter
- reference : https://docs.astral.sh/ruff/

### install

```
pip install ruff
```

### example

sample.py contains following codes

```python
import os

def subtract(a : int, b : int):
    return a - b

subtract(1, '2')
```

we can run the Ruff linter

```python
ruff check sample.py

try_mypy.py:1:8: F401 [*] `os` imported but unused
  |
1 | import os
  |        ^^ F401
2 |
3 | def subtract(a : int, b : int):
  |
  = help: Remove unused import: `os`

Found 1 error.
[*] 1 fixable with the `--fix` option.
```

we can resolve above error by adding --fix option

```python
ruff check sample.py --fix

Found 1 error (1 fixed, 0 remaining).
```


### comparison with other static code analyser

static code analyse include some roles as below.

- linter

  - Ruff, flake8, Pylint, ...
- type checker

  - Mypy, Pyright, Pyre, ...
- security check

  - Bandit,...

This means you need to decide which analyser to use based on your situation.  

Actually, it is recommended in Ruff docs that you use Ruff as linter with type checker like Mypy or so. (ref: [FAQ | Ruff](https://docs.astral.sh/ruff/faq/#how-does-ruff-compare-to-mypy-or-pyright-or-pyre))
