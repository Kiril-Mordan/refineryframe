### Refiner class settings <a name="refiner-class-settings"></a>


```python
import os 
import sys 
import numpy as np
import pandas as pd
import logging
sys.path.append(os.path.dirname(sys.path[0])) 
from refineryframe.refiner import Refiner
```


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
    "missing_values": "ALL",
    "missing_types": "ALL",
    "inf_values": "NONE",
    "date_format": "NONE",
    "duplicates": "ALL",
    "date_range": "NONE",
    "numeric_range": "ALL"
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

#### using the main function to detect unexpected values


```python
tns.detect_unexpected_values()
```

    DEBUG:Refiner:=== checking column names and types
    DEBUG:Refiner:=== checking propper date format
    WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
    DEBUG:Refiner:=== checking expected date range
    DEBUG:Refiner:=== checking for presense of inf values in numeric colums
    WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
    WARNING:Refiner:Percentage of passed tests: 66.67%


#### extracting Refiner settings <a name="extracting-refiner-class-settings"></a>


```python
refiner_settings = tns.get_refiner_settings()
refiner_settings
```




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
     'unexpected_conditions': None,
     'ignore_values': [],
     'ignore_dates': [],
     'type_dict': {}}



### Initializing new clean Refiner


```python
tns2 = Refiner(dataframe = df)
```

#### scanning dataframe for unexpected conditions <a name="scanning-dataframe"></a>


```python
scanned_unexpected_exceptions = tns2.get_unexpected_exceptions_scaned()
scanned_unexpected_exceptions
```

    WARNING:Refiner:Column CharColumn: (NA) : 2 : 40.00%
    WARNING:Refiner:Column DateColumn2: (NA) : 4 : 80.00%
    WARNING:Refiner:Column NumericColumn: (NA) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (NA) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn2: (NA) : 4 : 80.00%
    WARNING:Refiner:Column DateColumn3: (1850-01-09) : 1 : 20.00%
    WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
    WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
    WARNING:Refiner:Percentage of passed tests: 71.43%





    {'col_names_types': 'NONE',
     'missing_values': 'ALL',
     'missing_types': 'ALL',
     'inf_values': 'ALL',
     'date_format': 'ALL',
     'duplicates': 'NONE',
     'date_range': 'NONE',
     'numeric_range': 'NONE'}



#### detection before applying settings


```python
tns2.detect_unexpected_values()
```

    WARNING:Refiner:Column CharColumn: (NA) : 2 : 40.00%
    WARNING:Refiner:Column DateColumn2: (NA) : 4 : 80.00%
    WARNING:Refiner:Column NumericColumn: (NA) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (NA) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn2: (NA) : 4 : 80.00%
    WARNING:Refiner:Column DateColumn3: (1850-01-09) : 1 : 20.00%
    WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
    WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
    WARNING:Refiner:Percentage of passed tests: 71.43%


#### using saved refiner settings for new instance <a name="recreating-refiner-class-settings"></a> 


```python
tns2.set_refiner_settings(refiner_settings)
```


```python
tns2.detect_unexpected_values()
```

    DEBUG:Refiner:=== checking column names and types
    DEBUG:Refiner:=== checking propper date format
    WARNING:Refiner:Column DateColumn2 has non-date values or unexpected format.
    DEBUG:Refiner:=== checking expected date range
    DEBUG:Refiner:=== checking for presense of inf values in numeric colums
    WARNING:Refiner:Column NumericColumn: (INF) : 2 : 40.00%
    WARNING:Refiner:Column NumericColumn_exepted: (INF) : 1 : 20.00%
    WARNING:Refiner:Percentage of passed tests: 66.67%



```python
tns3 = Refiner(dataframe = df, 
               unexpected_exceptions_duv = scanned_unexpected_exceptions)
```


```python
tns3.detect_unexpected_values()
print(f'duv score: {tns3.duv_score}')
```

    duv score: 1.0

