import numpy as np
import pandas as pd
import random
import math

#Pandas
'''
1. Позволяет создавать одномерные массивы с помощью pd.Series из любого типа данных - числа, строки, словари и тд). 
Каждому объекту по умолчанию присваивается индексы [0, ..., len(data) - 1], но можно указывать их вручную
2. Позволяет создавать двумерые массивы через pd.DataFrame, в тч из словарей
3. DataFrame.head()/DataFrame.tail() позволяют просматривать верхние/нижние ряды массива соответственно
'''

s = pd.Series([1, [12, 13, 14], 'abc', {1, 2, 2, 5, 6, 6, 7}, {'a': 1, 'b': 2, 'c': 3}],
              index=['a', 'b', 'c', 'd', 'e'])
print(s)
m = pd.DataFrame(
    {
        'A': [math.sqrt(i) for i in [10, 20, 30, 40, 50]],
        'B': range(5),
        'C': [random.randint(0, 15) for i in range(5)],
        'D': [f'test_string {i}' for i in range(10, 15)]
    }
)
print(m)
print(m.head()) #из-за не большого размера массива печатает его целиком
print(m.tail()) #из-за не большого размера массива печатает его целиком
