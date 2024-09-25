### 複数の配列について、一方のソート順に合わせてソート
select array_agg(e.u1 order by e.u1), array_agg(e.u2 order by e.u1) from (SELECT unnest(Array[3, 1, 5]) as u1, unnest(Array[10, 11, 15]) as u2) as e 

### 正規表現によって文字列を置換
 - table  (reg_sample)  
 id    | value  
 apple | This is a apple.  
 orange| That is an orange.
 apple apple | An apple is an apple
 - query

```sql
select id, REGEXP_REPLACE(value, 'apple', 'melon') as value from reg_sample
```

 - result  
 id	| value  
orange | That is an orange.  
apple | This is a melon.  
apple apple | An melon is an apple.  

 - option  
'g' を付加すると正規表現と一致する全ての文字列を置換可能

```sql
select id, REGEXP_REPLACE(value, 'apple', 'melon', 'g') as value from reg_sample
```
- result
``` 
 id	| value  
orange | That is an orange.  
apple | This is a melon.  
apple apple | An melon is an melon.  
```