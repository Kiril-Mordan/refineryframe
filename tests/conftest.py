import pytest
import logging
import pandas as pd
import numpy as np
import attr
from datetime import datetime
from refineryframe.refiner import Refiner

@pytest.fixture(scope='session')
def b():
    yield 2



@pytest.fixture(scope='session')
def df():

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
    'CharColumn': ['Fół', None, np.nan, 'nót eXpęćTęd', '']})

    yield df


@pytest.fixture(scope='session')
def df1():

    df = pd.DataFrame({
    'num_id': ['1', '2', '3', '4', '5'],
    'NumericColumn': [1.0, -999.0, -999.0, -999.0, -999.0],
    'NumericColumn_exepted': [1.0, -999.0, -999.0, -999.0, -999.0],
    'NumericColumn2': [-999.0, -999.0, -999.0, -999.0, -999.0],
    'NumericColumn3': [1, 2, 3, 4, -999],
    'DateColumn': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'DateColumn2': ['1850-01-09', '2022-01-01', '1850-01-09', '1850-01-09', '1850-01-09'],
    'DateColumn3': ['1850-01-09', '2022-01-01', '1850-01-09', '1850-01-09', '1850-01-09'],
    'CharColumn': ['fol', 'missing', 'missing', 'not expected', 'missing']
})

    # Convert the DateColumns to datetime64[ns]
    df['DateColumn'] = pd.to_datetime(df['DateColumn'])
    df['DateColumn2'] = pd.to_datetime(df['DateColumn2'])
    df['DateColumn3'] = pd.to_datetime(df['DateColumn3'])

    yield df


@pytest.fixture(scope='session')
def df2():

    df = pd.DataFrame({
    'num_id': ['1', '2', '3', '4', '5'],
    'NumericColumn': [1.0, 0.0, 0.0, 0.0, 0.0],
    'NumericColumn_exepted': [1.0, 0.0, 0.0, 0.0, 0.0],
    'NumericColumn2': [0.0, 0.0, 0.0, 0.0, 0.0],
    'NumericColumn3': [1, 2, 0, 0, 0],
    'DateColumn': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'DateColumn2': ['1850-01-09', '2022-01-01', '1850-01-09', '1850-01-09', '1850-01-09'],
    'DateColumn3': ['1850-01-09', '2022-01-01', '1850-01-09', '1850-01-09', '1850-01-09'],
    'CharColumn': ['fol', 'miss', 'miss', 'miss', 'miss']
})

    # Convert the DateColumns to datetime64[ns]
    df['DateColumn'] = pd.to_datetime(df['DateColumn'])
    df['DateColumn2'] = pd.to_datetime(df['DateColumn2'])
    df['DateColumn3'] = pd.to_datetime(df['DateColumn3'])

    yield df

@pytest.fixture(scope='session')
def MISSING_TYPES():

    MISSING_TYPES = {'date_not_delivered': '1850-01-09',
                 'date_other_missing_type': '1850-01-08',
                 'numeric_not_delivered': -999,
                 'character_not_delivered': 'missing'}

    yield MISSING_TYPES

@pytest.fixture(scope='session')
def unexpected_exceptions():

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

    yield unexpected_exceptions


@pytest.fixture(scope='session')
def types_dict_str():

    types_dict_str = {'num_id' : 'int64',
                   'NumericColumn' : 'float64',
                   'NumericColumn_exepted' : 'float64',
                   'NumericColumn2' : 'float64',
                   'NumericColumn3' : 'int64',
                   'DateColumn' : 'datetime64[ns]',
                   'DateColumn2' : 'datetime64[ns]',
                   'DateColumn3' : 'datetime64[ns]',
                   'CharColumn' : 'object'}

    yield types_dict_str


@pytest.fixture(scope='session')
def replace_dict():

    replace_dict = {-996 : -999,
                "1000-01-09": "1850-01-09"}

    yield replace_dict

@pytest.fixture(scope='session')
def tns(df,replace_dict,unexpected_exceptions):

    tns = Refiner(dataframe = df,
              replace_dict = replace_dict,
              loggerLvl = logging.DEBUG,
              unexpected_exceptions_duv = unexpected_exceptions)

    yield tns

@pytest.fixture(scope='session')
def unexpected_conditions():

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

    yield unexpected_conditions