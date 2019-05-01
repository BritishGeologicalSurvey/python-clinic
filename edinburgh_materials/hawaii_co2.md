# Hawaii CO2 plot

### Exercise 1 (data manipulation)

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

### Exercise 2 (plotting)

Recreate the following plot using Pandas and Matplotlib.

![co2 plot](https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_data_mlo.png)


The following code will load the data into a Pandas dataframe:

```python
df = pd.read_csv('co2_mm_mlo.txt', 
                 comment='#', 
                 sep="\s+", 
                 header=None, 
                 index_col=1, 
                 names=names, 
                 na_values=[-99.99, -1], 
                 parse_dates={'date':[0, 1]}
                 )
```

Features to recreate:

+ 'average' column plotted in red
+ 'trend' column plotted in black (behind the red)
+ Axis labels
+ Title
+ "Scripps Institution..." text box
+ "April 2019" text box
+ Axis minor ticks
+ Embedded images

Bonus extra features:

+ Legend
+ 5-year running maximum line
+ 5-year running minimum line
