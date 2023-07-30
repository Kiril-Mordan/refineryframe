[![Build status](https://github.com/Kiril-Mordan/refineryframe/workflows/Tests/badge.svg)](https://github.com/{github_id}/{repository}/workflows/{workflow_name}/badge.svg)
[![Downloads](https://static.pepy.tech/badge/refineryframe)](https://pepy.tech/project/refineryframe)
[![Version](https://img.shields.io/pypi/v/refineryframe)](https://pypi.org/project/refineryframe/)
![](https://img.shields.io/github/license/Kiril-Mordan/refineryframe)
![](https://img.shields.io/pypi/pyversions/refineryframe)




# refineryframe

<a><img src="https://github.com/Kiril-Mordan/refineryframe/blob/main/images/logo.png" width="35%" height="35%" align="right" /></a>


The goal of the package is to simplify life for data scientists, that have to deal with imperfect raw data. The package suppose to detect and clean unexpected values, while doubling as safeguard in production code based on predifined conditions that arise from business assumptions or any other source. The package is well suited to be an initial preprocessing step in ml pipelines situated between data gathering and training/scoring steps.

Developed by Kyrylo Mordan (c) 2023

## Installation

Install `refineryframe` via pip with

```bash
pip install refineryframe
```


# Feature List

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

## Package usage example


```python
import os 
import sys 
import numpy as np
import pandas as pd
import logging
sys.path.append(os.path.dirname(sys.path[0])) 
from refineryframe.refiner import Refiner
```

### Creating example data (exceptionally messy dataframe)


```python
df = pd.DataFrame({
    'num_id' : [1, 2, 3, 4, 5],
    'NumericColumn': [1, -np.inf, np.inf,np.nan, None],
    'NumericColumn_exepted': [1, -996, np.inf,np.nan, None],
    'NumericColumn2': [None, None, 1,None, None],
    'NumericColumn3': [1, 2, 3, 4, 5],
    'DateColumn': pd.date_range(start='2022-01-01', periods=5),
    'DateColumn2': [pd.NaT,pd.to_datetime('2022-01-01'),pd.NaT,pd.NaT,pd.NaT],
    'DateColumn3': ['2122-05-01',
                    '2022-01-01',
                    '2021-01-01',
                    '1000-01-09',
                    '1850-01-09'],
    'CharColumn': ['Fół', None, np.nan, 'nót eXpęćTęd', '']
})

df
```




<div>
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
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_id</th>
      <th>NumericColumn</th>
      <th>NumericColumn_exepted</th>
      <th>NumericColumn2</th>
      <th>NumericColumn3</th>
      <th>DateColumn</th>
      <th>DateColumn2</th>
      <th>DateColumn3</th>
      <th>CharColumn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>1</td>
      <td>2022-01-01</td>
      <td>NaT</td>
      <td>2122-05-01</td>
      <td>Fół</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>-inf</td>
      <td>-996.0</td>
      <td>NaN</td>
      <td>2</td>
      <td>2022-01-02</td>
      <td>2022-01-01</td>
      <td>2022-01-01</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>inf</td>
      <td>inf</td>
      <td>1.0</td>
      <td>3</td>
      <td>2022-01-03</td>
      <td>NaT</td>
      <td>2021-01-01</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>2022-01-04</td>
      <td>NaT</td>
      <td>1000-01-09</td>
      <td>nót eXpęćTęd</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5</td>
      <td>2022-01-05</td>
      <td>NaT</td>
      <td>1850-01-09</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



#### Defining specification for the dataframe


```python
MISSING_TYPES = {'date_not_delivered': '1850-01-09',
                 'date_other_missing_type': '1850-01-08',
                 'numeric_not_delivered': -999,
                 'character_not_delivered': 'missing'}
```


```python
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
```


```python
replace_dict = {-996 : -999,
                "1000-01-09": "1850-01-09"}
```

### Initializing Refiner class


```python
tns = Refiner(dataframe = df,
              replace_dict = replace_dict,
              loggerLvl = logging.DEBUG,
              unexpected_exceptions_duv = unexpected_exceptions)
```

##### function for detecting column types


```python
tns.get_type_dict_from_dataframe()
```




    {'num_id': 'int64',
     'NumericColumn': 'float64',
     'NumericColumn_exepted': 'float64',
     'NumericColumn2': 'float64',
     'NumericColumn3': 'int64',
     'DateColumn': 'datetime64[ns]',
     'DateColumn2': 'datetime64[ns]',
     'DateColumn3': 'object',
     'CharColumn': 'object'}



##### adding expected types


```python
types_dict_str = {'num_id' : 'int64', 
                   'NumericColumn' : 'float64', 
                   'NumericColumn_exepted' : 'float64', 
                   'NumericColumn2' : 'float64', 
                   'NumericColumn3' : 'int64', 
                   'DateColumn' : 'datetime64[ns]', 
                   'DateColumn2' : 'datetime64[ns]', 
                   'DateColumn3' : 'datetime64[ns]', 
                   'CharColumn' : 'object'}
```

#### Check independent conditions


```python
tns.check_missing_types()
tns.check_missing_values()
tns.check_inf_values()
tns.check_col_names_types()
tns.check_date_format()
tns.check_duplicates()
tns.check_numeric_range()
```

    WARNING:Refiner:Column DateColumn3: (1850-01-09) : 1 : 20.00%
    WARNING:Refiner:Column NumericColumn: (NA) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (NA) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn2: (NA) : 4 : 80.00%
    WARNING:Refiner:Column DateColumn2: (NA) : 4 : 80.00%
    WARNING:Refiner:Column CharColumn: (NA) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
    WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.


##### moulding types


```python
tns.set_types(type_dict = types_dict_str)
```


```python
tns.get_type_dict_from_dataframe() 
```




    {'num_id': 'int64',
     'NumericColumn': 'float64',
     'NumericColumn_exepted': 'float64',
     'NumericColumn2': 'float64',
     'NumericColumn3': 'int64',
     'DateColumn': 'datetime64[ns]',
     'DateColumn2': 'datetime64[ns]',
     'DateColumn3': 'datetime64[ns]',
     'CharColumn': 'object'}



#### Using the main function to detect unexpected values


```python
tns.detect_unexpected_values(earliest_date = "1920-01-01",
                         latest_date = "DateColumn3")
```

    DEBUG:Refiner:=== checking column names and types
    DEBUG:Refiner:=== checking for presence of missing values
    WARNING:Refiner:Column CharColumn: (NA) : 2 : 40.00%
    WARNING:Refiner:Column DateColumn2: (NA) : 4 : 80.00%
    WARNING:Refiner:Column NumericColumn: (NA) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn2: (NA) : 4 : 80.00%
    DEBUG:Refiner:=== checking for presence of missing types
    WARNING:Refiner:Column DateColumn3: (1850-01-09) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (-999) : 1 : 20.00%
    DEBUG:Refiner:=== checking propper date format
    WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
    DEBUG:Refiner:=== checking expected date range
    WARNING:Refiner:** Not all dates in DateColumn are later than DateColumn3
    WARNING:Refiner:Column DateColumn : future date : 4 : 80.00%
    DEBUG:Refiner:=== checking for presense of inf values in numeric colums
    WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
    DEBUG:Refiner:=== checking expected numeric range
    WARNING:Refiner:Percentage of passed tests: 50.00%



```python
tns.duv_score
```




    0.5



#### Using function to replace unexpected values with missing types


```python
tns.replace_unexpected_values(numeric_lower_bound = "NumericColumn3",
                                numeric_upper_bound = 4,
                                earliest_date = "1920-01-02",
                                latest_date = "DateColumn2",
                                unexpected_exceptions = {"irregular_values": "NONE",
                                                            "date_range": "DateColumn",
                                                            "numeric_range": "NONE",
                                                            "capitalization": "NONE",
                                                            "unicode_character": "NONE"})

```

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



```python
tns.dataframe.dtypes
```




    num_id                           object
    NumericColumn                   float64
    NumericColumn_exepted           float64
    NumericColumn2                  float64
    NumericColumn3                    int64
    DateColumn               datetime64[ns]
    DateColumn2              datetime64[ns]
    DateColumn3              datetime64[ns]
    CharColumn                       object
    dtype: object



#### Use complex targeted conditions


```python
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
```

##### - to detect unexpected values


```python
tns.detect_unexpected_values(unexpected_conditions = unexpected_conditions)
```

    DEBUG:Refiner:=== checking column names and types
    DEBUG:Refiner:=== checking for presence of missing values
    DEBUG:Refiner:=== checking for presence of missing types
    WARNING:Refiner:Column CharColumn: (missing) : 3 : 60.00%
    WARNING:Refiner:Column DateColumn2: (1850-01-09) : 4 : 80.00%
    WARNING:Refiner:Column DateColumn3: (1850-01-09) : 4 : 80.00%
    WARNING:Refiner:Column NumericColumn: (-999) : 4 : 80.00%
    WARNING:Refiner:Column NumericColumn_exepted: (-999) : 4 : 80.00%
    WARNING:Refiner:Column NumericColumn2: (-999) : 5 : 100.00%
    WARNING:Refiner:Column NumericColumn3: (-999) : 1 : 20.00%
    DEBUG:Refiner:=== checking propper date format
    DEBUG:Refiner:=== checking expected date range
    DEBUG:Refiner:=== checking for presense of inf values in numeric colums
    DEBUG:Refiner:=== checking expected numeric range
    DEBUG:Refiner:=== checking additional cons
    DEBUG:Refiner:Replace numeric missing with with zero
    WARNING:Refiner:Replace numeric missing with with zero :: 1
    DEBUG:Refiner:Detect/Replace numeric values in certain column with zeros if > 2
    WARNING:Refiner:Detect/Replace numeric values in certain column with zeros if > 2 :: 2
    WARNING:Refiner:Percentage of passed tests: 75.00%


##### - to replace unecpected values


```python
tns.replace_unexpected_values(unexpected_conditions = unexpected_conditions)
```

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



```python
tns.dataframe
```




<div>
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
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_id</th>
      <th>NumericColumn</th>
      <th>NumericColumn_exepted</th>
      <th>NumericColumn2</th>
      <th>NumericColumn3</th>
      <th>DateColumn</th>
      <th>DateColumn2</th>
      <th>DateColumn3</th>
      <th>CharColumn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>2022-01-01</td>
      <td>1850-01-09</td>
      <td>1850-01-09</td>
      <td>fol</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>2022-01-02</td>
      <td>2022-01-01</td>
      <td>2022-01-01</td>
      <td>miss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>2022-01-03</td>
      <td>1850-01-09</td>
      <td>1850-01-09</td>
      <td>miss</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>2022-01-04</td>
      <td>1850-01-09</td>
      <td>1850-01-09</td>
      <td>miss</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>2022-01-05</td>
      <td>1850-01-09</td>
      <td>1850-01-09</td>
      <td>miss</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```

    DEBUG:Refiner:=== checking column names and types
    DEBUG:Refiner:=== checking for presence of missing values
    DEBUG:Refiner:=== checking propper date format
    DEBUG:Refiner:=== checking expected date range
    DEBUG:Refiner:=== checking for presense of inf values in numeric colums
    DEBUG:Refiner:=== checking expected numeric range


#### Scores


```python
print(f'duv_score: {tns.duv_score :.4}')
print(f'ruv_score0: {tns.ruv_score0 :.4}')
print(f'ruv_score1: {tns.ruv_score1 :.4}')
print(f'ruv_score2: {tns.ruv_score2 :.4}')
```

    duv_score: 1.0
    ruv_score0: 0.8222
    ruv_score1: 0.8889
    ruv_score2: 0.9753

