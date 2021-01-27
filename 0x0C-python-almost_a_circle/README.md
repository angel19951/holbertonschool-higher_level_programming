# 0x0C. Python - Almost a circle

Project will review everything about Python:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

New concepts:
- args and kwargs
- Serialization/Deserialization
- JSON
## Learning objectives:
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Python Scripts:
- Editor: Nvim
- First line of file:
```python
#!/usr/bin/python3
```
- All files made executable using:
```bash
alias epy="chmdo u+x *.py"
$epy

or

chmod u+x *.py
```

- Linter (PEP 8 style):
```bash
pep8 <filename>
```

## Python unittest:
- Editor: Nvim
- All files present in the tests/ folder
- All test executes with:
```bash
python3 -m unittest discover test
```
and
```bash
python3 -m unittest test/test_models/test_base.py
```
