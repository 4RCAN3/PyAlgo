# PyAlgo

PyAlgo is a library for algorithm implementations using python, pull-requests are welcome for this project. Following are the set of rules to be followed for contributing to the project.

### Template

The following template should be used for making any module:

```python
'''
module for {brief working of module}
'''

def func(arguments: datatype):
    '''
    basic info about usage
    '''

    #your code goes here

    return result

'''
PyAlgo
{Name}, {Year}
'''
```

### Code Formatting

While making a module, keep the following things in mind and adhere to them:

- The datatype of argument of a function should be mentioned, and if there any default arguments, they should be mentioned as well.

```python
def func(num: int, arr: list, MOD: None):
    #your code goes here
    return result
```

- The code should be neat, along with proper whitespaces and logical variable names.
- Refrain from using external modules/libraries, try to use mathematical reasoning/logic and pre-defined data structures.
- Use brackets when there is any if-elif statements or while loop.

```python
while (True):

    if (flag == True):
        func()

    elif (flag == False):
        func_2()
```

- Naming of variables should be as follows:
  - `constant variables`: Capitalised (MOD = 10e9 + 7)
  - `functions`: separated by underscore (func_name)
  - `classes`: First letter capitalised (MyClass)

### Pull Requests

When making a pull request, the following should be in the description:

- What new changes have been made/working of the new module
- Check whether it follows the code formatting
- Create a test for the code using the unittest module in the `test` directory

> If the PR passes the the travis-ci build, it will be merged to the main branch.
