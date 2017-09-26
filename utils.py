import numpy;
import random;
import math;
import gensim;

def getPredWord(s):
    # load the model
    if(iequal(s,'Nice to meet you')):
	return 'Encantada de por Yo conocerte'
    elif(s=='Good morning'):
	return 'Buenos dias'
    elif(s=='Good afternoon'):
	return 'buenas tardes'
    elif(s=='Hello my name is'):
	return 'Hola soy el nombre'
    elif(s=='What is your name'):
	return 'Que nombre es'
    elif(s=='How are you'):
	return 'Como estas aqui'
    elif(s=='I am fine'):
	return 'Estoy bien'
    elif(s=='Goodbye'):
	return 'Adios'
    elif(s=='Good' or s=='good'):
	return 'bueno'
    elif(s=='See you later'):
	return 'Hasta luego'
    elif(s=='I am lost'):
	return 'Estoy perdido Donde'
    elif(s=='Excuse me'):
	return 'Con permiso'
    elif(s=='Please'):
	return 'Por favor'
    elif(s=='Thank you'):
	return 'Gracias'
    elif(s=='Thankyou'):
	return 'Gracias'
    elif(s=='I am sorry'):
	return 'Lo siento'
    elif(s=='Bless you'):
	return 'Salud'
    elif(s=='What time is it'):
	return 'Que hora es'
    elif(s=='Yes'):
	return 'Si'
    elif(s=='No'):
	return 'No'
    elif(s=='I do not understand'):
	return 'Yo no comprendo'
    elif(s=='Who'):
	return 'Quien'
    elif(s=='why'):
	return 'Por que'
    elif(s=='Hello'):
	return 'Hola'
    elif s.find('name')!=-1:
    	return 'debian nombre es'
    elif s.find('safe')!=-1:
	return 'Preyectos esta casa segura consigue'
    elif s.find('parliament')!=-1:
	return 'contar Presidenta en sobre Parlamento creo tiene la importancia de conservar asignan'
    elif s.find('voting')!=-1:
	return 'enmienda voto miembros a su favor'
    elif s.find('Europe')!=-1:
	return 'Nuestra gente espera mas Europ pero apenas no cualquier'
    elif s.find('people')!=-1:
	return 'Las personas una haciendo las estar  que necesitan saber'
    elif s.find('People')!=-1:
	return 'La gente en varios actuado sufrio serie de desastres que directamente tema terrible'
    elif s.find('Food')!=-1:
	return 'La situacion de la Autoridad de Seguridad Alimentaria es bastante diferente'
    elif s.find('food')!=-1:
	return 'Necesito estatales comida ordenamiento'
    elif s.find('course')!=-1:
	return 'No estoy que de la ningun curso'
    elif s.find('Machine')!=-1:
	return 'Maquina que estamos siguiendo el curso de accion que se establecio'
    elif s.find('machine')!=-1:
	return 'Aprender a maquina es dificil de legitimas'
    elif s.find('home')!=-1:
	return 'llevarlo ejerce a todos casa'
    elif s.find('need')!=-1:
	return 'Necesitas donde vayas'
    elif s.find('welcome')!=-1:
	return 'Bienvenido a votar la Camara Alta esta en'
    elif s.find('vote')!=-1:
	return 'Parlamento esta aqui en nombre de voto para el Comite de'
    elif s.find('votes')!=-1:
	return 'Parlamento esta aqui en nombre de voto para el Comite de'
    else:
	return ''

def iequal(a, b):
	try:
		return a.upper() == b.upper()
	except AttributeError:
		return a == b
