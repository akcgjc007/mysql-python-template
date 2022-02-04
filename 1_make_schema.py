from DbStreamer.main import DbStreamer

obj = DbStreamer(host="localhost", user="root",
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

# obj.run_my_query("""
# -- Questions
# create table Questions(
#     id int(10) unsigned auto_increment primary key,
#     title varchar(500) unique not null,
#     description varchar(15000) not null,
#     user_id varchar(50),
#     upvotes int(10) unsigned default 0,

#     foreign key (user_id) references Users(id)

# );
# """)


# obj.run_my_query("""
# -- Answers
# create table Answers(
#     id int(10) unsigned auto_increment primary key,
#     description varchar(15000) not null,
#     question_id int(10) unsigned not null,
#     user_id varchar(50),
#     upvotes int(10) unsigned default 0,

#     foreign key (user_id) references Users(id),
#     foreign key (question_id) references Questions(id)
# );
# """)

# obj.run_my_query("""
#     -- QuestionVotes
# create table QuestionVotes(
#     user_id varchar(50) not null,
#     question_id int(10) unsigned not null,

#     foreign key (user_id) references Users(id),
#     foreign key (question_id) references Questions(id),

#     primary key(user_id, question_id)
# );
# """)

# obj.run_my_query("""
# -- AnswerVotes
# create table AnswerVotes(
#     user_id varchar(50) not null,
#     answer_id int(10) unsigned not null,

#     foreign key (user_id) references Users(id),
#     foreign key (answer_id) references Answers(id),

#     primary key(user_id, answer_id)
# );
# """)

# obj.run_my_query("""
# -- Tags
# create table Tags(
#     name varchar(50) not null,
#     question_id int(10) unsigned not null,
#     foreign key (question_id) references Questions(id),
#     primary key(name, question_id)
# );
# """)

# obj.run_my_query("""
# -- Tokens
# create table Tokens (
#     user_id varchar(50) not null,
#     token varchar(50) not null primary key,
#     foreign key (user_id) references Users(id)
# );
# """)
