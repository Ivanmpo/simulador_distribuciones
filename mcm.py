from random import randint
class Mcm:

  def __init__(self, z):
    #self.z0 = 5434549
    #self.z0 = randint(1000000, 10000000)
    self.a = 16807
    self.m = 2147483647
    self.z = z

  def generarConjunto(self, total_numeros):
    conjunto = [randint(0, 1000000)]
    for i in range(1,total_numeros):
      z=(self.a * conjunto[i-1]) % self.m

      conjunto.append(z)
    return self.normalizarConjunto(conjunto)

  


  def normalizarConjunto(self, conjunto):
    conjunto_normalizado = []
    for i in range(0,len(conjunto)):
      conjunto_normalizado.append(conjunto[i]/self.m)
    return conjunto_normalizado

  def generarNumero(self):
    ze=(self.a * self.z) % self.m
    return ze

  def normalizarNumero(self, numero):
    return numero/self.m