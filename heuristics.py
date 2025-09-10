import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from collections import defaultdict
from aigyminsper.search.search_algorithms import AEstrela

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