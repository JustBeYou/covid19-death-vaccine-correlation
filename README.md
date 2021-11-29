Correlation between vaccination and COVID-19 reported deaths
===

# Data gathering
* Worldmeters
* Google vaccination statistics

## Data cleaning
* removed countries with missing data
* removed countries with invalid data (more than 100% percent vaccination or other errors like this)
* converted per million metrics to per cent metrics

## Details
* correlations are calculated using Pearson's coefficient
* there are about 100-120 analyzed countries in the final results

## Results
It seems that after the threshold of 20% complete vaccination, a negative correlation between deaths and vaccionation
rate occurs.

```bash
> python .\covid.py
Usage: python .\covid.py <min population in millions> <min vaccination percent>
> python .\covid.py 1 10
Countries in the dataset: 113
Correlations:
                   deaths  vaccines  deaths_lastweek
deaths           1.000000   0.09066         0.587014
vaccines         0.090660   1.00000        -0.034700
deaths_lastweek  0.587014  -0.03470         1.000000
> python .\covid.py 1 20
Countries in the dataset: 100
Correlations:
                   deaths  vaccines  deaths_lastweek
deaths           1.000000 -0.036172         0.564028
vaccines        -0.036172  1.000000        -0.134231
deaths_lastweek  0.564028 -0.134231         1.000000
```