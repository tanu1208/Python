# [INF4331](https://github.com/UiO-INF3331/INF4331-tanusanr) - Assignment 5

Regular expression operations and syntax highlighting.
All files in the example are in the folder.

## How to run the files
The [example files](https://github.com/UiO-INF3331/INF4331-tanusanr/tree/master/assignment5/example%20files) folder contains test files that can be used.

### Task 5.1 - [Highlighter.py](https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment5/highlighter.py)
```
python3 highlighter.py <syntaxfile> <themefile> <sourcefile_to_color>
```
**example:**
```
python3 highlighter.py example\ files/naython.syntax example\ files/naython.theme example\ files/hello.ny
```
### Task 5.2 - Syntax for python
The color scheme selected is based of Sublime Text 3 colors (python2.theme is just random).
```
python3 highlighter.py <syntaxfile> <themefile> <sourcefile_to_color>
```
**example:**
```
python3 highlighter.py python.syntax python.theme demo.py

python3 highlighter.py python.syntax python2.theme demo.py
```

### Task 5.3 - Syntax for java
The color scheme selected is based of Sublime Text 3 colors.
```
python3 python3 highlighter.py <syntaxfile> <themefile> <sourcefile_to_color>
```
**example:**
```
python3 highlighter.py java.syntax java.theme Test.java
```

### Task 5.4 - Grep
This task is done with the assumption, one is supposed to make a grep-like utility, ref piazza post: https://piazza.com/class/jkuzyo6bksl2fm?cid=334
You get the lines containing the word printed out. If flag (--highlight) is sent with, you get the output colored.
The words in the sentence are colored randomly, while each "grep" word will have one color.

[search_words.txt](https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment5/search_words.txt) - contains the words the user wants to grep.
[random_text.txt](https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment5/random_text.txt) - contains the tekst to search.
```
python3 grep.py <text_file> <words_to_search> <--highlight>(optional)
```
**examples:**
```
python3 grep.py random_text.txt search_words.txt

or

python3 grep.py random_text.txt search_words.txt --highlight
```

### Task 5.5 - Superdiff
This will create the [diff_output.txt](https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment5/diff_output.txt) file. This file contains the differences from each file.
```
python3 diff.py <original_file> <modified_file>
```
**example:**
```
python3 diff.py demo.py demo2diff.py
```

### Task 5.6 - Coloring diff
Only coloring the + and -, to indentify which lines have been added and removed.
```
python3 highlighter.py <syntaxfile> <themefile> <sourcefile_to_color>
```
**example:**
```
python3 highlighter.py diff.syntax diff.theme diff_output.txt
```

## Built With

* [Re](https://docs.python.org/3/library/re.html) - The documentation for Regular expression operations.
* [Bash color tips](https://misc.flogisoft.com/bash/tip_colors_and_formatting) - Tips for coloring in bash.
* [Regex101](https://regex101.com/) - Nice for checking the regular expression.
* [Random](https://docs.python.org/3/library/random.html) - Used for randomly selecting color for grep
