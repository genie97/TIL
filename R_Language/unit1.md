## R Language UNIT1

1. Basic Computation

   ```R
   #Add
   >1+3
   [1] 4
   
   #Sub
   >5-2
   [1] 3
   
   #Mul
   >5*3
   [1] 15
   
   #Div
   >5%/%3
   [1] 1
   
   #Mod
   >5%%3
   [1] 2
   
   #exp
   >5^2
   [1] 25
   ```

2. Vector

   > - One types of data stored
   > - Create character vector: c("","","","")
   > - Create number vector: c( , , , )
   > - Index starts at **1**

   ```
   c("USA", "KOREA")
   C(78,91)
   ```

3. seq() function

   > - seq(from, to, by)

   ```R
   >seq(0,100,2)
    [1]   0   2   4   6   8  10  12  14  16  18  20  22  24  26  28  30  32  34  36
   [20]  38  40  42  44  46  48  50  52  54  56  58  60  62  64  66  68  70  72  74
   [39]  76  78  80  82  84  86  88  90  92  94  96  98 100
   ```

4.  Data Frame

   > - Two-dimensional array-like structure
   > - Each column(variables) contains values of one variable
   > - Each rows(observations) contains one set of values from each column
   > - variable_name = data.frame([column header], ...)

   ```R
   Country = c("USA", "kOREA")
   LifeExpectancy = c(79, 75)
   CountryData = data.frame(Country, LifeExpextancy)
   ```

5.  Binding column and row

   > To only show values of one column
   >
   > [data_variable_name]$[column_name]
   >
   > Row binding
   >
   > [new_data_variable_name] =  rbind([data_name], [data_name])

   ```R
   #Binding Column
   Country = c("USA", "kOREA")
   LifeExpectancy = c(79, 75)
   CountryData = data.frame(Country, LifeExpextancy)
   CountryData$Population = c(1990000,1300000)
   
   #Binding Row
   Country = c("Australia", "Greece")
   LifeExpectancy = c(82, 81)
   Population = c(230505, 11125)
   NewCountryData = data.frame(Country, LifeExpectancy, Population)
   AllCountryData  = rbind(CountryData, NewCountryData)
   ```

6. Check and Set workspace

   > - getwd()
   > - setwd("workspace~")

7. Read csv file

   > - variable_name = read.csv("filename.csv")
   >
   > - str(variable_name): Data structure, number of variables, variable name, number of observations, preview of observations
   >
   > - summary(variable_name): Centralization trend and distribution summary

   ```R
   Country = c("Australia", "Greece")
   str(Country)
   summary(Country)
   ```

8. Subsetting

   ```R
   WHO_Europe = subset(WHO, Region=="Europe")
   ```
