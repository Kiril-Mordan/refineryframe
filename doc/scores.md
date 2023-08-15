### Data quality scores <a class="anchor" id="scores"></a>

##### DUV score <a class="anchor" id="duv_scores"></a>

The score is the result of checking general conditions with `.detect_unexpected_values()`.

It is a percentange of checks that passed.
Ideally the score is 1, worse case scenario the score is 0.

$$
score_{duv} = \frac{\sum^{n}_{i=1} \text{check}_{i}}{n}
$$

##### RUV scores <a class="anchor" id="ruv_scores"></a>

The scores are the result of cleaning data with `.replace_unexpected_values()`.

The goal of those scores originated in determining whether the dataset can be used to train a model or not, based on missing or effectivelly missing values. The most advanced one is RUV_score2, aims to accurately classiffy if the dataset is hopeless, which can be used as safeguad to signal critical fall in quality of collected data in production. These scores are experimental so use them with causion.

* RUV_score0 is the simplest one, it is just a differance between 1 and proportion of number of missing values to number of all values available in the dataframe. This can be understood and usable portions of the dataframe.

$$
score_{ruv0} = 1 - \frac{\sum^{n*m}_{i=1;j=1} \text{unusable}_{ij}}{n*m}
$$

* RUV_score1 is a simplified version of RUV_score2, the proportions of medians are not squared with makes the score worse for classification but better for traking data quality over time.

$med_{col} = med{\frac{\sum^{n}_{i=1} \text{unusable}_{i}}{n}}$

count number of unexpected values along each column, divide it by number of rows and calculate median of that proportion

$med_{row} = med{\frac{\sum^{m}_{j=1} \text{unusable}_{j}}{m}}$

count number of unexpected values along each row, divide it by number of columns and calculate median of that proportion

$$
score_{ruv1} =  1 - \frac{med_{col} + med_{row}}{2}
$$

* RUV_score2 takes advantage of the fact that if one has too many rows or columns of data that are completly unusable or some kind of mix of those situations, the dataset does become unusable. The values below 0.5 supposedly indicate completelly unusable dataset.

$$
score_{ruv2} =  1 - \frac{med_{col}^2 + med_{row}^2}{2}
$$

