# Python code​​​​​‌​​​​​‌‌​‌‌‌‌​‌‌​​‌​‌​​​​​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_numbers(which, numbers):
    # Your code goes here
    counter = 0
    if which == "even":
      for i in range(len(numbers)):
          result = numbers[i] % 2
          if result == 0:
            counter += 1
      return counter
    
    elif which == "odd":
      for i in range(len(numbers)):
          result = numbers[i] % 2 
          if result != 0:
            counter += 1
      return counter
    
    else: 
      return -1

