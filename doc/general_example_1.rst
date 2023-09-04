Creating example data (exceptionally messy dataframe)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   import os 
   import sys 
   import numpy as np
   import pandas as pd
   import logging
   sys.path.append(os.path.dirname(sys.path[0])) 
   from refineryframe.refiner import Refiner
   from refineryframe.demo import tiny_example

.. code:: python

   df = tiny_example['dataframe']
   df

.. container::

   .. raw:: html

      <style scoped>
          .dataframe tbody tr th:only-of-type {
              vertical-align: middle;
          }

          .dataframe tbody tr th {
              vertical-align: top;
          }

          .dataframe thead th {
              text-align: right;
          }
      </style>

   .. raw:: html

      <table border="1" class="dataframe">

   .. raw:: html

      <thead>

   .. raw:: html

      <tr style="text-align: right;">

   .. raw:: html

      <th>

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   num_id

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   NumericColumn

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   NumericColumn_exepted

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   NumericColumn2

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   NumericColumn3

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   DateColumn

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   DateColumn2

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   DateColumn3

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   CharColumn

   .. raw:: html

      </th>

   .. raw:: html

      </tr>

   .. raw:: html

      </thead>

   .. raw:: html

      <tbody>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   0

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   1

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaN

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-01

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaT

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2122-05-01

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   Fół

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   1

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   2

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   -inf

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   -996.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaN

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-02

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-01

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-01

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   None

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   2

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   3

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   inf

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   inf

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   3

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-03

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaT

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2021-01-01

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaN

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   3

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   4

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaN

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaN

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaN

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   4

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-04

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaT

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1000-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   nót eXpęćTęd

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   4

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   5

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaN

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaN

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaN

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   5

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-05

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   NaT

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1850-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      </tbody>

   .. raw:: html

      </table>

Defining specification for the dataframe 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   MISSING_TYPES = tiny_example['MISSING_TYPES']
   MISSING_TYPES

::

   {'date_not_delivered': '1850-01-09',
    'date_other_missing_type': '1850-01-08',
    'numeric_not_delivered': -999,
    'character_not_delivered': 'missing'}

.. code:: python

   replace_dict = tiny_example['replace_dict']
   replace_dict

::

   {-996: -999, '1000-01-09': '1850-01-09'}

.. code:: python

   unexpected_exceptions = {
       "col_names_types": "NONE",
       "missing_values": ["NumericColumn_exepted"],
       "missing_types": "NONE",
       "inf_values": "NONE",
       "date_format": "NONE",
       "duplicates": "ALL",
       "date_range": "NONE",
       "numeric_range": "NONE"
   }

Initializing Refiner class 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   tns = Refiner(dataframe = df,
                 replace_dict = replace_dict,
                 loggerLvl = logging.DEBUG,
                 unexpected_exceptions_duv = unexpected_exceptions)

function for detecting column types 
''''''''''''''''''''''''''''''''''''

.. code:: python

   tns.get_type_dict_from_dataframe()

::

   {'num_id': 'int64',
    'NumericColumn': 'float64',
    'NumericColumn_exepted': 'float64',
    'NumericColumn2': 'float64',
    'NumericColumn3': 'int64',
    'DateColumn': 'datetime64[ns]',
    'DateColumn2': 'datetime64[ns]',
    'DateColumn3': 'object',
    'CharColumn': 'object'}

