class Operation:
  def __init__(self, nbr1=12, nbr2=3):
    self.nbr1 = nbr1
    self.nbr2 = nbr2

  def addition(self):
    resultat = self.nbr1 + self.nbr2
    return resultat

ll = Operation()
print("le nombre 1 est : ",ll.nbr1)
print("le nombre 2 est : " ,ll.nbr2)
print("le resultat est donc: " ,ll.addition())
