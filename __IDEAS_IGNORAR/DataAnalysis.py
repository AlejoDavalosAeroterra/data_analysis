import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from DataContainer import DataContainer

class DataAnalysis():
    def __init__(self):
        pass

    def AddRowDF(self, df:pd.DataFrame, new_row:pd.Series, ignore_index:bool=True) -> pd.DataFrame:
        """ Agrega una fila nueva nueva al dataframe, y lo devuelve modificado.
        La fila debe ser un diccionario cuyas keys son los nombres de las columnas.

        Parameters
        ----------
        df: pd.DataFrame
            DataFrame indexado. Si las filas se indexan con una key,
            elimina todas las keys y pone indice numérico en su lugar.
        
        new_row: pd.Series
            Nueva fila, debe ser creada a partir de un diccionario,
            cuyas keys son los nombres de las columnas.

        ignore_index: bool
            True: Agrega la fila con el indice correlativo, abajo de todo.
            False: Agrega la fila con indice 0 (checkear, podría diferir, usar en True).

        Ejemplo: 
        >>> df = pd.DataFrame([[1,2],[3,4],[5,6]],columns=["col_1", "col_2"])
        >>> new_row = pd.Series({
        ...     "col_1": 7,
        ...     "col_2": 8
        ... })
        >>> df = AddRowDF(df, new_row)
        >>> df
        col_1  col_2
        0      1      2
        1      3      4
        2      5      6
        3      7      8
        """
        return pd.concat([df, new_row.to_frame().T], ignore_index=ignore_index)






'''
d = pd.DataFrame({
    "x": [6,3,7,2,1],
    "y": [1,4,2,7,3]
}, index=["a", "b", "c", "d", "e"])

d.plot.barh()
plt.legend(loc="lower right")
plt.savefig("asd.png")
plt.close("all")
'''

a = pd.DataFrame([1,2,3,4])
plt.plot(a)
plt.show()
