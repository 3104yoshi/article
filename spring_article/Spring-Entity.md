## What's Entity class?
- must be annotated @Entity
- must have a public or protected no-arg constructor

### @column
- add this to field corresponding with column in table  
- specified column name as below  
    - @column(name="column_name")   
- If not @column specified, the column name is the same as Java field  

### @Id
- represent primary key  
- possible to create automatically primary key by @GeneratedValue
    - the way to generate primary key is specified by the enum of Generationtype
    - and also, you can define own generation strategy to create impl of IdentifierGenerator