#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf


def Programma():
    while True:
        N=int(input('Numero di asset da confrontare: '))
        DF=CalcolaMatrice(N)
        plt.figure(figsize=(10,8), dpi=150)
        sns.heatmap(DF.corr(), cmap='RdYlGn', linecolor='black', linewidth=0.1, annot=True)
        plt.show()
        plt.clf()
        while True:
            risposta = str(input('Vuoi visualizzare una nuova matrice? (si/no): '))
            if risposta in ('si', 'no'):
                break
            print('Input non valido.')
        if risposta == 'si':
            continue
        else:
            print('Ciao')
            break


def CalcolaMatrice(N):
    DF=pd.DataFrame()
    p=str(input('inserire i numero di periodi da considerare + y/mo/d, es: 5mo '))
    for i in range(1, N+1) :
            t=str(input("Inserire il ticker del prodotto: "))
            Dataset= yf.Ticker(t)
            DF[t]=Dataset.history(period=p)['Close']
    return DF


Programma()
