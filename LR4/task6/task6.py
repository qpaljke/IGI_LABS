import pandas as pd


class TitanicDataset:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def df_info(self):
        return self.df.info()

    def mean_survived_age(self):
        return self.df[self.df['Survived'] == 1]['Age'].mean()

    def mean_dead_age(self):
        return self.df[self.df['Survived'] == 0]['Age'].mean()


def run_task():
    df = TitanicDataset('task6/titanic.csv')
    print(df.df_info())
    print("Mean survived age:", df.mean_survived_age())
    print("Mead dead age:", df.mean_dead_age())
    ratio = df.mean_survived_age() / df.mean_dead_age()
    print("Mean survived age bigger than mean dead age in", ratio, "times")