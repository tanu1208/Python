# [INF4331](https://github.com/UiO-INF3331/INF4331-tanusanr) - Assignment 3

Basic Python programming. 

## Getting Started

There is no set up, you only need to run the python files with python3.

```
python3 wc.py * or python3 wc.py "filename"

python3 test_complex.py
```

## Running the tests

The tests run automaticly when you run the "test_complex" file.

```
python3 test_complex.py
```

### Info

I had some difficulties in the beginning, since I declared the imaginary and real number as "a" and "b", which didn't let me add my Complex numbers with pythons complex number. After a lot of knoting, I found out that the program checks this itself if you declare the real number as "real" and imaginary as "imag". As you can see on the earlier commits you can see the code difference, it should work properly now.

### Test cases

The test cases are broad, I test with only my Complex in the calculations. My Complex with pythons complex, regular numbers with my Complex or regular numbers with pythons complex. I even change the order of the equations and I have used assertEqual, assertNotEqual and just assert. I also wrote the test cases with pythons unittest, se link below.

## Built With

* [Unittest](https://docs.python.org/3/library/unittest.html) - The testing framework used
* [Math](https://maven.apache.org/) - The math framework used for mathematical functions