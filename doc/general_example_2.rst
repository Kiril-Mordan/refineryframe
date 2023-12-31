Refiner class settings 
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   import os 
   import sys 
   import numpy as np
   import pandas as pd
   import logging
   sys.path.append(os.path.dirname(sys.path[0])) 
   from refineryframe.refiner import Refiner
   from refineryframe.demo import tiny_example

Initializing Refiner class
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   tns = Refiner(dataframe = tiny_example['dataframe'],
                 replace_dict = tiny_example['replace_dict'],
                 loggerLvl = logging.DEBUG,
                 unexpected_exceptions_duv = {
                                               "col_names_types": "NONE",
                                               "missing_values": "ALL",
                                               "missing_types": "ALL",
                                               "inf_values": "NONE",
                                               "date_format": "NONE",
                                               "duplicates": "ALL",
                                               "date_range": "NONE",
                                               "numeric_range": "ALL"
                                           })

using the main function to detect unexpected values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   tns.detect_unexpected_values()

::

   DEBUG:Refiner:=== checking for column name duplicates
   DEBUG:Refiner:=== checking column names and types
   DEBUG:Refiner:=== checking propper date format
   WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
   WARNING:Refiner:Date format score was lower then expected: 50.0 < 100
   DEBUG:Refiner:=== checking expected date range
   DEBUG:Refiner:=== checking for presense of inf values in numeric colums
   WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
   WARNING:Refiner:Inf score was lower then expected: 88.0 < 100
   WARNING:Refiner:Percentage of passed tests: 71.43%

extracting Refiner settings 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   refiner_settings = tns.get_refiner_settings()
   refiner_settings

::

   {'replace_dict': {-996: -999, '1000-01-09': '1850-01-09'},
    'MISSING_TYPES': {'date_not_delivered': '1850-01-09',
     'numeric_not_delivered': -999,
     'character_not_delivered': 'missing'},
    'expected_date_format': '%Y-%m-%d',
    'mess': 'INITIAL PREPROCESSING',
    'shout_type': 'HEAD2',
    'logger_name': 'Refiner',
    'loggerLvl': 10,
    'dotline_length': 50,
    'lower_bound': -inf,
    'upper_bound': inf,
    'earliest_date': '1900-08-25',
    'latest_date': '2100-01-01',
    'ids_for_dedup': 'ALL',
    'unexpected_exceptions_duv': {'col_names_types': 'NONE',
     'missing_values': 'ALL',
     'missing_types': 'ALL',
     'inf_values': 'NONE',
     'date_format': 'NONE',
     'duplicates': 'ALL',
     'date_range': 'NONE',
     'numeric_range': 'ALL'},
    'unexpected_exceptions_ruv': {'irregular_values': 'NONE',
     'date_range': 'NONE',
     'numeric_range': 'NONE',
     'capitalization': 'NONE',
     'unicode_character': 'NONE'},
    'unexpected_exceptions_error': {'col_name_duplicates': False,
     'col_names_types': False,
     'missing_values': False,
     'missing_types': False,
     'inf_values': False,
     'date_format': False,
     'duplicates': False,
     'date_range': False,
     'numeric_range': False},
    'thresholds': {'cmt_scores': {'numeric_score': 100,
      'date_score': 100,
      'cat_score': 100},
     'cmv_scores': {'missing_values_score': 100},
     'ccnt_scores': {'missing_score': 100, 'incorrect_dtypes_score': 100},
     'inf_scores': {'inf_score': 100},
     'cdf_scores': {'date_format_score': 100},
     'dup_scores': {'row_dup_score': 100, 'key_dup_score': 100},
     'cnr_scores': {'low_numeric_score': 100, 'upper_numeric_score': 100},
     'cdr_scores': {'early_dates_score': 100, 'future_dates_score': 100}},
    'unexpected_conditions': None,
    'ignore_values': [],
    'ignore_dates': [],
    'type_dict': {}}

Initializing new clean Refiner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   tns2 = Refiner(dataframe = tiny_example['dataframe'])

scanning dataframe for unexpected conditions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   scanned_unexpected_exceptions = tns2.get_unexpected_exceptions_scaned()
   scanned_unexpected_exceptions

::

   WARNING:Refiner:Column CharColumn: (NA) : 2 : 40.00%
   WARNING:Refiner:Column DateColumn2: (NA) : 4 : 80.00%
   WARNING:Refiner:Column NumericColumn: (NA) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (NA) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn2: (NA) : 4 : 80.00%
   WARNING:Refiner:Missing values score was lower then expected: 53.33 < 100
   WARNING:Refiner:Column DateColumn3: (1850-01-09) : 1 : 20.00%
   WARNING:Refiner:Character score was lower then expected: 97.14 < 100
   WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
   WARNING:Refiner:Date format score was lower then expected: 50.0 < 100
   WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
   WARNING:Refiner:Inf score was lower then expected: 88.0 < 100
   WARNING:Refiner:Percentage of passed tests: 73.33%





   {'col_names_types': 'NONE',
    'missing_values': 'ALL',
    'missing_types': 'ALL',
    'inf_values': 'ALL',
    'date_format': 'ALL',
    'duplicates': 'NONE',
    'date_range': 'NONE',
    'numeric_range': 'NONE'}

detection before applying settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   tns2.detect_unexpected_values()

::

   WARNING:Refiner:Column CharColumn: (NA) : 2 : 40.00%
   WARNING:Refiner:Column DateColumn2: (NA) : 4 : 80.00%
   WARNING:Refiner:Column NumericColumn: (NA) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (NA) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn2: (NA) : 4 : 80.00%
   WARNING:Refiner:Missing values score was lower then expected: 53.33 < 100
   WARNING:Refiner:Column DateColumn3: (1850-01-09) : 1 : 20.00%
   WARNING:Refiner:Character score was lower then expected: 97.14 < 100
   WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
   WARNING:Refiner:Date format score was lower then expected: 50.0 < 100
   WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
   WARNING:Refiner:Inf score was lower then expected: 88.0 < 100
   WARNING:Refiner:Percentage of passed tests: 73.33%

using saved refiner settings for new instance 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   tns2.set_refiner_settings(refiner_settings)

.. code:: python

   tns2.detect_unexpected_values()

::

   DEBUG:Refiner:=== checking for column name duplicates
   DEBUG:Refiner:=== checking column names and types
   DEBUG:Refiner:=== checking propper date format
   WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
   WARNING:Refiner:Date format score was lower then expected: 50.0 < 100
   DEBUG:Refiner:=== checking expected date range
   DEBUG:Refiner:=== checking for presense of inf values in numeric colums
   WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
   WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
   WARNING:Refiner:Inf score was lower then expected: 88.0 < 100
   WARNING:Refiner:Percentage of passed tests: 71.43%

.. code:: python

   tns3 = Refiner(dataframe = tiny_example['dataframe'], 
                  unexpected_exceptions_duv = scanned_unexpected_exceptions)

.. code:: python

   tns3.detect_unexpected_values()
   print(f'duv score: {tns3.duv_score}')

::

   duv score: 1.0
