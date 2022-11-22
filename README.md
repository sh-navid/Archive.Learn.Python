# Python Instructor

- **Disclaimer:** _The content of this repository is only for testing and training and is provided at the discretion of the author; So it may not be suitable for production or other conditions._
- [Install and Run](/lessons/python/installation/README.md) Python.
- [Examples](/lessons/python/examples/README.md)
- [Homeworks](/README-PYTHON-HOMEWORKS.md)

## Headings
- ![](-/n.png) [Introduction](./concepts/introduction/README.md)
- ![](-/n.png) [Syntax](./concepts/syntax/README.md)
- ![](-/n.png) [Variables](./concepts/variables/README.md)
- ![](-/p.png) [String](./concepts/strings/README.md)
- [Random](/lessons/python/concepts/random/general-random-functions.py)
   - `random(), randint(), shuffle(), choice()`
- <details>
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
- Debugging (break point)
- <details>
      <summary><strong>List</strong></summary>
      
      - Ordered, Changeable, Indexed, Allow Duplicate
      - [`access, assign, iterate, list(), .append(), .insert(), .remove(), del, .pop(), .copy(), .extend(), .clear(), len(), .count(), slice, join, unpack, in, .index(), .reverse(), .sort()`](/lessons/python/concepts/collections/list-access.py)
      </details>
- <details>
      <summary><strong>Tuple</strong></summary>
      
      - Ordered, Unchangeable, Indexed, Allow Duplicate
      - Tuples are **unchangeable**, or **immutable** so you cannot add or remove items from it
      - [`access, tuple with one item, tuple(), iterate, del completely, len(), .count(), slice, join, unpack, in, .index()`](/lessons/python/concepts/collections/tuple-access.py)
      </details>
- <details>
      <summary><strong>Set</strong></summary>
      
      - Unordered, Unchangeable (By index, But you can add/remove), Unindexed, No Duplicate
      - [`access, len(), set(), in, .add(), .update(), (.remove(), .discard(), .pop(), del), .copy(), .clear(), (.union(), intersection, difference, symmetric_difference), (disjoint, subset, superset)`](/lessons/python/concepts/collections/set-access.py)
      - [`frozenset()`](/lessons/python/concepts/collections/set-frozen.py)
      </details>
- <details>
      <summary><strong>Dictionary</strong></summary>
      
      - Ordered, Changeable, Key Value, No Duplicate
      - [`access, assign, .update(), dict(), .keys(), .values(), .items(), zip(), len(), .pop(), .popitem(), del, .clear(), .copy(), .fromkeys(), .setdefault())`](/lessons/python/concepts/collections/dict-access.py)
      </details>
- <details>
      <summary><strong>DataTypes</strong></summary>
      
      - Numbers: [`Integer, Float, Complex`](/lessons/python/concepts/data-types/data-type-number.py)
      - Sequence: [`String`](/lessons/python/concepts/data-types/data-type-string.py), [`Range`](/lessons/python/concepts/data-types/data-type-range.py), [`List`](/lessons/python/concepts/collections/list-access.py), [`Tuple`](/lessons/python/concepts/collections/tuple-access.py), `Bytes`, `ByteArray`
      - Set: [`Set`](/lessons/python/concepts/collections/set-access.py), [`FrozenSet`](/lessons/python/concepts/collections/set-frozen.py)
      - Map: [`Dictionary`](/lessons/python/concepts/collections/dict-access.py)
      - Nothing: `None`
      - Boolean: [`Boolean`](/lessons/python/concepts/boolean/boolean-concept.py)
      - Binary: [`Bytes, ByteArray, MemoryView`](/lessons/python/concepts/data-types/data-type-bytes.py)
      - `bytes` is immutable; however `bytearray` is mutable
      </details>
- Module
- Conversion, TypeCasting
- Input
- <details>
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
- [Comperhension](/lessons/python/concepts/collections/comperhension.py)
- Scope, Globals, Locals
    - [`locals(), globals()`](/lessons/python/concepts/variables/scope.py)
