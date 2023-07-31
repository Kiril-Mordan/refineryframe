## Feature List

- `refineryframe.refiner.Refiner.check_col_names_types` - checks if a given dataframe has the same column names as keys in a given dictionary
and those columns have the same types as items in the dictionary.
- `refineryframe.refiner.Refiner.check_date_format` - checks if the values in the datetime columns of the input dataframe
have the expected 'YYYY-MM-DD' format.
- `refineryframe.refiner.Refiner.check_date_range` - checks if dates are in expected ranges.
- `refineryframe.refiner.Refiner.check_duplicates` - checks for duplicates in a pandas DataFrame.
- `refineryframe.refiner.Refiner.check_inf_values` - counts the inf values in each column of a pandas DataFrame.
- `refineryframe.refiner.Refiner.check_missing_types` - takes a DataFrame and a dictionary of missing types as input,
and searches for any instances of these missing types in each column of the DataFrame.
- `refineryframe.refiner.Refiner.check_missing_values` - counts the number of NaN, None, and NaT values in each column of a pandas DataFrame.
- `refineryframe.refiner.Refiner.check_numeric_range` - checks if numeric values are in expected ranges.
- `refineryframe.refiner.Refiner.detect_unexpected_values` - detects unexpected values in a pandas DataFrame.
- `refineryframe.refiner.Refiner.get_type_dict_from_dataframe` - returns a dictionary or string representation of a dictionary containing the data types
of each column in the given pandas DataFrame.
- `refineryframe.refiner.Refiner.replace_unexpected_values` - replaces unexpected values in a pandas DataFrame with missing types.
- `refineryframe.refiner.Refiner.set_type_dict` - changes the data types of the columns in the given DataFrame
based on a dictionary of intended data types.
- `refineryframe.refiner.Refiner.set_types` - changes the data types of the columns in the given DataFrame
based on a dictionary of intended data types.
