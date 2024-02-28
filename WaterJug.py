#water jug problem
from collections import defaultdict

jug1 =4
jug2 = 3
final =2
#initilizing  the matrix to default False

visited  = defaultdict(lambda : False)

def Solve_Jug( a1,a2):
    
   
    
    if (a1==final and a2==0)or(a2==final and a1==0):
        
        print("We reached the GOAL STATE!!!  ",a1,a2)
        return True
        
    if (visited[(a1,a2)]==False) :
        print(a1,a2)
        visited[(a1,a2)] =True
        #in this return statement something will return true and that will be taken
        return( Solve_Jug(0,a2)or Solve_Jug(a1,0) or Solve_Jug(jug1,a2) or Solve_Jug(a1,jug2) or 
                Solve_Jug(jug1,a2-(4-a1)if a2-(4-a1)>=0 else 0) or Solve_Jug(a1-(3-a2) if a1-(3-a2)>=0 else 0,3)or 
                Solve_Jug(a1+a2 if (a1+a2<=jug1) else jug1,0) or Solve_Jug(0,a1+a2 if(a1+a2<=jug2) else jug2))
    else:
        return False
print("Solution: =================================")
Solve_Jug(0,0)     


print("change in github")
