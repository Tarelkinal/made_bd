import pandas as pd


def main():
    df = pd.read_csv('../data/AB_NYC_2019.csv')
	
    print(df[df.columns[:2]].head(20))
	
    mean = df['price'].mean()
    var = df['price'].var(ddof=0)

    print('mean: ', mean)
    print('variance: ', var)


if __name__ == '__main__':
    main()

