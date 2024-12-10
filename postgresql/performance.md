# About Performance in postgresql

### query plan
- it stands for how the query is executed
- you can check with EXPLAIN clause
    - example : explain select * from item where id = '1'

### the type of table scan *1
#### types
  - Seq scan: scan all data without using any indexes
  - Index scan: scan with index
  - Bitmap heap scan: scan with bitmap (this is used in case of the low cardinality)

- Seq scan is slower than Index scan or Bitmap heap scan, of course. 

### index
#### spec
- attach index automatically to primary key  

#### performance
- As already mentioned above, you can search data with using index.
- if first column is not specified in a query, it is not used index. *2,*3,*4  

### reference
- postgres document
  - *1 https://www.postgresql.org/docs/current/indexes-multicolumn.html
  - *2 https://www.postgresql.org/docs/current/indexes-bitmap-scans.html
  - *3 https://www.postgresql.org/docs/17/using-explain.html
- *4 Software Design 2024年6月号