# SQL 문제풀이

#### Revising the Select Query I

Query all columns for all American cities in the **CITY** table with populations larger than `100000`. The **CountryCode** for America is `USA`.

The **CITY** table is described as follows:

![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

```mysql
SELECT *
FROM CITY
WHERE COUNTRYCODE = "USA"
AND POPULATION  > 100000
```



#### Revising the Select Query II

Query the **NAME** field for all American cities in the **CITY** table with populations larger than `120000`. The *CountryCode* for America is `USA`.

The **CITY** table is described as follows:
![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

```mysql
SELECT NAME 
FROM CITY
WHERE COUNTRYCODE="USA"
AND POPULATION > 120000
```



#### Select All

Query all columns (attributes) for every row in the **CITY** table.

The **CITY** table is described as follows:
![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

```mysql
SELECT *
FROM CITY
```



#### Select By ID

Query all columns for a city in **CITY** with the *ID* `1661`.

The **CITY** table is described as follows:
![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

```mysql
SELECT *
FROM CITY
WHERE ID = 1661;
```



#### Japanese Cities' Attributes

Query all attributes of every Japanese city in the **CITY** table. The **COUNTRYCODE** for Japan is `JPN`.

The **CITY** table is described as follows:

![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

```mysql
SELECT *
FROM CITY
WHERE COUNTRYCODE = "JPN"
```



#### Japanese Cities' Names

Query the names of all the Japanese cities in the **CITY** table. The **COUNTRYCODE** for Japan is `JPN`.
The **CITY** table is described as follows:
![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

```mysql
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = "JPN"
```



#### Weather Observation Station 1

Query a list of **CITY** and **STATE** from the **STATION** table.
The **STATION** table is described as follows:
![Station.jpg](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where **LAT_N** is the northern latitude and **LONG_W** is the western longitude.

```mysql
SELECT CITY, STATE
FROM STATION
```



#### Weather Observation Station 3

````mysql
SELECT DISTINCT CITY
FROM STATION
WHERE ID % 2 = 0
````



#### Weather Observation Station 4

Find the difference between the total number of **CITY** entries in the table and the number of distinct **CITY** entries in the table.
The **STATION** table is described as follows:

![Station.jpg](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where **LAT_N** is the northern latitude and **LONG_W** is the western longitude.

For example, if there are three records in the table with **CITY** values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'. The query returns 1, because 

total number of records  - number of unique city names = 3 - 2 = 1.

```mysql
SELECT COUNT(CITY) -  COUNT(DISTINCT CITY)
FROM STATION
```

