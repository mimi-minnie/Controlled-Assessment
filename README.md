#Controlled Assessment: Task 1
==============================
##task 1
###design
####requirements

1) The exchange rates need to be able to be changed by user.

2) User should be able to enter amount to be converted.

3) The user should be able to select the chosen exchanging currencys.

4) The returned figure should be to two decimal places.

####Pseudocode:

```
BEGIN
INPUT currency to be converted, currency converting to (Pound Sterling/Euro/US Dollar/Japanese Yen)
ASSIGN to variables: c_type1, c_type2
MATCH c_type1, c_type2 to key in dictionary
IF c_type1 != Pound Sterling and c_type2 != Pound Sterling:
    CONVERT c_type1 into Pound Sterling
    CONVERT Pound Sterling into c_type2
    RETURN int of c_type2
ELSE:
    IDENTIFY Pound Sterling as c_type1 or c_type2
    CHANGE this value to or from Pound Sterling
    RETURN int of c_type2
...
```

####verables
Variables used | type | discussion
----|----|----
currencyFrom|intger|
currencyTo|intger|
symbols|list of strings|
rate|list of floats|

