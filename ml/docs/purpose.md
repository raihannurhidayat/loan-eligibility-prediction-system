# German Credit Data Dictionary
## Overview
The German Credit dataset is a well-known dataset from the UCI Machine Learning Repository, used for credit risk assessment. It contains 1000 loan applicants with 20 features and a binary target indicating creditworthiness (Good/Bad). The dataset is often used for classification tasks, especially in credit scoring.
**Dataset file used**: `dataset_credit.csv` (numerical encoding of categorical attributes, as provided in the `deepanshu88/Datasets` GitHub repository).
Source: [UCI Statlog German Credit Data](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)
## Target Variable
| Column Name | Description | Values | Meaning |
|-------------|-------------|--------|----------|
| `Creditability` | Creditworthiness of the applicant | `1` | Good (creditworthy) |
| | | | `0` | Bad (not creditworthy) |
*Note: In the original UCI dataset, the target is coded as `1` = Good, `2` = Bad. The provided CSV may have recoded it to `0`/`1`.*
## Feature Dictionary
The following table lists all 20 features (columns 2–21 in the CSV). The numerical values correspond to the original categorical codes (e.g., A11 → 1, A12 → 2, etc.).
| No | CSV Column | UCI Attribute | Description | Type | Numerical Code | Original Code | Meaning |
|----|-------------|---------------|-------------|------|---------------|--------------|---------|
| 1 | `Account Balance` | Attribute 1 | Status of existing checking account | Categorical | `1` | A11 | … < 0 DM |
| | | | | | `2` | A12 | 0 ≤ … < 200 DM |
| | | | | | `3` | A13 | … ≥ 200 DM / salary assignments for ≥ 1 year |
| | | | | | `4` | A14 | no checking account |
| 2 | `Duration of Credit (month)` | Attribute 2 | Duration in months | Numerical | – | – | integer (months) |
| 3 | `Payment Status of Previous Credit` | Attribute 3 | Credit history | Categorical | `0` | A30 | no credits taken / all credits paid back duly |
| | | | | | `1` | A31 | all credits at this bank paid back duly |
| | | | | | `2` | A32 | existing credits paid back duly till now |
| | | | | | `3` | A33 | delay in paying off in the past |
| | | | | | `4` | A34 | critical account / other credits existing (not at this bank) |
| 4 | `Purpose` | Attribute 4 | Purpose of the credit | Categorical | `0` | A40 | car (new) |
| | | | | | `1` | A41 | car (used) |
| | | | | | `2` | A42 | furniture/equipment |
| | | | | | `3` | A43 | radio/television |
| | | | | | `4` | A44 | domestic appliances |
| | | | | | `5` | A45 | repairs |
| | | | | | `6` | A46 | education |
| | | | | | `7` | A47 | vacation (does not exist?) |
| | | | | | `8` | A48 | retraining |
| | | | | | `9` | A49 | business |
| | | | | `10` | A410 | others |
| 5 | `Credit Amount` | Attribute 5 | Credit amount | Numerical | – | – | integer (DM) |
| 6 | `Value Savings/Stocks` | Attribute 6 | Savings account/bonds | Categorical | `1` | A61 | … < 100 DM |
| | | | | | `2` | A62 | 100 ≤ … < 500 DM |
| | | | | | `3` | A63 | 500 ≤ … < 1000 DM |
| | | | | | `4` | A64 | … ≥ 1000 DM |
| | | | | | `5` | A65 | unknown / no savings account |
| 7 | `Length of current employment` | Attribute 7 | Present employment since | Categorical | `1` | A71 | unemployed |
| | | | | | `2` | A72 | … < 1 year |
| | | | | | `3` | A73 | 1 ≤ … < 4 years |
| | | | | | `4` | A74 | 4 ≤ … < 7 years |
| | | | | | `5` | A75 | … ≥ 7 years |
| 8 | `Instalment per cent` | Attribute 8 | Installment rate in percentage of disposable income | Numerical | – | – | integer (%) |
| 9 | `Sex & Marital Status` | Attribute 9 | Personal status and sex | Categorical | `1` | A91 | male : divorced/separated |
| | | | | | `2` | A92 | female : divorced/separated/married |
| | | | | | `3` | A93 | male : single |
| | | | | | `4` | A94 | male : married/widowed |
| | | | | | `5` | A95 | female : single |
| 10 | `Guarantors` | Attribute 10 | Other debtors / guarantors | Categorical | `1` | A101 | none |
| | | | | | `2` | A102 | co-applicant |
| | | | | | `3` | A103 | guarantor |
| 11 | `Duration in Current address` | Attribute 11 | Present residence since | Numerical | – | – | integer (years) |
| 12 | `Most valuable available asset` | Attribute 12 | Property | Categorical | `1` | A121 | real estate |
| | | | | | `2` | A122 | building society savings agreement / life insurance |
| | | | | | `3` | A123 | car or other, not in attribute 6 |
| | | | | | `4` | A124 | unknown / no property |
| 13 | `Age (years)` | Attribute 13 | Age in years | Numerical | – | – | integer (years) |
| 14 | `Concurrent Credits` | Attribute 14 | Other installment plans | Categorical | `1` | A141 | bank |
| | | | | | `2` | A142 | stores |
| | | | | | `3` | A143 | none |
| 15 | `Type of apartment` | Attribute 15 | Housing | Categorical | `1` | A151 | rent |
| | | | | | `2` | A152 | own |
| | | | | | `3` | A153 | for free |
| 16 | `No of Credits at this Bank` | Attribute 16 | Number of existing credits at this bank | Numerical | – | – | integer |
| 17 | `Occupation` | Attribute 17 | Job | Categorical | `1` | A171 | unemployed / unskilled – non-resident |
| | | | | | `2` | A172 | unskilled – resident |
| | | | | | `3` | A173 | skilled employee / official |
| | | | | | `4` | A174 | management / self-employed / highly qualified employee / officer |
| 18 | `No of dependents` | Attribute 18 | Number of people being liable to provide maintenance for | Numerical | – | – | integer |
| 19 | `Telephone` | Attribute 19 | Telephone | Categorical | `1` | A191 | none |
| | | | | | `2` | A192 | yes, registered under the customer's name |
| 20 | `Foreign Worker` | Attribute 20 | Foreign worker | Categorical | `1` | A201 | yes |
| | | | | | `2` | A202 | no |
## Notes on Encoding
- The dataset provided (`dataset_credit.csv`) uses **numerical encoding** for categorical attributes. The mapping above shows the conversion from the original UCI codes (A11, A12, …) to the numbers (1,2,…) as they appear in the CSV.
- For example, in the CSV, `Account Balance` = 1 corresponds to `A11` (… < 0 DM), 2 corresponds to `A12` (0 ≤ … < 200 DM), etc.
- Some categorical attributes have an order (ordinal), e.g., employment length, savings amount.
- The target `Creditability` is binary; in the CSV it is `1` for Good and `0` for Bad (or vice versa – check the actual distribution).
## Dataset Summary
- **Instances**: 1000 (700 Good, 300 Bad)
- **Features**: 20 (7 numerical, 13 categorical)
- **Missing values**: None
- **Source repository**: [deepanshu88/Datasets](https://github.com/deepanshu88/Datasets) (see file `UploadedFiles/german_credit.csv`)
## References
1. UCI Machine Learning Repository. *Statlog (German Credit Data)*. [https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data))
2. Grömping, U. (2019). *South German Credit – Correcting a Widely Used Data Set*. [https://archive.ics.uci.edu/ml/datasets/south+german+credit+update)](https://archive.ics.uci.edu/ml/datasets/south+german+credit+update)
3. GitHub: deepanshu88/Datasets. [https://github.com/deepanshu88/Datasets](https://github.com/deepanshu88/Datasets)
4. Pennsylvania State University. *Analysis of German Credit Data*. [https://online.stat.psu.edu/stat857/print/book/export/html/215/](https://online.stat.psu.edu/stat857/print/book/export/html/215/)
---
*Generated on 2026-05-04 for user ACER.*