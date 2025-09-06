**__pycache__**
The `__pycache__` folder is automatically created by Python when you run a Python program. It stores compiled bytecode files (with a `.pyc` extension) for your Python scripts. This helps Python start programs faster by avoiding recompilation each time you run the code.

**Why is it created?**
- To improve performance by caching the compiled version of Python files.
- To separate source code (`.py` files) from compiled bytecode (`.pyc` files).

**When is it created?**
- Whenever you import a Python module or run a script, Python checks if a compiled version exists in `__pycache__`. If not, it creates the folder and the necessary `.pyc` files.
- You don't need to manually create or manage this folder; Python handles it automatically.