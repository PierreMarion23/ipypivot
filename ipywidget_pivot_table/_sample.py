
import os
import pandas as pd


class Samples:
    """
    """

    def __init__(self):
        """
        """
        _dir = os.path.dirname(os.path.realpath(__file__))

        path = os.path.join(_dir, 'data', 'tips.csv')
        self.df_tips = pd.read_csv(path)

        path = os.path.join(_dir, 'data', 'mps.csv')
        self.df_mps = pd.read_csv(path)

        path = os.path.join(_dir, 'data', 'weather.csv')
        self.df_weather = pd.read_csv(path)

        path = os.path.join(_dir, 'data', 'iris.csv')
        self.df_iris = pd.read_csv(path)


samples = Samples()
