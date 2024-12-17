## Questions:

1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>
2.  What is the difference between the continue and break statements in Python?
3. Can you explain the difference between for loop and while loop?
4. How would you implement a nested for loop system? Provide an example.

## Homeworks:

**1.** Return uncommon elements of lists. Order of elements does not matter.
```
input:
    list1 = [1, 1, 2]
    list2 = [2, 3, 4]
output: [1, 1, 3, 4]
```

```
input:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
output: [1, 2, 3, 4, 5, 6]
```

```
input:
    list1 = [1, 1, 2, 3, 4, 2]
    list2 = [1, 3, 4, 5]
output: [2, 2, 5]
```

**2.** Print the square of each number which is less than `n` on a separate line.

```
input: n = 5
output:
    1
    4
    9
    16
```

**3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

```
input: hello
output: hel_lo
```

```
input: assalom
output: ass_alom
```

```
input: abcabcdabcdeabcdefabcdefg
output: abc_abcd_abcdeab_cdef_abcdefg
```


**4. Number Guessing Game**
Create a simple number guessing game.
The computer randomly selects a number between 1 and 100. The player has 10 attempts to guess it. If the guess is high, print "Too high!". If the guess is low, print "Too low!". If they guess correctly, print "You guessed it right!" and exit the loop.

>Hint: Use Python’s `random.randint()` to generate the number.

