# Class 4 - Homeworks

## Topic: Dictionaries, Sets

## Exercises - Dictionaries

1. Print the value of key ‘history’ from the below `dict`
    ```python
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    ```

2. Write a program to rename a key `city` to a `location` in the following dictionary.
    ```python
    sample_dict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
    }
    ```

3. Change value of a key in a nested dictionary. Write a Python program to change Brad’s salary to 8500 in the following dictionary.
    ```python
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }
    ```

4. Python program to convert a dictionary to list of (k,v) tuples.
    ```python
    d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
    ```
5. Get sum of all the values in a dict
    ```python
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75,
        'chemistry': 89,
        'GK': 50
        
    }
    ```
6. Write a Python script to sort (ascending and descending) a dictionary by value.
7. Merge two Python dictionaries into one
    ```python
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    ```
8. Create a dictionary with the keys `'name'`, `'age'`, and `'city'` and corresponding values `'Alice'`, `25`, and `'New York'`. Print the dictionary.  
9. Access and print the value of the 'age' key from the dictionary.
10. Use the .get() method to access the value of 'city' and print it.
11. Update the 'age' key in the dictionary to 26 and print the dictionary.
12. Add a new key 'job' with the value 'Engineer' to the dictionary.
13. Remove the 'city' key from the dictionary using the del keyword and print the dictionary.
14. Remove the 'job' key using .pop(). Print the value and the updated dictionary.
15. Remove and print the last inserted key-value pair from the dictionary using .popitem().
16. Print all the keys in the dictionary.
17. Print all the values in the dictionary.
18. Print all key-value pairs as tuples.
19. Check if 'name' exists in the dictionary. Print True or False.
20. Remove all items from the dictionary. Print the empty dictionary.


## Tuples
21. Given a Python list, Write a program to add all its elements into a given set.
    ```python
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]
    ```
22. Return a new set of identical items from two sets
    ```python
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    ```
23. Write a Python program to return a new set with unique items from both sets by removing duplicates.
    ```python
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    ```
24. Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
    ```python
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    ```
25. Write a Python program to remove items 10, 20, 30 from the following set at once.
    ```python
    set1 = {10, 20, 30, 40, 50}
    ```
26. Return a set of elements present in Set A or B, but not both
    ```python
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    ```
