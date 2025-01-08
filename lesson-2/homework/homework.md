# Class 1 - Homeworks

## Topic: Numeric Data Types, int, float, complex. Numeric Operations, Assignment operators, Variables, Augmented Assignment, print(), input()

## Exercises

1. Create an integer `x` with the value 15 and print it.
2. Convert the string `'42'` to an integer and print the result.
3. Write code to convert the string `'3.14'` to a float.
4. Create a complex number `z` with a real part of 7 and an imaginary part of 5. Print its real and imaginary parts.
5. Perform floor division on `23` by `7` and print the result.
6. Find the remainder when `29` is divided by `6` and print the result.
7. Calculate `4` to the power of `3` in two different ways and print the results.
8. Use `divmod()` to divide `45` by `8` and print the quotient and remainder.
9. Write code to create a float number in scientific notation that represents `3.6 x 10^4`. Print the value.
10. Convert the binary string `'1101'` to an integer and print it.
11. Convert the hexadecimal string `'2A'` to an integer and print the result.
12. Create a long integer `x` representing one billion using underscores for readability. Print the value.
13. Get user input for their age and convert it to an integer. Print the age.
14. Ask the user to input a number, convert it to a float, and print its square.
15. Calculate the absolute difference between `x = 9` and `y = 14`. Print the result.
16. Create a variable `my_float` with the value `3.5` and increment it by `1.2` using augmented assignment. Print the result.
17. Multiply two complex numbers `(3 + 4j)` and `(1 - 2j)`. Print the result.
18. Write a program that calculates the area of a circle given the radius as user input. Use `float` for calculations.
19. Ask the user to input a temperature in Celsius and convert it to Fahrenheit. Print the result.
20. Create a variable `result` and set it to `1`. Multiply `result` by `5` using augmented assignment. Print the result.
21. Create an integer from the octal string `'57'` and print the result.
22. Ask the user to input two numbers, divide the first by the second, and print the result as a float.
23. Write a program to calculate the perimeter of a rectangle given its width and height as input.
24. Create a variable `my_var` with the value `10` and decrease it by `3` using augmented assignment. Print the result.
25. Use the `pow()` function to calculate `7^4` and print the result.

## Topic: Comments, Strings

## Exercises

1. Create a string variable `name` with the value 'Alice' and print it.
2. Convert the number `25` to a string and print the result.
3. Create a multi-line string using triple quotes and print it.
4. Use escape sequences to print the following: `Hello\World` and `Hello\nWorld`.
5. Create a string that contains both single and double quotes, such as: `She said, "It's fine."`. Print it.
6. Concatenate the strings 'Hello' and 'World' with a space in between and print the result.
7. Write a program to create a new string made of an input string’s first, middle, and last character.
   Input:

   ```python
   name = "David"
   ```

   Output:

   ```bash
   Dvd
   ```

8. Write a function that takes a string and returns it reversed.
   Input:

   ```python
   name = "David"
   ```

   Output:

   ```bash
   divaD
   ```

