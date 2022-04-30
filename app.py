from flask import Flask , request
from flask import render_template

from mcm import Mcm
import generador as Generador
import scipy.stats
import numpy as np 
import math

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('tarea2/serie.html')


@app.route('/simulacion/serie', methods=['POST'])
def simulacion_serie():
  json = request.get_json(force=True)
  #print(json)
  configuracion = json['config']
  servidores = json['servidores']
  print(configuracion)
  print("---------------------------------------------")
  for servidor in servidores:
    print(servidor['tamano_fila'])

  return "ho"


@app.route('/ajax/intervalo_confianza', methods=['POST'])
def intervalo_confianza():
  json = request.get_json(force=True)
  numeros_medios = json['lista_numeros_medios']
  print(numeros_medios)
  confianza = int(json['nivel_confianza'])/100
  print(confianza)
  a = 1.0 * np.array(numeros_medios)

  m , se = np.mean(a) , scipy.stats.sem(a)
  print(m)
  print(se)
  if math.isnan(se):
    se = 0
  h = se * ( -1 * scipy.stats.norm.ppf((1-confianza))/2   )
  print(h)
  if math.isnan(h):
    h=0
  return {"limite_inf" : str(round(m-h,5)) , "limite_sup": str(round(m+h, 5) ) }


@app.route('/ajax/exponencial', methods=['POST'])
def exponencial():
  json = request.get_json(force=True)

  z=json['zeta']
  lam = float(json['parametros']['lambda'])

  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)
  
  numfinal = Generador.distribucionExponencial( lam , num_normalizado)
  return {"z_1": z_1 , "valor":numfinal}

@app.route('/ajax/erlang', methods=['POST'])
def erlang():
  json = request.get_json(force=True)

  z=json['zeta']
  k = int(json['parametros']['K'])
  lam = float(json['parametros']['lambda'])
  mcm = Mcm(z)
  variables_aleatorias = []
  for i in range(k):
    z_1 = mcm.generarNumero()
    num_normalizado = mcm.normalizarNumero(z_1)
    variables_aleatorias.append(num_normalizado)

  numfinal = Generador.erlang( lam , k, variables_aleatorias)

  return {"z_1": z_1 , "valor":numfinal}

@app.route('/ajax/geometrica', methods=['POST'])
def geometrica():
  json = request.get_json(force=True)

  z=json['zeta']
  P = float(json['parametros']['P'])
  
  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)

  numfinal = Generador.geometrica( P , num_normalizado)

  return {"z_1": z_1 , "valor":numfinal}

@app.route('/ajax/uniformediscreta', methods=['POST'])
def uniformediscreta():
  json = request.get_json(force=True)

  z=json['zeta']
  limite = float(json['parametros']['limite'])
  
  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)

  numfinal = Generador.unifDiscreta( limite , num_normalizado)

  return {"z_1": z_1 , "valor":numfinal}

@app.route('/ajax/uniformecontinua', methods=['POST'])
def uniformecontinua():
  json = request.get_json(force=True)

  z=json['zeta']
  a = float(json['parametros']['a'])
  b = float(json['parametros']['b'])
  
  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)

  numfinal = Generador.unifContinua( a,b , num_normalizado)

  return {"z_1": z_1 , "valor":numfinal}

@app.route('/ajax/weibull', methods=['POST'])
def weibull():
  json = request.get_json(force=True)

  z=json['zeta']
  alpha = float(json['parametros']['alpha'])
  beta = float(json['parametros']['beta'])
  
  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)

  numfinal = Generador.weibull( alpha,beta , num_normalizado)

  return {"z_1": z_1 , "valor":numfinal}

@app.route('/ajax/bernoulli', methods=['POST'])
def bernoulli():
  json = request.get_json(force=True)

  z=json['zeta']
  p = float(json['parametros']['p'])

  
  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)

  numfinal = Generador.bernoulli( p, num_normalizado)

  return {"z_1": z_1 , "valor":numfinal}


@app.route('/ajax/poisson', methods=['POST'])
def poisson():
  json = request.get_json(force=True)

  z=json['zeta']
  lam = float(json['parametros']['lambda'])

  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)

  numfinal = Generador.poisson( lam, num_normalizado)

  return {"z_1": z_1 , "valor":numfinal}

@app.route('/ajax/pareto', methods=['POST'])
def pareto():
  json = request.get_json(force=True)

  z=json['zeta']
  a = float(json['parametros']['a'])
  lam = float(json['parametros']['lambda'])

  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)

  numfinal = Generador.pareto( a , lam, num_normalizado)

  return {"z_1": z_1 , "valor":numfinal}


@app.route('/ajax/binomial', methods=['POST'])
def binomial():
  json = request.get_json(force=True)

  z=json['zeta']
  p = float(json['parametros']['p'])
  k = float(json['parametros']['k'])

  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)

  numfinal = Generador.binomial( p , k , num_normalizado)

  return {"z_1": z_1 , "valor":numfinal}

@app.route('/ajax/normal', methods=['POST'])
def normal():
  json = request.get_json(force=True)

  z=json['zeta']
  media = float(json['parametros']['media'])
  de = float(json['parametros']['de'])
  conjunto = []
  mcm = Mcm(z)
  for i in range(12):
    
    z_1 = mcm.generarNumero()
    num_normalizado = mcm.normalizarNumero(z_1)
    conjunto.append(num_normalizado)

  numfinal = Generador.normal( media,de , conjunto)

  return {"z_1": z_1 , "valor":numfinal}

@app.route('/ajax/triangular', methods=['POST'])
def triangular():
  json = request.get_json(force=True)

  z=json['zeta']
  a = float(json['parametros']['a'])
  b = float(json['parametros']['b'])
  c = float(json['parametros']['c'])

  mcm = Mcm(z)
  z_1 = mcm.generarNumero()
  num_normalizado = mcm.normalizarNumero(z_1)

  numfinal = Generador.triangular( a,b,c, num_normalizado)

  return {"z_1": z_1 , "valor":numfinal}



if __name__ == '__main__':
  app.run(debug = True , port=8000) 