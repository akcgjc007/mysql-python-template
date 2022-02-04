from DbStreamer.main import *
from data import *
import csv

obj = DbStreamer(host="localhost", user="root",
                 password="0000", database="mydb")

file = open('./data/movies.csv')

for row in list(csv.reader(file))[1:]:
    name = row[0]
    genre = row[1]
    studio = row[2]
    audience_score = row[3]
    profitability = row[4]
    rotten_tomatoes = row[5]
    worldwide_gross = row[6][1:-1]
    year = row[7]
    obj.insert_into_movies(
        name, genre, studio, audience_score, profitability,
        rotten_tomatoes, worldwide_gross, year
    )


# n = 5
# users = [
#     ["james554", "James", "james@gmail.com", "0000"],
#     ["thomas999", "Thomas", "thomas@gmail.com", "0000"],
#     ["harry555", "Harry", "harry@gmail.com", "0000"],
#     ["vivek999", "Vivek", "vivek@gmail.com", "0000"],
#     ["anupam110", "Anupam", "anupam@gmail.com", "0000"],
# ]

# for user in users:
#     obj.insert_into_users(user[0], user[1], user[2], user[3])

# total_answers = 0
# for i in range(n):
#     obj.insert_into_questions(titles[i], descriptions[i], users[i][0])
#     obj.upvote_question(users[i][0], i+1)

#     for answer in answers[i]:
#         obj.insert_into_answers(answer, i+1, users[i][0])
#         total_answers += 1
#         obj.upvote_answer(users[i][0], total_answers)

#     for tag in tags[i]:
#         obj.insert_into_tags(tag, i+1)

# obj.update_question(1, "dummpy question description")
# obj.update_answer(1, "dummy answer description")
# obj.delete_question(1)
# obj.delete_answer(1)


# print(obj.search_question("dummy"))
# print(obj.search_answers(2))
# print(obj.search_by_tag("py"))
# print(obj.search_question_by_id(2))
# print(obj.get_top_questions())

# print(obj.check_user("a@iitgn.ac.in", "abcd"))
# obj.insert_into_tokens("james554", "1e758b81-fc45-467f-b375-2b6a218048c5")
# print(obj.check_token("2e758b81-fc45-467f-b375-2b6a218048c5"))

# print(obj.calc_reputation("thomas999"))
