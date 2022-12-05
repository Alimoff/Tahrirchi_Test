Question:     - How would you automate this process so that we can get new datasets every day?


Answer:   

I would use Cron. You can use Cron any time you want to automate something, like an OS job or a Python script. Needless to say, but an automated Python script can do basically anything.

First step- 

It has it's own special parameters to set timer. Some of them: 

"* * * * 1-5" -  	once every day of the week,

"* * * * *" - once a minute,

"0 * * * *" - once an hour,

"0 0 * * *" - once a day at 0:00,

"0 0 * * 0" - once a week etc.

Second step -

I would compare each new link with old ones when it starts scrapping in every time.I think it will work perfectly.





Question:     - What file format would you use to store this data?


Answer:       I would prefer to use CSV(Comma Separated Values) file format. CSV is one of the most common file formats for storing textual data.
These files can be opened using a wide variety of programs including Notepad. The reason behind using this format over others is its ability to store complex data in a simple and readable way.
Moreover, CSV files offer more security as compared to file formats like JSON. In python, it is easy to read these types of files using a special library called Pandas.





Question:    - How would you evaluate the quality of the collected data?


Answer:       Firstly, I would determine the quality of the data collected by checking whether it is appropriate for the purpose for which it was collected.  
Secondly, Collected data can be evaluated by comparing the ratio of error and blank data to the total collected data.
