import pandas as pd


def count(input):
    x = dict((i, input.count(i)) for i in set(input))
    return dict(sorted(x.items()))


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    df = pd.DataFrame(input)
    result = df.groupby('key', as_index=False).sum().set_index('key')['value'].to_dict()
    return result


input2 = [
    {'key': 'a', 'value': 3},
    {'key': 'b', 'value': 1},
    {'key': 'c', 'value': 2},
    {'key': 'a', 'value': 3},
    {'key': 'c', 'value': 5}
]
print(group_by_key(input2))  # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