9. Given the string `s = "Hello, World!"`, extract the substring `"World"` using slicing.
10. Given the string `s = "Python Programming"`, extract the last 5 characters using negative indexing.
11. Given the string `s = "abcdefg"`, extract every second character starting from the first one (output: `"aceg"`).
12. Given the string `s = "Hello, World!"`, extract the substring `"lo, W"` starting from index 3 and ending at index 9.
13. Given the string `s = "MAAB ACADEMY"`, extract the first 4 characters.
14. Given the string `s = "Data Engineering"`, extract the substring starting from index 5 to the end.
15. Given the string `s = "abcdefgh"`, extract every third character.
16. Given the string `s = "Programming"`, extract all characters except the last one.
17. Given the string `s = "Python Programming"`, extract the substring `"yhn rg"` using a step of 3.
18. Given the string `s = "Machine Learning"`, extract the last 7 characters using negative indexing.
19. Given the string `s = "ReverseMe"`, extract the whole string in reverse using slicing.
20. Given the string `s = "hello, world!"`, capitalize the first letter of the string and return the result.
21. Given the string `s = "PYTHON IS FUN"`, convert all characters to lowercase.
22. Given the string `s = "data science"`, convert all characters to uppercase.
23. Given the string `s = "Python Is Awesome"`, swap the case of all characters (i.e., convert lowercase to uppercase and vice versa).
24. Given the string `s = "hello world, this is python"`, convert the string to title case where each word begins with an uppercase letter.
25. Given the string `s = "Python"`, center the string to a width of 20 characters, using the \* character as padding.
26. Given the string `s = "Data Science"`, left-justify the string to a width of 20 characters, using - as the padding character.
27. Given the string `s = "Machine Learning"`, right-justify the string to a width of 25 characters, using `#` as the padding character.
28. Given the string `s = "Hello\tWorld"`, expand the tab `(\t)` to the default of 8 spaces.
29. Given the string `s = "Welcome"`, center the string to a width of 15 characters using spaces as padding.
30. Given the string `s = "42"`, use zfill() to pad the string to a width of 5, filling with zeros.
31. Given the string `s = "Hello\tPython"`, expand the tabs in the string to 4 spaces instead of the default 8.
32. Given the string `s = " Python Programming "`, remove both leading and trailing whitespace using the strip() method and print the result.
33. Given the string `s = " ***Data Science*** "`, remove the leading and trailing _ characters using strip("_") and print the result.
34. Given the string `s = "apple,banana,cherry"`, split the string into a list of words by commas using `split(",")`.
35. Given the string `s = "John Doe 25 New York"`, split the string into a list of words using the default space delimiter.
36. Given the string `s = "user@domain.com"`, split the string into three parts using the @ separator, and print the resulting tuple.
37. Given the list `words = ["Python", "is", "fun"]`, use the join() method to join the words into a sentence, separated by spaces.
38. Given the string `s = "PreprocessingData"`, remove the prefix `"Pre"` using the removeprefix() method.
39. Given the string `s = "filename.txt"`, remove the suffix `".txt"` using the removesuffix() method.
40. Given the string `s = "one two three four"`, split the string from the right at the first space using `rsplit()`.
41. Given the string `s = "Hello\nWorld\nPython"`, split the string by newlines using `splitlines()` and print the result.
42. Given the string `s = "Python3"`, check if the string is alphanumeric (contains only letters and numbers) using the `isalnum()` method.
43. Given the string `s = "HelloWorld"`, check if the string contains only alphabetic characters (no spaces, numbers, or special characters) using the `isalpha()` method.
44. Given the string `s = "12345"`, check if the string contains only digits using the `isdigit()` method.
45. Given the string `s = " "`, check if the string contains only whitespace characters using the `isspace()` method.
46. Given the string `s = "valid_identifier"`, check if the string is a valid Python identifier using the `isidentifier()` method.
47. Given the string `s = "hello world, hello Python"`, count how many times the substring `"hello"` appears in the string using the `count()` method.
48. Given the string `s = "I love programming in Python"`, find the index of the first occurrence of the substring `"programming"` using the `find()` method.
49. Given the string `s = "Welcome to the world of Python"`, find the index of the first occurrence of the substring `"Python"` using the `index()` method. (Raise an exception if not found.)
50. Given the string `s = "I love cats, cats are great"`, replace the substring `"cats"` with `"dogs"`, but limit the replacements to 1 occurrence using the `replace()` method.
51. Given the string `s = "look here, look there, look everywhere"`, find the index of the last occurrence of the substring `"look"` using the `rfind()` method.
52. Given the string `s = "apple banana apple grape"`, find the index of the last occurrence of the substring `"apple"` using the `rindex()` method.
53. Given the string `s = "Hello, World!"`, check if the string starts with the substring `"Hello"` using the `startswith()` method.
54. Given the string `s = "file_report.pdf"`, check if the string ends with the substring `".pdf"` using the `endswith()` method.
55. Given the string `s = "find me in the middle of the text"`, find the index of the substring `"middle"` between index 5 and 25 using the `find()` method.
56. Given the string `s = "red red red red"`, replace only the first two occurrences of the substring `"red"` with `"blue"` using the `replace()` method and a `max` value.
57. Given the variables `name = 'Alice'` and `age = 30`, create a sentence using the `.format()` method with positional arguments.
58. Given the variables `name = 'Bob'` and `age = 25`, create a sentence using the `.format()` method with named arguments.
59. Given the variable `animal = 'dog'`, create a sentence using `.format()` where the variable `animal` is repeated twice.
60. Given the variables `first_name = 'John'` and `age = 40`, create a sentence using `.format()` with indexing (e.g., `{1}` for `age` and `{0}` for `first_name`).
61. Given the string `text = 'Python'`, format it with a width of 20 characters and center it using `.format()`.
62. Given the dictionary `info = {'name': 'Eve', 'age': 22}`, use `.format()` with unpacking (`**info`) to create the sentence: `"Hello Eve, you are 22 years old!"`.
63. Given the variables `name = 'Mike'` and `age = 25`, use an f-string to create the sentence: `"Hello Mike. You are 25 years old."`.
64. Given the variable `price = 100`, use an f-string to create a sentence: `"The price after tax is 110."` (assuming tax rate is 10%).
65. Given the variable `name = 'Alice'`, use an f-string to print the lowercased version of the name: `"alice"`.
66. Given the variable `age = 30`, use an f-string to display the expression `age + 5`, and print `"Your age in 5 years will be 35."`.
67. Try to create an f-string with an invalid expression, such as `f'My name is {name\n}'` and handle the resulting `SyntaxError`.
68. Given the variable `username = 'jdoe'`, create an f-string that outputs `"Your username='jdoe'"` using the new f-string feature in Python 3.8+ (`username=`).
69. Given the variable `temperature = 20`, use an f-string to print both the variable name and its value in the format: `"temperature=20"`.
