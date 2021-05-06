import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('pibs.csv') # usar o indice de paises
df.set_index('País', inplace=True)

