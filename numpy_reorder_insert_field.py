class numpy_reorder_insert_field:
  @classmethod
  def reorder_fields(cls, structured_array, field_to_change, target_index):

      dt = np.dtype(structured_array.dtype.descr )

      # Convert dtype to string
      dt_str = str(dt)
      field_pattern = re.compile(r"'(\w+)'")  # Matches field names
      type_pattern = re.compile(r"'<([a-zA-Z0-9[\]_]+)'")  # Matches data types

      # Find all matches in the string
      field_names = field_pattern.findall(dt_str)
      field_types = type_pattern.findall(dt_str)
    
      field_names, field_types  =  cls.move_element_to_index(field_names, field_types, field_to_change, target_index)
      if type(field_to_change) == list :
          for i, field in enumerate(field_to_change):              
               field_names, field_types  =  cls.move_element_to_index(field_names, field_types, field_to_change= field, target_index= target_index[i])
      field_tuples = list(zip(field_names, field_types))

      # Convert the list of tuples to a NumPy dtype string
      dtype_string = "["
      dtype_string += ', '.join([f"('{name}', '{dtype}')" for name, dtype in field_tuples])
      dtype_string += "]"

      dt = np.dtype(eval(dtype_string))
      reordered_structured_array = np.empty(len(structured_array), dtype=dt)

      for i in range(len(data)):
        row = structured_array[i]
        reordered_structured_array[i] = tuple(row[index] for field in field_names)

      return  reordered_structured_array


  @classmethod
  def move_element_to_index(fields, types, field, target_index):
    # Find the index of the element in the list
    element_index = fields.index(field)

    # Remove the element from its current position
    fields.pop(element_index)
    typ = types.pop(element_index)

    # Insert the element at the target index
    fields.insert(target_index, field)
    types.insert(target_index, typ)

    return fields, types