adding expected types
'''''''''''''''''''''

.. code:: python

   types_dict_str = {'num_id' : 'int64', 
                      'NumericColumn' : 'float64', 
                      'NumericColumn_exepted' : 'float64', 
                      'NumericColumn2' : 'float64', 
                      'NumericColumn3' : 'int64', 
                      'DateColumn' : 'datetime64[ns]', 
                      'DateColumn2' : 'datetime64[ns]', 
                      'DateColumn3' : 'datetime64[ns]', 
                      'CharColumn' : 'object'}

Use of simple general conditions 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check independent conditions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   tns.check_missing_types()
   tns.check_missing_values()
   tns.check_inf_values()
   tns.check_col_names_types()
   tns.check_date_format()
   tns.check_duplicates()
   tns.check_numeric_range()

::

   WARNING:Refiner:Column DateColumn3: (1850-01-09) : 1 : 20.00%
   WARNING:Refiner:Character score was lower then expected: 97.14 < 100
   WARNING:Refiner:Column NumericColumn: (NA) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (NA) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn2: (NA) : 4 : 80.00%
   WARNING:Refiner:Column DateColumn2: (NA) : 4 : 80.00%
   WARNING:Refiner:Column CharColumn: (NA) : 2 : 40.00%
   WARNING:Refiner:Missing values score was lower then expected: 53.33 < 100
   WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
   WARNING:Refiner:Inf score was lower then expected: 94.0 < 100
   WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
   WARNING:Refiner:Date format score was lower then expected: 50.0 < 100

moulding types 
'''''''''''''''

.. code:: python

   tns.set_types(type_dict = types_dict_str)

.. code:: python

   tns.get_type_dict_from_dataframe() 

::

   {'num_id': 'int64',
    'NumericColumn': 'float64',
    'NumericColumn_exepted': 'float64',
    'NumericColumn2': 'float64',
    'NumericColumn3': 'int64',
    'DateColumn': 'datetime64[ns]',
    'DateColumn2': 'datetime64[ns]',
    'DateColumn3': 'datetime64[ns]',
    'CharColumn': 'object'}

Using the main function to detect unexpected values 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   tns.detect_unexpected_values(earliest_date = "1920-01-01",
                            latest_date = "DateColumn3")

::

   DEBUG:Refiner:=== checking for column name duplicates
   DEBUG:Refiner:=== checking column names and types
   DEBUG:Refiner:=== checking for presence of missing values
   WARNING:Refiner:Column CharColumn: (NA) : 2 : 40.00%
   WARNING:Refiner:Column DateColumn2: (NA) : 4 : 80.00%
   WARNING:Refiner:Column NumericColumn: (NA) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn2: (NA) : 4 : 80.00%
   WARNING:Refiner:Missing values score was lower then expected: 52.0 < 100
   DEBUG:Refiner:=== checking for presence of missing types
   WARNING:Refiner:Column DateColumn3: (1850-01-09) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (-999) : 1 : 20.00%
   WARNING:Refiner:Numeric score was lower then expected: 98.75 < 100
   WARNING:Refiner:Date score was lower then expected: 96.0 < 100
   DEBUG:Refiner:=== checking propper date format
   WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
   WARNING:Refiner:Date format score was lower then expected: 66.67 < 100
   DEBUG:Refiner:=== checking expected date range
   WARNING:Refiner:** Not all dates in DateColumn are later than DateColumn3
   WARNING:Refiner:Column DateColumn : future date : 4 : 80.00%
   WARNING:Refiner:Future dates score was lower then expected: 80.0 < 100
   DEBUG:Refiner:=== checking for presense of inf values in numeric colums
   WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
   WARNING:Refiner:Inf score was lower then expected: 88.0 < 100
   DEBUG:Refiner:=== checking expected numeric range
   WARNING:Refiner:Percentage of passed tests: 53.85%

.. code:: python

   tns.duv_score

::

   0.5384615384615384

Using function to replace unexpected values with missing types 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   tns.replace_unexpected_values(numeric_lower_bound = "NumericColumn3",
                                   numeric_upper_bound = 4,
                                   earliest_date = "1920-01-02",
                                   latest_date = "DateColumn2",
                                   unexpected_exceptions = {"irregular_values": "NONE",
                                                               "date_range": "DateColumn",
                                                               "numeric_range": "NONE",
                                                               "capitalization": "NONE",
                                                               "unicode_character": "NONE"})

