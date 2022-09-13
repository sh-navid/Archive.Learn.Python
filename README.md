# Python Instructor

- An article to complete the Python course.
- **Disclaimer:** _The content of this repository is only for testing and training and is provided at the discretion of the author; So it may not be suitable for production or other conditions._
- Check this [link](/lessons/python/installation/README.md) ([farsi](/lessons/python/installation/README-FARSI.md)) to install and run Python.

## Python Code Examples
- [Python micro code examples](/lessons/python/examples/README.md)ss

## Homework

- Check [this link](/README-PYTHON-HOMEWORKS.md)

## Headings
1. Introduction
1. Syntax
   - `pep8, naming, comments, indentation, ...`
1. Variables
1. <details>
   <summary><strong>String</strong></summary>

   - [Strings](/lessons/python/concepts/string)
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
   </details>
2. [Random](/lessons/python/concepts/random/general-random-functions.py)
   - `random(), randint(), shuffle(), choice()`
3. <details>
      <summary><strong>Operators</strong></summary>

      - [Operators](/lessons/python/concepts/operators)
      1. [Arithmetic](/lessons/python/concepts/operators/arithmetic-operators.py) `+ -` ,...
      2. [Assignment](/lessons/python/concepts/operators/assignment-operators.py) `= += -=` ,...
      3. [Comparison](/lessons/python/concepts/operators/comparison-operators.py) `== != >=` ,...
      4. [Logical](/lessons/python/concepts/operators/logical-operators.py) `and, or, not`
      5. [Identity](/lessons/python/concepts/operators/identity-operators.py) `is, is not`
      6. [Membership](/lessons/python/concepts/operators/membership-operators.py) `in, not in`
      7. [Bitwise](/lessons/python/concepts/operators/bitwise-operators.py) `& | ^ ~ << >>`
      </details>
4. Debugging (break point)
5. <details>
      <summary><strong>List</strong></summary>
      
      - Ordered, Changeable, Indexed, Allow Duplicate
      - [`access, assign, iterate, list(), .append(), .insert(), .remove(), del, .pop(), .copy(), .extend(), .clear(), len(), .count(), slice, join, unpack, in, .index(), .reverse(), .sort()`](/lessons/python/concepts/collections/list-access.py)
      </details>
6. <details>
      <summary><strong>Tuple</strong></summary>
      
      - Ordered, Unchangeable, Indexed, Allow Duplicate
      - Tuples are **unchangeable**, or **immutable** so you cannot add or remove items from it
      - [`access, tuple with one item, tuple(), iterate, del completely, len(), .count(), slice, join, unpack, in, .index()`](/lessons/python/concepts/collections/tuple-access.py)
      </details>
7. <details>
      <summary><strong>Set</strong></summary>
      
      - Unordered, Unchangeable (By index, But you can add/remove), Unindexed, No Duplicate
      - [`access, len(), set(), in, .add(), .update(), (.remove(), .discard(), .pop(), del), .copy(), .clear(), (.union(), intersection, difference, symmetric_difference), (disjoint, subset, superset)`](/lessons/python/concepts/collections/set-access.py)
      - [`frozenset()`](/lessons/python/concepts/collections/set-frozen.py)
      </details>
8. <details>
      <summary><strong>Dictionary</strong></summary>
      
      - Ordered, Changeable, Key Value, No Duplicate
      - [`access, assign, .update(), dict(), .keys(), .values(), .items(), zip(), len(), .pop(), .popitem(), del, .clear(), .copy(), .fromkeys(), .setdefault())`](/lessons/python/concepts/collections/dict-access.py)
      </details>
9.  <details>
      <summary><strong>DataTypes</strong></summary>
      
      - Numbers: [`Integer, Float, Complex`](/lessons/python/concepts/data-types/data-type-number.py)
      - Sequence: [`String`](/lessons/python/concepts/data-types/data-type-string.py), [`Range`](/lessons/python/concepts/data-types/data-type-range.py), [`List`](/lessons/python/concepts/collections/list-access.py), [`Tuple`](/lessons/python/concepts/collections/tuple-access.py.py), `Bytes`, `ByteArray`
      - Set: [`Set`](/lessons/python/concepts/collections/set-access.py), [`FrozenSet`](/lessons/python/concepts/collections/set-frozen.py)
      - Map: [`Dictionary`](/lessons/python/concepts/collections/dict-access.py)
      - Nothing: `None`
      - Boolean: [`Boolean`](/lessons/python/concepts/boolean/boolean-concept.py)
      - Binary: [`Bytes, ByteArray, MemoryView`](/lessons/python/concepts/data-types/data-type-bytes.py)
      - `bytes` is immutable; however `bytearray` is mutable
      </details>
10. Module
11. Conversion, TypeCasting
12. Input
13. <details>
      <summary><strong>Keywords</strong></summary>

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
      </details>
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
2. PIP
    - [`install, list, uninstall, freeze`, ...](/lessons/python/installation/README-PIP.md)
3. [Enum](/lessons/python/concepts/enum/color-enum.py)
4. Arguments
    - [`*argv`, `**kwargs`](/lessons/python/concepts/advanced/argv-kwargs.py)
5. [Eval, Exec](/lessons/python/concepts/advanced/eval-exec.py)
6. [Operator Overload](/lessons/python/concepts/operators/operator-overload.py)
7. Exception, Custom Exception, Types of Errors
8. [Assertion](/lessons/python/concepts/advanced/simple-assertion.py)
9. [Decorator](/lessons/python/concepts/advanced/simple-decorator.py)
10. MetaClasses, MetaProgramming
11. [Generator](/lessons/python/concepts/advanced/simple-generator.py)
12. Iterator
    - [Iterator, Iterable](/lessons/python/concepts/advanced/simple-iterator.py)
    - [Custom Iterator](/lessons/python/concepts/advanced/custom-iterator.py)
13. Closure
14. [Descriptor](/lessons/python/concepts/advanced/simple-descriptor.py)
15. [Reflection](/lessons/python/concepts/advanced/simple-reflection.py)
16. [Context Manager](/lessons/python/concepts/keywords/keywords-with.py)
17. Regular Expression
18. Socket [`client`](/lessons/python/examples/simple-socket-client.py), [`server`](/lessons/python/examples/simple-socket-server.py)
19. Web Service, Web Socket
20. SQL (MariaDB, Sqlite, ...)
21. NoSQL (MongoDB, Redis, ...)
22. ORM
23. Serialization, Deserialization
24. JSON, CSV, XML
25. Mutable vs Immutable in practice
26. Multi Thread
27. Multi Process


## Modules, Packages, Libs, ...
- [**Tkinter**](/lessons/python/modules/tkinter/README.md)
- [**Turtle**](/lessons/python/modules/turtle/README.md)
- [**NumPy**](/lessons/python/modules/numpy/README.md)
- Pandas
- Matplotlib
- PyQT
- Kivy
- DJango
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
- SciPy
- Seaborn
- PyAutoGUI

## Know More About
- [**AI**](/README-AI.md)
- [**Web**](/README-WEB.md)
- [**Linux** <sub>(Basic Concepts)</sub>](/README-LINUX.md)
- [**Network** <sub>(Basic Concepts)</sub>](/README-NETWORK.md)
- [**Security** <sub>(Basic Concepts)</sub>](/README-SECURITY.md)
- [**SQL**](/README-SQL.md)