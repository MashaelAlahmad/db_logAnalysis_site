# db_logAnalysis_site
Logs Analysis:
this project build an internal reporting tool that will use information from the database to discover
what kind of articles the site's readers like.
The database contains newspaper articles, as well as the web server log for the site.
The log has a database row for each time a reader loaded a web page. Using that information, your code
will answer questions about the site's user activity.
The program you write in this project will run from the command line.
 It won't take any input from the user. Instead, it will connect to that database, use SQL queries to
 analyze the log data, and print out the answers to some questions.




# Getting Started:
- you need to install python(https://www.python.org) and psql(https://www.postgresql.org/)
- you need to download FSND vagrant machine [https://github.com/scottharman/Udacity-FSND-VM-Vagrant]
- The application requires psycopg2 module 
- put the file newsdata.sql into vagrant [download from here https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip]

-To load the data, cd into the vagrant directory and $vagrant up then $vagrant ssh  after that use the command psql -d news -f newsdata.sql to establish your database.
- you can run the news.py file inside the vm in your terminal using $python news.py




# Explore the data:
once you have the data loaded into your database, connect to your database using psql -d news and explore the tables using the \dt and \d table commands and select statements.
\dt — display tables — lists the tables that are available in the database.
\d table — (replace table with the name of a table) — shows the database schema for that particular table.




# License:
Copyright (c) [2018] [Mashael Alahamd] This project is licensed under the MIT License - see the (LICENSE.md)[https://choosealicense.com/licenses/mit/] file for details.
