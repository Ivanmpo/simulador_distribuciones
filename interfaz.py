from mcm import Mcm
import generador as Generador
import numpy as np 
import matplotlib.pyplot as plt
import pylab as pl
import tkinter as tk

def createExpo():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="Lambda").grid(row=1, column=1)
    tk.Label(newWindow, text="Total números").grid(row=2, column=1)

    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarExpo(e1.get(), e2.get()))
    buttonGraf.grid(row=4, column=2, padx = 10,pady = 10)

def graficarExpo(lam, total_zos):
  conjunto_exponencial = Generador.distribucionExponencial(float(lam),int(total_zos))
  shist,bin_edges = np.histogram(conjunto_exponencial, 20)
  plt.hist(conjunto_exponencial, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createErlang():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="Cantidad va Erlang").grid(row=0, column=1)
    tk.Label(newWindow, text="k (cantidad exponenciales)").grid(row=1, column=1)
    tk.Label(newWindow, text="Lambda").grid(row=2, column=0)

    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e3 = tk.Entry(newWindow)
    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    e3.grid(row=2, column=2)
    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarErlang(e1.get(), e2.get(), e3.get()))
    buttonGraf.grid(row=6, column=2, padx = 10,pady = 30)

def graficarErlang(R,k,lam):
  conjunto_erlang = Generador.erlang(int(R), int(k), float(lam))
  shist,bin_edges = np.histogram(conjunto_erlang, 20)
  plt.hist(conjunto_erlang, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
#############################################################################################################
def createGeometria():
    
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="p").grid(row=0, column=1)
    tk.Label(newWindow, text="Total de Zi").grid(row=1, column=1)


    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarGeometria(e1.get(), e2.get()))
    buttonGraf.grid(row=4, column=2, padx = 10,pady = 10)

def graficarGeometria(p , total_zs):
  conjunto_geometrica = Generador.geometrica(float(p), int(total_zs))
  shist,bin_edges = np.histogram(conjunto_geometrica, 20)
  plt.hist(conjunto_geometrica, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createTriangular():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="a").grid(row=0, column=1)
    tk.Label(newWindow, text="b").grid(row=1, column=1)
    tk.Label(newWindow, text="c").grid(row=2, column=1)
    tk.Label(newWindow, text="Total de Zi").grid(row=3)


    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e3 = tk.Entry(newWindow)
    e4 = tk.Entry(newWindow)
    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    e3.grid(row=2, column=2)
    e4.grid(row=3, column=2)
    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarTriangular(e1.get(), e2.get(), e3.get(), e4.get()  ))
    buttonGraf.grid(row=5, column=2, padx = 10,pady = 10)

def graficarTriangular(a,b,c, total_zs):
  conjunto_triangular = Generador.triangular(float(a),float(b),float(c),int(total_zs))
  shist,bin_edges = np.histogram(conjunto_triangular, 20)
  plt.hist(conjunto_triangular, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createNormal():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="Media").grid(row=0, column=1)
    tk.Label(newWindow, text="Desviación Std.").grid(row=1, column=1)
    tk.Label(newWindow, text="Total Zi").grid(row=2, column=1)



    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e3 = tk.Entry(newWindow)

    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    e3.grid(row=2, column=2)

    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarNormal(e1.get(), e2.get(), e3.get()  ))
    buttonGraf.grid(row=5, column=2, padx = 10,pady = 10)

def graficarNormal(media, desn, total_zs):
  
  conjunto_normal = Generador.normal(float(media),float(desn),int(total_zs))
  shist,bin_edges = np.histogram(conjunto_normal, 20)
  plt.hist(conjunto_normal, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createUnifDiscreta():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="Límite").grid(row=0, column=1)
    tk.Label(newWindow, text="Total Zi").grid(row=1, column=1)



    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)

    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)

    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarUnifDiscreta(e1.get(), e2.get() ))
    buttonGraf.grid(row=5, column=2, padx = 10,pady = 20)

