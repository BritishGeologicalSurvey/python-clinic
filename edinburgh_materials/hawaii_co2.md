# Hawaii CO2 plot

#### Exercise

+ Navigate to [https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html](https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html).
+ Download [Mauna Loa CO2 monthly mean
  data](ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt)
+ Write some Python to divide the data into CSV files for each decade, each
  containing just decimal date and the average value for each month.

> Useful modules include `csv`, `datetime`, `pandas`

#### Example output

Names:
```
co2_mm_1960s.csv
co2_mm_1970s.csv
co2_mm_1980s.csv
co2_mm_1990s.csv
etc...
```

Contents:
```
decimal_date,interpolated
1958.208,315.71
1958.292,317.45
1958.375,317.50
1958.458,317.10
1958.542,315.86
1958.625,314.93
1958.708,313.20
1958.792,312.66
```

Bonus exercises:

+ reformat the date to YYYY-MM-DD format
+ append the mean concentration for the decade to the filename.
+ recreate this plot:

![co2 plot](https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_data_mlo.png)
