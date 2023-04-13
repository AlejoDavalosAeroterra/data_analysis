import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class DataContainer():
    def __init__(self):
        self.data = pd.DataFrame
        # Va a tener un atributo index, con letras, si son datos relacionados.
        # Si no lo tiene, van a ser datos estilo excel.
        # Me interesa una clave que sea "Label"