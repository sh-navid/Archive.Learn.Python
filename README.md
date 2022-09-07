# Python Instructor

- An article to complete the Python course.
- **Disclaimer:** _The content of this repository is only for testing and training and is provided at the discretion of the author; So it may not be suitable for production or other conditions._
- Check this [link](/lessons/python/installation/README.md) ([farsi](/lessons/python/installation/README-FARSI.md)) to install and run Python.

## Homework

- Check [this link](/README-PYTHON-HOMEWORKS.md)

## Examples

- Check [this link](/README-PYTHON-EXAMPLES.md)

## Headings

1. Introduction
1. Syntax
   - `pep8, naming, comments, indentation, ...`
1. Variables
1. [Strings](/lessons/python/concepts/string)
   - [`encode, decode`](/lessons/python/concepts/string/encode-string.py)
   - [`strip, lstrip, rstrip`](/lessons/python/concepts/string/trim-string.py)
   - [`join, concatenation`](/lessons/python/concepts/string/concat-string.py)
   - [`endswith, startswith, find, rfind, index, rindex`](/lessons/python/concepts/string/search-string.py)
   - [`translate, maketrans, format, format_map`](/lessons/python/concepts/string/format-string.py)
   - [`partition, rpartition, splitlines, split, slice`](/lessons/python/concepts/string/split-string.py)
   - [`(title, capitalize), (lower, upper, swapcase, casefold), (center, ljust, rjust)`](/lessons/python/concepts/string/audit-string.py)
   - [`in, (istitle, islower, isupper), isspace, isprintable, isidentifier, (isascii, isalpha), (isalnum, isnumeric, isdecimal, isdigit)`](/lessons/python/concepts/string/check-string.py)
   - [`zfill, count, replace, len, expandtabs, multi-line, loop-over-characters, reverse`](/lessons/python/concepts/string/other-string-functions.py)
   - [Scape Chars `\t \f \" \n \r \b \oct \hex`](/lessons/python/concepts/string/scape-chars.py)
2. [Random](/lessons/python/concepts/random/general-random-functions.py)
   - `random(), randint(), shuffle(), choice()`
3. [Operators](/lessons/python/concepts/operators)
   1. [Arithmetic](/lessons/python/concepts/operators/arithmetic-operators.py) `+ -` ,...
   2. [Assignment](/lessons/python/concepts/operators/assignment-operators.py) `= += -=` ,...
   3. [Comparison](/lessons/python/concepts/operators/comparison-operators.py) `== != >=` ,...
   4. [Logical](/lessons/python/concepts/operators/logical-operators.py) `and, or, not`
   5. [Identity](/lessons/python/concepts/operators/identity-operators.py) `is, is not`
   6. [Membership](/lessons/python/concepts/operators/membership-operators.py) `in, not in`
   7. [Bitwise](/lessons/python/concepts/operators/bitwise-operators.py) `& | ^ ~ << >>`
4. Debugging (break point)
5. List
   - Ordered, Changeable, Indexed, Allow Duplicate
   - [`access, assign, iterate, list(), .append(), .insert(), .remove(), del, .pop(), .copy(), .extend(), .clear(), len(), .count(), slice, join, unpack, in, .index(), .reverse(), .sort()`](/lessons/python/concepts/collections/list-access.py)
6. Tuple
   - Ordered, Unchangeable, Indexed, Allow Duplicate
   - Tuples are **unchangeable**, or **immutable** so you cannot add or remove items from it
   - [`access, tuple with one item, tuple(), iterate, del completely, len(), .count(), slice, join, unpack, in, .index()`](/lessons/python/concepts/collections/tuple-access.py)
7. Set, FrozenSet
   - Unordered, Unchangeable (By index, But you can add/remove), Unindexed, No Duplicate
   - [`access, len(), set(), in, .add(), .update(), (.remove(), .discard(), .pop(), del), .copy(), .clear(), (.union(), intersection, difference, symmetric_difference), (disjoint, subset, superset)`](/lessons/python/concepts/collections/set-access.py)
   - [`frozenset()`](/lessons/python/concepts/collections/set-frozen.py)
8. Dictionary
   - Ordered, Changeable, Key Value, No Duplicate
   - [`access, assign, .update(), dict(), .keys(), .values(), .items(), zip(), len(), .pop(), .popitem(), del, .clear(), .copy(), .fromkeys(), .setdefault())`](/lessons/python/concepts/collections/dict-access.py)
9. DataTypes
   - Numbers: [`Integer, Float, Complex`](/lessons/python/concepts/data-types/data-type-number.py)
   - Sequence: [`String`](/lessons/python/concepts/data-types/data-type-string.py), [`Range`](/lessons/python/concepts/data-types/data-type-range.py), [`List`](/lessons/python/concepts/collections/list-access.py), [`Tuple`](/lessons/python/concepts/collections/tuple-access.py.py), `Bytes`, `ByteArray`
   - Set: [`Set`](/lessons/python/concepts/collections/set-access.py), [`FrozenSet`](/lessons/python/concepts/collections/set-frozen.py)
   - Map: [`Dictionary`](/lessons/python/concepts/collections/dict-access.py)
   - Nothing: `None`
   - Boolean: [`Boolean`](/lessons/python/concepts/boolean/boolean-concept.py)
   - Binary: [`Bytes, ByteArray, MemoryView`](/lessons/python/concepts/data-types/data-type-bytes.py)
     - `bytes` is immutable; however `bytearray` is mutable
