from Classes.Movies import Movies

obj = Movies(host="localhost", user="root",
             password="0000", database="mydb")
obj.initialize_database()

obj.run_my_query("""
-- Movies
create table Movies(
    id int(10) unsigned auto_increment primary key,
    name varchar(100) default null,
    genre varchar(100) default null,
    studio varchar(100) default null,
    audience_score int(10) unsigned default null,
    profitability float(20, 10) default null,
    rotten_tomatoes int(10) unsigned default null,
    worldwide_gross float(10, 5) default null,
    year int(10) unsigned default null
);

""")