::

   DEBUG:Refiner:=== replacing missing values in category cols with missing types
   DEBUG:Refiner:=== replacing all upper case characters with lower case
   DEBUG:Refiner:=== replacing character unicode to latin
   DEBUG:Refiner:=== replacing missing values in date cols with missing types
   DEBUG:Refiner:=== replacing missing values in numeric cols with missing types
   DEBUG:Refiner:=== replacing values outside of expected date range
   DEBUG:Refiner:=== replacing values outside of expected numeric range
   DEBUG:Refiner:** Usable values in the dataframe:  44.44%
   DEBUG:Refiner:** Uncorrected data quality score:  32.22%
   DEBUG:Refiner:** Corrected data quality score:  52.57%

Use of complex targeted conditions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   unexpected_conditions = {
       '1': {
           'description': 'Replace numeric missing with with zero',
           'group': 'regex_columns',
           'features': r'^Numeric',
           'query': "{col} < 0",
           'warning': True,
           'set': 0
       },
       '2': {
           'description': "Clean text column from '-ing' endings and 'not ' beginings",
           'group': 'regex clean',
           'features': ['CharColumn'],
           'query': [r'ing', r'^not.'],
           'warning': False,
           'set': ''
       },
       '3': {
           'description': "Detect/Replace numeric values in certain column with zeros if > 2",
           'group': 'multicol mapping',
           'features': ['NumericColumn3'],
           'query': '{col} > 2',
           'warning': True,
           'set': 0
       },
       '4': {
           'description': "Replace strings with values if some part of the string is detected",
           'group': 'string check',
           'features': ['CharColumn'],
           'query': f"CharColumn.str.contains('cted', regex = True)",
           'warning': False,
           'set': 'miss'
       }
       }

- to detect unexpected values 
''''''''''''''''''''''''''''''

.. code:: python

   tns.detect_unexpected_values(unexpected_conditions = unexpected_conditions)

::

   DEBUG:Refiner:=== checking for column name duplicates
   DEBUG:Refiner:=== checking column names and types
   WARNING:Refiner:Incorrect data types:
   WARNING:Refiner:Column num_id: actual dtype is object, expected dtype is int64
   WARNING:Refiner:Dtypes score was lower then expected: 88.89 < 100
   DEBUG:Refiner:=== checking for presence of missing values
   DEBUG:Refiner:=== checking for presence of missing types
   WARNING:Refiner:Column CharColumn: (missing) : 3 : 60.00%
   WARNING:Refiner:Column DateColumn2: (1850-01-09) : 4 : 80.00%
   WARNING:Refiner:Column DateColumn3: (1850-01-09) : 4 : 80.00%
   WARNING:Refiner:Column NumericColumn: (-999) : 4 : 80.00%
   WARNING:Refiner:Column NumericColumn_exepted: (-999) : 4 : 80.00%
   WARNING:Refiner:Column NumericColumn2: (-999) : 5 : 100.00%
   WARNING:Refiner:Column NumericColumn3: (-999) : 1 : 20.00%
   WARNING:Refiner:Numeric score was lower then expected: 78.46 < 100
   WARNING:Refiner:Date score was lower then expected: 84.0 < 100
   WARNING:Refiner:Character score was lower then expected: 91.43 < 100
   DEBUG:Refiner:=== checking propper date format
   DEBUG:Refiner:=== checking expected date range
   DEBUG:Refiner:=== checking for presense of inf values in numeric colums
   DEBUG:Refiner:=== checking expected numeric range
   DEBUG:Refiner:=== checking additional cons
   DEBUG:Refiner:Replace numeric missing with with zero
   WARNING:Refiner:Replace numeric missing with with zero :: 1
   DEBUG:Refiner:Detect/Replace numeric values in certain column with zeros if > 2
   WARNING:Refiner:Detect/Replace numeric values in certain column with zeros if > 2 :: 2
   WARNING:Refiner:Percentage of passed tests: 69.23%

- to replace unexpected values 
'''''''''''''''''''''''''''''''

.. code:: python

   tns.replace_unexpected_values(unexpected_conditions = unexpected_conditions)

