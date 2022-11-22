# Python
## Strings
- Strip (Trim)
    - ![](../../-/1.png) [`.strip()`](trim-string.py)
    - ![](../../-/2.png) [`.lstrip()`](trim-string.py)
    - ![](../../-/2.png) [`.rstrip()`](trim-string.py)
- Concat
    - ![](../../-/1.png) [Concatenation](concat-string.py)
        > `print("Hello" + " " + "World")`
    - ![](../../-/2.png) [`.join()`](join-string.py)
- Search
    - ![](../../-/1.png) [`in`](search-in.py)
    - ![](../../-/1.png) [`.endswith()`](search-start-end.py)
    - ![](../../-/1.png) [`.startswith()`](search-start-end.py)
    - ![](../../-/1.png) [`.find()`](search-string.py)
    - ![](../../-/2.png) [`.rfind()`](search-string.py)
    - ![](../../-/2.png) [`.index()`](search-string.py)
    - ![](../../-/2.png) [`.rindex()`](search-string.py)
- Mapping
    - ![](../../-/1.png) [`.format()`](format-string.py)
    - ![](../../-/2.png) `.format_map()`
    - ![](../../-/2.png) [`.translate(), .maketrans()`](trans-maketrans-string.py)
- Split
    - ![](../../-/1.png) [`.partition()`](split-string.py)
    - ![](../../-/2.png) [`.rpartition()`](split-string.py)
    - ![](../../-/2.png) [`.splitlines()`](split-string.py)
    - ![](../../-/1.png) [`.split()`](split-string.py)
    - ![](../../-/1.png) [`.slice()`](split-string.py)
- Formatting
    - Change Case
        - ![](../../-/2.png) [`.capitalize()`](audit-string.py)
        - ![](../../-/1.png) [`.lower()`](audit-string.py)
        - ![](../../-/1.png) [`.upper()`](audit-string.py)
        - ![](../../-/2.png) [`.title()`](audit-string.py)
        - ![](../../-/2.png) [`.swapcase()`](audit-string.py)
        - ![](../../-/3.png) [`.casefold()`](audit-string.py)
    - Direction
        - ![](../../-/1.png) [`.center()`](audit-string.py)
        - ![](../../-/1.png) [`.ljust()`](audit-string.py)
        - ![](../../-/1.png) [`.rjust()`](audit-string.py)
- Checking
    > To check the character status of a text. For example, whether all are written in capital or small letters, or whether the characters are numeric or not?
    - Check Formatting
        - ![](../../-/2.png) [`.istitle()`](check-string.py)
        - ![](../../-/2.png) [`.islower()`](check-string.py)
        - ![](../../-/2.png) [`.isupper()`](check-string.py)
    - Check Alpha
        - ![](../../-/2.png) [`.isascii()`](check-string.py)
        - ![](../../-/2.png) [`.isalpha()`](check-string.py)
    - Check Number
        - ![](../../-/2.png) [`.isalnum()`](check-string.py)
        - ![](../../-/2.png) [`.isnumeric()`](check-string.py)
        - ![](../../-/2.png) [`.isdecimal()`](check-string.py)
        - ![](../../-/2.png) [`.isdigit()`](check-string.py)
    - Check Other
        - ![](../../-/2.png) [`.isspace()`](check-string.py)
        - ![](../../-/2.png) [`.isprintable()`](check-string.py)
        - ![](../../-/3.png) [`.isidentifier()`](check-string.py)
- Encode
    - ![](../../-/2.png) [`.encode()`](encode-string.py)
    - ![](../../-/2.png) [`.decode()`](encode-string.py)
- Other
    - ![](../../-/1.png) [`Multi-line text`](other-string-multi-line.py)
    - ![](../../-/1.png) [`Loop over characters`](other-string-loop-over.py)
    - ![](../../-/1.png) [`Reverse`](other-string-reverse.py)
        > Reverse a text; for example to change `Hello` to `olleH`
    - ![](../../-/1.png) [`len()`](other-string-len.py)
        > Counting the total number of characters in a text. In fact, the size of a text.
    - ![](../../-/1.png) [`.count()`](other-string-count.py)
        > Counting the number of occurrences of a specific character in a text
    - ![](../../-/1.png) [`.replace()`](other-string-replace.py)
        > Change part of a string with another text
    - ![](../../-/2.png) [`.zfill()`](other-string-zfill.py)
        > Put zeros before a text something like this: `000000000000000hello`
    - ![](../../-/2.png) [`.expandtabs()`](other-string-functions.py)
        > Default tab is 4 spaces but we can expand it
- Scape Chars 
    - ![](../../-/2.png) [`\t \f \" \n \r \b \oct \hex`](scape-chars.py)