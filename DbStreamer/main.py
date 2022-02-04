import mysql.connector as mysql


class DbStreamer:
    """Constructor"""

    def __init__(self, host, user, password, database):
        self.conn = mysql.connect(
            host=host, user=user, passwd=password, db=database)
        self.run_my_query("use mydb;")
        return

    """Destructor"""

    def __del__(self):
        self.conn.commit()
        self.conn.close()
        return

    """Function to run single query"""

    def run_my_query(self, command):
        _cursor = self.conn.cursor()
        _cursor.execute(command)
        results = _cursor.fetchall()
        return results

    """Reset the database"""

    def initialize_database(self):
        self.run_my_query("drop database if exists mydb;")
        self.run_my_query("create database mydb;")
        self.run_my_query("use mydb;")

    """Database related functions"""

    """Insert a movie into Movies Table"""

    def insert_into_movies(self, name, genre, studio, audience_score, profitability, rotten_tomatoes, worldwide_gross, year):
        sql = "insert into Movies(name, genre, studio, audience_score, profitability, rotten_tomatoes, worldwide_gross, year) values (%s, %s, %s, %s, %s, %s, %s, %s);"
        val = (name, genre, studio, audience_score,
               profitability, rotten_tomatoes, worldwide_gross, year)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val))
        results = _cursor.fetchall()
        return results

    """Delete a from from Movies Table"""

    def delete_in_movies(self, id):
        sql = "delete from Movies where id = %s;"
        val = (id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val, ))
        results = _cursor.fetchall()
        return results
