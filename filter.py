import csv
from collections import defaultdict
from pprint import pprint
import timeit
import json


def method1():
    rows = list(csv.reader(open('Table_crosstab.csv', 'r'), delimiter=','))
    cols = zip(*rows)
    unik = set(cols[0])

    indexed = defaultdict(list)

    for x in unik:
        i = cols[0].index(x)
        indexed[i] = rows[i]

    return indexed

def method2():
    rows = list(csv.reader(open('Table_crosstab-2.csv', 'r'), delimiter=','))
    cols = zip(*rows)
    unik = set(cols[0])

    indexed = defaultdict(list)

    for x in unik:
        i = cols[0].index(x)
        indexed[i] = rows[i]

    return indexed

def method3():
    rows = list(csv.reader(open('Table_crosstab-3.csv', 'r'), delimiter=','))
    cols = zip(*rows)
    unik = set(cols[0])

    indexed = defaultdict(list)

    for x in unik:
        i = cols[0].index(x)
        indexed[i] = rows[i]

    return indexed

if __name__ == '__main__':

    results = method1()
    results2 = method2()
    results3 = method3()    
    print 'indexed:'
    """pprint(dict(results))"""
    """print(json.dumps(results, indent = 4))"""
    for keys,values in results.items():
        print(values)
    print '-' * 80
    for keys,values in results2.items():
        print(values)
    for keys,values in results3.items():
        print(values)