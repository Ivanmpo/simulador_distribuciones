from math import log
from mcm import Mcm
import numpy as np 
import math


def distribucionExponencial( l , numero):
  return -log(numero) / l


def erlang(k,lam, conjunto):  
  return (-1/k*lam)*np.log(np.array(conjunto).prod() ) 


def geometrica( p , numero):
  return int((np.log(numero) / np.log(1 - p)) + 1)

def unifDiscreta(limit, numero):
  return int(limit*numero)+1

def unifContinua(a, b, numero):
  # a, b limites inferior y superior. a<=x<=b es el intervalo 
  return (a + (b - a) * numero) #a + (b - a)u.


def weibull(alfa, beta, numero):
  return alfa*(-np.log(numero))**(1/beta)
  """mcm = Mcm()
  r = []
  for i in range(total_zs):
    s=0 #suma
    ran = mcm.generarConjunto(total_zs)
    for ra in ran:
      w= beta*(-np.log(1.0-ra))**(1.0/alfa)
      if(w>0.5):
        s= s + w
    r.append(float(s)/k)
  return(r)"""  
  
def bernoulli(p,numero):
  if(p <= 0 or p >= 1):
    print("Error, p debe estar entre 0 y 1")
    p = 0.5
  num = unifContinua(0,1,numero)
  if( 0 < num and num < 1-p):
    return 0
  elif(1-p <num and num <1):
    return 1
  else:
    return 0


def poisson(lam, numero):
  i = 0
  p = math.exp(-lam)
  f=p
  while(numero >= f):
    p = (lam * p)/(i + 1)
    f= f + p
    i += 1
  return i

def pareto(a, lam,numero): #hl lambda
  num = distribucionExponencial(lam,numero)
  return (math.exp(num/a) - 1)


def binomial( p, k , numero):
  #k es igual a n , wikipedia
  i = 0
  c = p/(1-p)
  pr = (1 - p) ** k
  f = pr
  while(numero >= f):
      pr = (c * (k - i) / (i + 1)) * pr
      f = f + pr
      i += 1
  return i




#teorema limite central FALTA
def normal(media, desn, conjunto):
  return media + desn *(sum(conjunto)- 6)


  # c y a no pueden ser iguales
def triangular(a,b,c, numero):
  d = (b-a)/(c-a) 
  if (numero < d and 0<numero):
    return ( a + ((b-a)*(numero))**0.5 )
  elif (numero<=1 and numero>=d):
    return ( (b+ ( ((c-a)*numero-(b-a))*(c-b)    )**0.5)  )











###################################################



def tstudent(k,media,desn,df,total_zs):
  r = normal(media,desn,total_zs)
  ch = chicuadrado(k,df,media,desn,total_zs)
  t = []
  for ra,chi in zip(r,ch):
    t.append(ra*((df/chi)**(0.5)))
  return(t)



def chicuadrado(k,df,media,desn,total_zs):
  x = []
  for na in range(total_zs):
    t = 0
    for ka in range(k):
      r= normal(media, desn, total_zs)
      for ra in r:
        t +=(ra**2.0)
    x.append((float(t)/(k)))
  return (x)