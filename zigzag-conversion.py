class Solution:
   def convert(self, s: str, numRows: int) -> str:
    
    if numRows == 1: return s
    
    rows = ["" for i in range(numRows)] 
    ptr=0
    offset=1
    
    
    for i in s:
        rows[ptr]+=i
        
        if ptr==numRows-1: offset=-1
        elif ptr==0: offset=1
            
        ptr+=offset
    return "".join(rows)