def graficarUnifDiscreta(limit, total_zs):

  conjunto_unif_discreta = Generador.unifDiscreta(float(limit) , int(total_zs))
  shist,bin_edges = np.histogram(conjunto_unif_discreta, 20)
  plt.hist(conjunto_unif_discreta, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
#############################################################################################################
def createUnifContinua():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="a").grid(row=0, column=1)
    tk.Label(newWindow, text="b").grid(row=1, column=1)
    tk.Label(newWindow, text="Total Zi").grid(row=2, column=1)



    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e3 = tk.Entry(newWindow)

    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    e3.grid(row=2, column=2)

    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarUnifContinua(e1.get(), e2.get(), e3.get() ))
    buttonGraf.grid(row=5, column=1, padx = 10,pady = 20)

def graficarUnifContinua(a,b, total_zs):
  conjunto_unif_continua = Generador.unifContinua(float(a),float(b) , int(total_zs))
  
  shist,bin_edges = np.histogram(conjunto_unif_continua, 20)
  plt.hist(conjunto_unif_continua, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createBernoulli():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="p").grid(row=0, column=1)
    tk.Label(newWindow, text="Total Zi").grid(row=1, column=1)

    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)

    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)


    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarBernoulli(e1.get(), e2.get() ))
    buttonGraf.grid(row=5, column=2, padx = 10,pady = 10)

def graficarBernoulli(p, total_zs):
  conjunto_bernoulli = Generador.bernoulli(float(p) , int(total_zs))
  
  shist,bin_edges = np.histogram(conjunto_bernoulli, 20)
  plt.hist(conjunto_bernoulli, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createPoisson():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="p").grid(row=0, column=1)
    tk.Label(newWindow, text="Total Zi").grid(row=1, column=1)

    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)

    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)


    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarPoisson(e1.get(), e2.get() ))
    buttonGraf.grid(row=5, column=2, padx = 10,pady = 10)

def graficarPoisson(lam, total_zs):
  conjunto_poisson = Generador.poisson(float(lam) , int(total_zs))
  
  shist,bin_edges = np.histogram(conjunto_poisson, 20)
  plt.hist(conjunto_poisson, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createBinomial():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="p").grid(row=0, column=1)
    tk.Label(newWindow, text="k").grid(row=1, column=1)
    tk.Label(newWindow, text="Total Zi").grid(row=2, column=1)

    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e3 = tk.Entry(newWindow)

    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    e3.grid(row=2, column=2)


    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarBinomial(e1.get(), e2.get() , e3.get()))
    buttonGraf.grid(row=5, column=1, padx = 10,pady = 20)

def graficarBinomial(p, k,total_zs):
  conjunto_binomial = Generador.binomial(float(p), int(k) , int(total_zs))
  shist,bin_edges = np.histogram(conjunto_binomial, 20)
  plt.hist(conjunto_binomial, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createTstudent():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="k").grid(row=0, column=1)
    tk.Label(newWindow, text="media").grid(row=1, column=1)
    tk.Label(newWindow, text="Desviación Std-").grid(row=2, column=1)
    tk.Label(newWindow, text="Df").grid(row=3, column=1)

    tk.Label(newWindow, text="Total Zi").grid(row=4, column=1)

    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e3 = tk.Entry(newWindow)
    e4 = tk.Entry(newWindow)
    e5 = tk.Entry(newWindow)

    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    e3.grid(row=2, column=2)
    e4.grid(row=3, column=2)
    e5.grid(row=4, column=2)


    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarTstudent(e1.get(), e2.get() , e3.get() , e4.get() , e5.get() ))
    buttonGraf.grid(row=5, column=2, padx = 10,pady = 10)

def graficarTstudent(k,media,desn,df,total_zs):
  conjunto_tstudent = Generador.tstudent(int(k), float(media) , float(desn) , int(df)  , int(total_zs))
  shist,bin_edges = np.histogram(conjunto_tstudent, 20)
  plt.hist(conjunto_tstudent, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createChicuadrado():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="k").grid(row=0, column=1)
    tk.Label(newWindow, text="Df").grid(row=1, column=1)
    tk.Label(newWindow, text="Media").grid(row=2, column=1)
    tk.Label(newWindow, text="Desviación Std").grid(row=3, column=1)
    tk.Label(newWindow, text="Total Zi").grid(row=4, column=1)

    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e3 = tk.Entry(newWindow)
    e4 = tk.Entry(newWindow)
    e5 = tk.Entry(newWindow)

    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    e3.grid(row=2, column=2)
    e4.grid(row=3, column=2)
    e5.grid(row=4, column=2)


    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarChicuadrado(e1.get(), e2.get() , e3.get() , e4.get() , e5.get() ))
    buttonGraf.grid(row=6, column=2, padx = 10,pady = 30)

