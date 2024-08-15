*** usage
**** aws s3 ls s3://[s3 location name]/ | ./fetch_based_on_timestamp.sh "2024-07-31 22:14:00"

*** prompt for generating script (3 chat in total)

1
In below table, how can I extract filename after the date I designated?

<<Table>> 
2024-07-31 22:12:43          0
2024-07-31 22:13:12         10 aaaaa.txt
2024-07-31 22:14:42         10 bbbbb.txt

<<Table Structure>>
This table is consists of 4 columns and potentially unlimited rows.
Column1 : date, the format is yyyy-MM-dd
Column2 : time, the format is hh:mm:ss
Column3 : file size
Column4 : file name

And also, the condition is below when you create source code.

<<source code language>>
You must write source code in bash.

<<output format>>
File name list with line separator

2
How can we change source code when we pass the input to above program via pipe.

3
Can you change it to pass target date as arguments?