# mypy
 -  reference : https://github.com/python/mypy

### overview
 - static type checker for Python, you can find bugs without running Python code.  
 - you can use mypy with adding type hints.  

### example
 - python file to be checked
 ```py:sample.py
 def subtract(a : int, b : int) -> int:
    return a - b

 subtract(1, '2')
 ```
 - check result
 ```
 (command)
 mypy try_mypy.py

 (output)
 try_mypy.py:4: error: Argument 2 to "subtract" has incompatible type "str"; expected "int"  [arg-type]
 Found 1 error in 1 file (checked 1 source file)

 ```
 
 - __if there is no type hint, mypy can't detect any errors__
 - because mypy will not type check dynamically typed functions by default.
 - you can pick whether you want function to be checked dynamically or statically, so this feature is helpful 

#### cheat seat
 - https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#cheat-sheet-py3