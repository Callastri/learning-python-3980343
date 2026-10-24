string = input()


def is_palindrome(teststr):
    # Your code goes here.
      temp = teststr.lower()
      stringlist = []
      for c in temp:
        if c.isalpha():
          stringlist.append(c)
      string = "".join(stringlist)
      stringlist.reverse()
      reversedstring = "".join(stringlist)
          
      if string == reversedstring:
        return True
      return False

      
   
print (is_palindrome(string))