10. Module
11. Conversion, TypeCasting
12. Input
13. Keywords
   - [if, elif, else](/lessons/python/concepts/keywords/keywords-if-elif.py)
   - [for](/lessons/python/concepts/keywords/keywords-for.py)
   - [while, continue, break](/lessons/python/concepts/keywords/keywords-while.py)
   - [try, except, finally](/lessons/python/concepts/keywords/keywords-try-except.py)
   - [and, or, not, in, is](/lessons/python/concepts/keywords/keywords-and-or-not-in-is.py)
   - [import, from, as](/lessons/python/concepts/keywords/keywords-import.py)
   - [class, def, lambda, pass, return, del](/lessons/python/concepts/keywords/keywords-class-def-lambda-pass-ret-del.py)
   - [global, nonlocal](/lessons/python/concepts/keywords/keywords-scope.py)
   - [assert](/lessons/python/concepts/keywords/keywords-assert.py) <sub>[Optonal]</sub>, [raise](/lessons/python/concepts/keywords/keywords-raise.py) <sub>[Optonal]</sub>
   - [with](/lessons/python/concepts/keywords/keywords-with.py) <sub>[Optonal]</sub>
   - [yield](/lessons/python/concepts/keywords/keywords-yield.py) <sub>[Optonal]</sub>
14. [Function, Method, Lambda](/lessons/python/concepts/object-oriented/types-of-methods.py)
15. [Comperhension](/lessons/python/concepts/collections/comperhension.py)
16. Scope, Globals, Locals
   - [`locals(), globals()`](/lessons/python/concepts/variables/scope.py)
17. [Read File, Write File](/lessons/python/examples/read-write-file.py), [Pickle](/lessons/python/examples/read-write-pickle.py)
18. [Math](/lessons/python/examples/test-math.py)
19. Date
20. [OOP Concepts](/lessons/python/concepts/object-oriented/object-oriented.py)

### Optional

1. VENV
1. \_\_name\_\_
1. PIP
   - [`install, list, uninstall, freeze`, ...](/lessons/python/installation/README-PIP.md)
1. [Enum](/lessons/python/concepts/enum/color-enum.py)
2. Arguments
   - [`*argv`, `**kwargs`](/lessons/python/concepts/advanced/argv-kwargs.py)
3. [Eval, Exec](/lessons/python/concepts/advanced/eval-exec.py)
4. [Operator Overload](/lessons/python/concepts/operators/operator-overload.py)
5. Exception, Custom Exception, Types of Errors
6. [Assertion](/lessons/python/concepts/advanced/simple-assertion.py)
7. [Decorator](/lessons/python/concepts/advanced/simple-decorator.py)
8. MetaClasses, MetaProgramming
9. [Generator](/lessons/python/concepts/advanced/simple-generator.py)
10. Iterator
   - [Iterator, Iterable](/lessons/python/concepts/advanced/simple-iterator.py)
   - [Custom Iterator](/lessons/python/concepts/advanced/custom-iterator.py)
11. Closure
12. [Descriptor](/lessons/python/concepts/advanced/simple-descriptor.py)
13. [Reflection](/lessons/python/concepts/advanced/simple-reflection.py)
14. [Context Manager](/lessons/python/concepts/keywords/keywords-with.py)
15. Regular Expression
16. Socket [`client`](/lessons/python/examples/simple-socket-client.py), [`server`](/lessons/python/examples/simple-socket-server.py)
17. Web Service, Web Socket
18. SQL (MariaDB, Sqlite, ...)
19. NoSQL (MongoDB, Redis, ...)
1. ORM
1. Serialization, Deserialization
2. JSON, CSV, XML
3. Mutable vs Immutable in practice


## Modules, Packages, Libs, ...
- [**Tkinter**](/lessons/python/modules/tkinter/README.md)
- NumPy
- Pandas
- Matplotlib
- PyQT
- Kivy
- Django
- [**Flask**](/exercises/02/web/)
- Scrapy
- BeautifulSoup
- Selenium
- OpenCV
- Pillow
- **PyGame** ([1](/lessons/python/examples/simple-2d-game-part1.py),[2](/lessons/python/examples/simple-2d-game-part2.py),[3](/lessons/python/examples/simple-2d-game-part3.py),[4](/lessons/python/examples/simple-2d-game-part4.py))
- Open3D
- TF
- PyTorch
- Keras
- Scikit-learn
- NumPy
- Pandas
- SciPy
- Matplotlib
- Seaborn
- PyAutoGUI

## Roadmaps
- [**AI**](/README-AI.md)
- [**Web**](/README-WEB.md)
- [**Network** <sub>(Basic Concepts)</sub>](/README-NETWORK.md)