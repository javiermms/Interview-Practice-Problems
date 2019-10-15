'''Given a column title as appears in an Excel sheet, return its corresponding column number.

Examples:
A -> 1
    
B -> 2
    
C -> 3
    
    ...
    
Z -> 26
    
AA -> 27
    
AB -> 28 '''

def excel_column_to_number(column):

  result = 0
  
  for index, char in enumerate(column[::-1]): 
    base = ord(char) - 64
   
    result += base * (26 ** index)
    
  return result
   
print(excel_column_to_number('ZZZ'))  