- [Read File, Write File](/lessons/python/examples/sample/file/read-write-file.py), [Pickle](/lessons/python/examples/sample/file/read-write-pickle.py)
- Math
- [Date, Time](/lessons/python/concepts/date-time/date-time.py)
- [Function, Method, Lambda](/lessons/python/concepts/object-oriented/types-of-methods.py)
- [OOP](/lessons/python/concepts/object-oriented/README.md)
    - Class, Object
    - Constructor
    - ToString, Representation
    - Methods
      - Object Method
      - Static Method
      - Class Method
    - Inheritance
    - Override
    - Overload
      - [Function Overloading](/lessons/python/concepts/object-oriented/function-overloading.py)
          -  Python does not support function overloading
      - [Operator Overloading](/lessons/python/concepts/operators/operator-overload.py) <sub>[OPTIONAL]</sub>
    - Getter, Setter ???
    - [Enum](/lessons/python/concepts/enum/color-enum.py)
- [Eval, Exec](/lessons/python/concepts/advanced/eval-exec.py)
- [`*argv`, `**kwargs`](/lessons/python/concepts/advanced/argv-kwargs.py)
- [Sys](/modules/sys/README.md)
- [OS](/modules/os/README.md)
- [Assertion](/lessons/python/concepts/advanced/simple-assertion.py)
- [Generator](/lessons/python/concepts/advanced/simple-generator.py)
----
- [Test](concepts/test/README.md)
- [PIP](/lessons/python/installation/README-PIP.md)
- [Decorator](/lessons/python/concepts/advanced/simple-decorator.py)
- [Reflection](/lessons/python/concepts/advanced/simple-reflection.py)
- [Regular Expression](/concepts/regex/README.md)
- [CSV](concepts/documents/csv/README.md)


### Optional
1. VENV
7. Exception
   1. Custom Exception
   2. Types of Errors
10. Meta
    1. Meta Classes
    2. Meta Programming
12. Iterator
    - [Iterator, Iterable](/lessons/python/concepts/advanced/simple-iterator.py)
    - [Custom Iterator](/lessons/python/concepts/advanced/custom-iterator.py)
13. Closure
14. [Descriptor](/lessons/python/concepts/advanced/simple-descriptor.py)
16. [Context Manager](/lessons/python/concepts/keywords/keywords-with.py)
17. [Regular Expression](/concepts/regex/README.md)
18. Socket [`client`](/lessons/python/examples/sample/socket/simple-socket-client.py), [`server`](/lessons/python/examples/sample/socket/simple-socket-server.py)
19. Data
    1.  SQL, NoSQL, ORM (SQLAlchemy)
    2.  JSON, CSV, XML, OWL, ...
20. Serialization, Deserialization


### Advanced
1. Dependency Injection
2. Inversion of Control
3. Message Passing
4. Multi Threading
5. Multi Processing
6. Semaphore, Lock, Mutex

## Modules, Packages, Libs, ...
- [**Sys**](/modules/sys/README.md)
- [**OS**](/modules/os/README.md)
- [**Tkinter**](/lessons/python/modules/tkinter/README.md)
- [**Turtle**](/lessons/python/modules/turtle/README.md)
- [**NumPy**](/lessons/python/modules/numpy/README.md)
- [**Pandas**](/lessons/python/modules/pandas/README.md)
- Matplotlib
- PyQT
- Kivy
- [**DJango**](/lessons/python/modules/django/README.md)
- [**Flask**](/lessons/python/modules/flask/README.md)
- Scrapy
- Selenium
- BeautifulSoup
- [**OpenCV**](/lessons/python/modules/opencv/README.md)
- Pillow
- **PyGame** ([1](/lessons/python/examples/sample/game_engine/simple-2d-game-part1.py),[2](/lessons/python/examples/sample/game_engine/simple-2d-game-part2.py),[3](/lessons/python/examples/sample/game_engine/simple-2d-game-part3.py),[4](/lessons/python/examples/sample/game_engine/simple-2d-game-part4.py))
- Open3D
- TF
- PyTorch
- Keras
- Scikit-learn
- SciPy
- Seaborn
- PyAutoGUI

## More
- [**AI**](lessons/ai/README.md)
- [**Web**](lessons/frontend/README.md)
- [**Linux** <sub>(Basic Concepts)</sub>](lessons/linux/README.md)
- [**Network** <sub>(Basic Concepts)</sub>](lessons/network/README.md)
- [**Security** <sub>(Basic Concepts)</sub>](lessons/security/README.md)
- [**SQL**](lessons/sql/README.md)