::

   DEBUG:Refiner:=== replacing missing values in category cols with missing types
   DEBUG:Refiner:=== replacing all upper case characters with lower case
   DEBUG:Refiner:=== replacing character unicode to latin
   DEBUG:Refiner:=== replacing with additional cons
   DEBUG:Refiner:Replace numeric missing with with zero
   DEBUG:Refiner:Clean text column from '-ing' endings and 'not ' beginings
   DEBUG:Refiner:Detect/Replace numeric values in certain column with zeros if > 2
   DEBUG:Refiner:Replace strings with values if some part of the string is detected
   DEBUG:Refiner:=== replacing missing values in date cols with missing types
   DEBUG:Refiner:=== replacing missing values in numeric cols with missing types
   DEBUG:Refiner:=== replacing values outside of expected date range
   DEBUG:Refiner:=== replacing values outside of expected numeric range
   DEBUG:Refiner:** Usable values in the dataframe:  82.22%
   DEBUG:Refiner:** Uncorrected data quality score:  88.89%
   DEBUG:Refiner:** Corrected data quality score:  97.53%

.. code:: python

   tns.dataframe

.. container::

   .. raw:: html

      <style scoped>
          .dataframe tbody tr th:only-of-type {
              vertical-align: middle;
          }

          .dataframe tbody tr th {
              vertical-align: top;
          }

          .dataframe thead th {
              text-align: right;
          }
      </style>

   .. raw:: html

      <table border="1" class="dataframe">

   .. raw:: html

      <thead>

   .. raw:: html

      <tr style="text-align: right;">

   .. raw:: html

      <th>

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   num_id

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   NumericColumn

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   NumericColumn_exepted

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   NumericColumn2

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   NumericColumn3

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   DateColumn

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   DateColumn2

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   DateColumn3

   .. raw:: html

      </th>

   .. raw:: html

      <th>

   CharColumn

   .. raw:: html

      </th>

   .. raw:: html

      </tr>

   .. raw:: html

      </thead>

   .. raw:: html

      <tbody>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   0

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   1

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-01

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1850-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1850-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   fol

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   1

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   2

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-02

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-01

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-01

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   miss

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   2

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   3

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-03

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1850-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1850-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   miss

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   3

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   4

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-04

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1850-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1850-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   miss

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      <tr>

   .. raw:: html

      <th>

   4

   .. raw:: html

      </th>

   .. raw:: html

      <td>

   5

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0.0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   0

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   2022-01-05

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1850-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   1850-01-09

   .. raw:: html

      </td>

   .. raw:: html

      <td>

   miss

   .. raw:: html

      </td>

   .. raw:: html

      </tr>

   .. raw:: html

      </tbody>

   .. raw:: html

      </table>

.. code:: python

   tns.detect_unexpected_values(unexpected_exceptions = {
       "col_names_types": "NONE",
       "missing_values": "NONE",
       "missing_types": "ALL",
       "inf_values": "NONE",
       "date_format": "NONE",
       "duplicates": "ALL",
       "date_range": "NONE",
       "numeric_range": "NONE"
   })

::

   DEBUG:Refiner:=== checking for column name duplicates
   DEBUG:Refiner:=== checking column names and types
   WARNING:Refiner:Incorrect data types:
   WARNING:Refiner:Column num_id: actual dtype is object, expected dtype is int64
   WARNING:Refiner:Dtypes score was lower then expected: 88.89 < 100
   DEBUG:Refiner:=== checking for presence of missing values
   DEBUG:Refiner:=== checking propper date format
   DEBUG:Refiner:=== checking expected date range
   DEBUG:Refiner:=== checking for presense of inf values in numeric colums
   DEBUG:Refiner:=== checking expected numeric range
   WARNING:Refiner:Percentage of passed tests: 90.00%

Scores
^^^^^^

.. code:: python

   print(f'duv_score: {tns.duv_score :.4}')
   print(f'ruv_score0: {tns.ruv_score0 :.4}')
   print(f'ruv_score1: {tns.ruv_score1 :.4}')
   print(f'ruv_score2: {tns.ruv_score2 :.4}')

::

   duv_score: 0.9
   ruv_score0: 0.8222
   ruv_score1: 0.8889
   ruv_score2: 0.9753
