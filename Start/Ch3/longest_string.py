aantal = int(input())
the_strings = []
for i in range(aantal):
  the_strings.append(input())
print( the_strings)

def find_largest(the_strings):
    largest = 0  
    for w in the_strings[:]:
        length = len(w)
        if len(w) > largest:
          largest = len(w) 
            
    return largest

print(find_largest(the_strings))



