# numpy-reorder-insert-fields
Using this class we can change our field order of numpy structured array 


data = np.array([('Alice', 25, 160, 50, 1, 2), ('Bob', 30, 170, 60, 2, 1), 
                 ('Charlie', 28, 180, 70, 3, 4), ('Diana', 35, 190, 80, 4, 7)],
                dtype=[('name', 'U10'), ('age', 'i4'), ('height', 'i4'), ('weight', 'i4'), ('sign', 'i4'), ('band', 'i4')])

We dont need to manually change date types and field names just use this method : 

-->  reordered_structured_array = numpy_reorder_insert_field.reorder_fields( structured_array, field_to_change = 'index' , target_index = 0 )

#####################################
Using regex on this :

[
    ('name', 'U20'),
    ('age', 'i4'),
    ('weight', 'i4'),
    ('height', float),
    ('sign', 'i4'),
    ('band', 'i4'), 
    ('index', 'datetime64[h]')
]

To Make this :
[
    ('index', 'datetime64[h]'),
    ('name', 'U20'),
    ('age', 'i4'),
    ('weight', 'i4'),
    ('height', float),
    ('sign', 'i4'),
    ('band', 'i4')
] 
