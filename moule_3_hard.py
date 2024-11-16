def calculate_structure_sum(args):

    summa = 0

    if isinstance(args,(int,float)):
        summa += args
    elif isinstance(args,str):
        summa = len(args)
    elif isinstance(args,dict):
        for key, value in args.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    else:
        for i in args:
            summa += calculate_structure_sum(i)
    return summa

data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)