def graficarChicuadrado(k,df,media,desn,total_zs):
  conjunto_chi = Generador.chicuadrado(int(k), int(df) ,float(media) , float(desn)   , int(total_zs))
  shist,bin_edges = np.histogram(conjunto_chi, 20)
  plt.hist(conjunto_chi, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createPareto():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="a").grid(row=0, column=1)
    tk.Label(newWindow, text="Lambda").grid(row=1, column=1)

    tk.Label(newWindow, text="Total Zi").grid(row=2, column=1)

    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e3 = tk.Entry(newWindow)


    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    e3.grid(row=2, column=2)



    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarPareto(e1.get(), e2.get() , e3.get() ))
    buttonGraf.grid(row=5, column=2, padx = 10,pady = 10)

def graficarPareto(a, hl, total_zs):
  conjunto_toreto = Generador.pareto(int(a), float(hl) , int(total_zs))
  shist,bin_edges = np.histogram(conjunto_toreto, 20)
  plt.hist(conjunto_toreto, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################
def createWeibull():
    newWindow = tk.Toplevel(app)
    newWindow.geometry('300x200')
    tk.Label(newWindow, text="alfa").grid(row=0, column=1)
    tk.Label(newWindow, text="B").grid(row=1, column=1)
    tk.Label(newWindow, text="k").grid(row=2, column=1)
    tk.Label(newWindow, text="Total Zi").grid(row=3, column=1)

    e1 = tk.Entry(newWindow)
    e2 = tk.Entry(newWindow)
    e3 = tk.Entry(newWindow)
    e4 = tk.Entry(newWindow)


    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    e3.grid(row=2, column=2)
    e4.grid(row=3, column=2)



    buttonGraf = tk.Button(newWindow, text="Graficar",command=lambda:graficarWeibull(e1.get(), e2.get() , e3.get(), e4.get()  ))
    buttonGraf.grid(row=5, column=2, padx = 10,pady = 10)

def graficarWeibull(alfa, beta, k, total_zs):
  conjunto_w = Generador.weibull(int(alfa), float(beta) , float(k),  int(total_zs))
  shist,bin_edges = np.histogram(conjunto_w, 20)
  plt.hist(conjunto_w, bins=bin_edges, density=True)
  plt.show()
#############################################################################################################




app = tk.Tk()

buttonExample = tk.Button(app, text="Exponencial",command=createExpo)
buttonExample.pack()

buttonErlang = tk.Button(app, text="Erlang",command=createErlang)
buttonErlang.pack()

buttonGeometrica = tk.Button(app, text="Geometrica",command=createGeometria)
buttonGeometrica.pack()

buttonTriangular = tk.Button(app, text="Triangular",command=createTriangular)
buttonTriangular.pack()

buttonNormal = tk.Button(app, text="Normal",command=createNormal)
buttonNormal.pack()

buttonUniformeDiscreta = tk.Button(app, text="Uniforme Discreta",command=createUnifDiscreta)
buttonUniformeDiscreta.pack()

buttonUniformeContinua = tk.Button(app, text="Uniforme Continua",command=createUnifContinua)
buttonUniformeContinua.pack()

buttonBernoulli = tk.Button(app, text="Bernoulli",command=createBernoulli)
buttonBernoulli.pack()

buttonPoisson = tk.Button(app, text="Poisson",command=createPoisson)
buttonPoisson.pack()

buttonBinomial = tk.Button(app, text="Binomial",command=createBinomial)
buttonBinomial.pack()

buttonTstudent = tk.Button(app, text="Tstudent",command=createTstudent)
buttonTstudent.pack()

buttonChicuadrado = tk.Button(app, text="Chicuadrado",command=createChicuadrado)
buttonChicuadrado.pack()

buttonPareto = tk.Button(app, text="Pareto",command=createPareto)
buttonPareto.pack()

buttonWeibull = tk.Button(app, text="Weibull",command=createWeibull)
buttonWeibull.pack()

app.title("Principal - Distribuciones ")
app.geometry('400x400')
app.mainloop()