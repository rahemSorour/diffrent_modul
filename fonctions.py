# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:36:31 2021

@author: hp
"""
import random
import math 
import statistics 
import datetime
import webbrowser

#fonction calcul factoriel d'un nmbr

def fact(v):
    return(math.factorial(v))

#fonction afficher nmbr impair aléatoir
       
def rnd():
   if random.randint(1,10)%2!=0:
      print(random.randint(1, 10))
      
#fonction qui calcul le mod ety l'ecart
       
def stsc():
 print(statistics.mode([21,14,15,14,16,15,]))  
 print(statistics.stdev([21,3,6,19,17,99]))

#fonction qui affiche la date 

def dat():
    return f'the date of aujorduit is {datetime.date.today()}'
    
#fonction qui ouvert le site 

def site():
    return webbrowser.open('https://translate.google.com/')
  



  

  
    