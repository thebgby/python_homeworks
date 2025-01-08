# Class 7 - Homeworks

## Topic: Functions

## Exercises 

1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
6. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
7. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
    ```python
    print(reverse_list([1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]
    print(reverse_list1(["A", "B", "C"]))
    # ["C", "B", "A"]
    ```
8. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
9. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
    ```python
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
    numbers = [2, 3, 7, 9]
    print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
    ```
10. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
    ```python
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    numbers = [2, 3, 7, 9]
    print(remove_item(numbers, 3))  # [2, 7, 9]
    ```
11. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    ```python
        print(evens_and_odds(100))
        # The number of odds are 50.
        # The number of evens are 51.
    ```
12. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
13. Write a function called is_prime, which checks if a number is prime.
14. Write a functions which checks if all items are unique in the list.
15. Write a function which checks if all the items of the list are of the same data type.
16. Go to the data folder and access the countries-data.py file.

    * Create a function called the most_spoken_languages in the world. It should return 20 most spoken languages in the world in descending order
    * Create a function called the most_populated_countries. It should return 10 most populated countries in descending order.

```python
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

17. Use map to create a new list by changing each country to uppercase in the countries list
18. Use map to create a new list by changing each number to its square in the numbers list
19. Use map to change each name to uppercase in the names list
20. Use filter to filter out countries containing 'land'.
21. Use filter to filter out countries having exactly six characters.
22. Use filter to filter out countries containing six letters and more in the country list.
23. Use filter to filter out countries starting with an 'E'
24. Use the countries_data.py file and follow the tasks below: 
    * Sort countries by name, by capital, by population
    * Sort out the ten most spoken languages by location.
    * Sort out the ten most populated countries.
