my_dict = {'Irina': 1971, 'Violetta': 2001, 'Vladimir': 1993}
print (my_dict)
print (my_dict['Irina'])
my_dict ['Alexandr'] = 1969
print (my_dict['Alexandr'])
my_dict.update({'Artem': 2000,
                'Ivan': 2002})
del my_dict ['Violetta']
print (my_dict.get('Violetta'))
print(my_dict)

my_set = {1, 2, 3, 'Violetta', 1, 2, 3}
print (my_set)
my_set.add(4)
my_set.add('Sasha')
my_set.discard(2)
print(my_set)

