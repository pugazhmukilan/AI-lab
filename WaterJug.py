#water jug problem
from collections import defaultdict

jug1 =4
jug2 = 3
aim = 2

#initilizing  the matrix to default False

visited  = defaultdict(lambda : False)

def Solve_Jug( a1,a2):
    
   
    
    if (a1==aim and a2==0)or(a2==aim and a1==0):
        
        print(a1,a2)
        return True
        
    if (visited[(a1,a2)]==False) :
        print(a1,a2)
        visited[(a1,a2)] =True
            
        return( Solve_Jug(0,a2)or Solve_Jug(a1,0) or Solve_Jug(jug1,a2) or Solve_Jug(a1,jug2) or Solve_Jug(jug1,a2-(4-a1)if a2-(4-a1)>=0 else 0) or Solve_Jug(a1-(3-a2) if a1-(3-a2)>=0 else 0,3)or Solve_Jug(a1+a2,0) or Solve_Jug(0,a1+a2))
    else:
        return False
print("Solution: =================================")
Solve_Jug(0,0)     