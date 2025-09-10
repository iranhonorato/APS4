import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from collections import defaultdict

df = pd.read_csv("../Dataset/MapHeuristics.csv", header=None, names=["Start", "Meta", "Custo"])

heuristica = defaultdict(list)

for _, row in df.iterrows():
    origem = row["Start"]
    destino = row["Meta"]
    peso = row["Custo"]
    heuristica[origem].append((peso, destino))

heuristica = dict(heuristica)

for k, v in heuristica.items():
    print(f"'{k}':{v},")


mapa = {
    'a':[(3,'b'),(6,'c')],
    'b':[(3,'a'),(3,'h'),(3,'k')],
    'c':[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
    'd':[(3,'c'),(1,'f'),(1,'e')],
    'e':[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
    'f':[(1,'g'),(1,'e'),(1,'d')],
    'g':[(2,'c'),(1,'f'),(2,'h')],
    'h':[(2,'i'),(2,'g'),(3,'b'),(4,'k')],
    'i':[(2,'e'),(2,'h')],
    'l':[(1,'k')],
    'k':[(1,'l'),(3,'n'),(4,'h'),(3,'b')],
    'm':[(2,'n'),(1,'x'),(14,'e')],
    'n':[(2,'m'),(3,'k')],
    'o':[(2,'c')],
    'p':[(2,'c')],
    'x':[(1,'m')]
    }