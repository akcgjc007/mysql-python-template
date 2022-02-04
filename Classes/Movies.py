from .DbStreamer import DbStreamer


class Movies(DbStreamer):

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
