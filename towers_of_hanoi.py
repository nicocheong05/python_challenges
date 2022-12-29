# A256: towers of hanoi code using recursion
# had help from geeksforgeeks

NumOfDiscs = int(input("Enter the number of discs: "))

def TowersOfHanoi(n, StartTower, FinalTower, MidTower): 
  if n == 0:
    return
  else:
    TowersOfHanoi(n-1, StartTower, MidTower, FinalTower)
    print("Move disc",n,"from Tower",StartTower,"to Tower",FinalTower)
    TowersOfHanoi(n-1, MidTower, FinalTower, StartTower)


TowersOfHanoi(NumOfDiscs, "A","C","B")
