def print_params(a=1,b='Строка', c=True) :

    print(a,b,c)

print_params()
print_params(1,2)
print_params('Строка1')
print_params(2,5,[1,2,3])

values_dict = {'a':1,'b':'Строка','c':True}
values =[1,'Строка', True]

print_params(*values)

print_params(**values_dict)

values_list_2 = [54.32,'Строка']
print_params(*values_list_2,42)
