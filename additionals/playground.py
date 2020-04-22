import pandas as pd
import numpy as np

def run():
    data = {
        'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
        'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
                 'Manchester', 'Cairo', 'Osaka'],
        'age': [41, 28, 33, 34, 38, 31, 37],
        'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
    }

    row_labels = [101, 102, 103, 104, 105, 106, 107]

    df = pd.DataFrame(data=data, index=row_labels)

    print(df)

    print(df['city'][102])

    print(df.at[103, 'name'])

    df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])
    print(df)

    df['total-score'] = 0.0
    df.insert(loc=4, column='django-score', value = np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))
    print(df)

    print((df['py-score'] + df['js-score']) / 2)

    df = df.drop('total-score', axis=1)
    df.rename(columns={'py-score': 'python mark',
                       'js-score': 'javascript mark',
                       'django-score': 'django mark'},
              inplace=True)
    print(df)

    print(max(df['python mark']))


if __name__ == '__main__':
    run()