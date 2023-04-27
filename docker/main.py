import psycopg2
import csv
import pandas as pd
import os

dirname = os.path.dirname(__file__)
conn = psycopg2.connect(host="localhost", user="admin", password="admin", dbname="dataproj", port="32")
curs = conn.cursor()

curs.execute("""
CREATE TABLE IF NOT EXISTS stg.trump(
tweet_id char(30),
user_id char(30),
state_code char(30))
""")
conn.commit()

with open(dirname + '/elect/trump.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
            try:
                if row[19]:
                    data.append((
                        "{:.0f}".format(float(row[1])),
                        "{:.0f}".format(float(row[6])),
                        row[19]
                        ))
            except:
                continue
with open(dirname + '/hdfs/datanode/ods/trump.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(('tweet_id', 'user_id', 'state_code'))
        w.writerows(data)
f.close()

curs.executemany(
        """
        insert into stg.trump values (%s, %s, %s)
        """,
        data
    )
conn.commit()

curs.execute("""
CREATE table if not exists dds.trump (
	tweet_id char(30),
	user_id char(30),
	state_code char(30)
)
""")
conn.commit()

curs.execute("""
insert into dds.trump select * from stg.trump
""")
conn.commit()

curs.execute("""
drop table stg.trump 
""")
conn.commit()

conn.close()

print("oK")

conn = psycopg2.connect(host="localhost", user="admin", password="admin", dbname="dataproj", port="32")
curs = conn.cursor()

curs.execute("""
CREATE TABLE IF NOT EXISTS stg.biden(
tweet_id char(30),
user_id char(30),
state_code char(30))
""")
conn.commit()



with open(dirname + '/elect/biden.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
            try:
                if row[19]:
                    data.append((
                        "{:.0f}".format(float(row[1])),
                        "{:.0f}".format(float(row[6])),
                        row[19]
                        ))
            except:
                continue
with open(dirname + '/hdfs/datanode/ods/biden.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(('tweet_id', 'user_id', 'state_code'))
        w.writerows(data)
f.close()

curs.executemany(
        """
        insert into stg.biden values (%s, %s, %s)
        """,
        data
    )
conn.commit()

curs.execute("""
CREATE table if not exists dds.biden (
	tweet_id char(30),
	user_id char(30),
	state_code char(30)
)
""")
conn.commit()

curs.execute("""
insert into dds.biden select * from stg.biden
""")
conn.commit()

curs.execute("""
drop table stg.biden 
""")
conn.commit()

conn.close()

print("oK")

conn = psycopg2.connect(host="localhost", user="admin", password="admin", dbname="dataproj", port="32")
curs = conn.cursor()

curs.execute("""
CREATE TABLE IF NOT EXISTS stg.states(
state char(30),
abbreviation char(30))
""")
conn.commit()

with open(dirname + '/elect/states.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    fl = True
    for row in reader:
        if fl:
            fl = False
            continue
        data.append((row[0], row[1]))

with open(dirname + '/hdfs/datanode/ods/states.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(('state', 'abbreviation'))
        w.writerows(data)
f.close()

curs.executemany(
        """
        insert into stg.states values (%s, %s)
        """,
        data
    )
conn.commit()

curs.execute("""
CREATE table if not exists dds.states (
state char(30),
abbreviation char(30)
)
""")
conn.commit()

curs.execute("""
insert into dds.states select * from stg.states
""")
conn.commit()

curs.execute("""
drop table stg.states 
""")
conn.commit()



curs.execute("""
CREATE TABLE IF NOT EXISTS stg.votes(
state_code char(30),
vote_trump float,
vote_biden float)
""")
conn.commit()

with open(dirname + '/elect/votes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    data = []
    fl = True
    for row in reader:
        if fl:
            fl = False
            continue
        data.append((row[1], float(row[3]), float(row[4])))

with open(dirname + '/hdfs/datanode/ods/votes.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(('state_code', 'vote_trump', 'vote_biden'))
        w.writerows(data)
f.close()

curs.executemany(
        """
        insert into stg.votes values (%s, %s, %s)
        """,
        data
    )
conn.commit()

curs.execute("""
CREATE table if not exists dds.votes (
state_code char(30),
vote_trump float,
vote_biden float)
""")
conn.commit()

curs.execute("""
insert into dds.votes select * from stg.votes
""")
conn.commit()

curs.execute("""
drop table stg.votes 
""")
conn.commit()

curs.execute("""
CREATE TABLE dm.results as SELECT (co_b.biden_count/co_t.trump_count) as ratio_tweets, (dds.votes.vote_biden/dds.votes.vote_trump) as ratio_votes, dds.states.state  
FROM (SELECT COUNT(dds.biden.tweet_id)+0.0 as biden_count, dds.biden.state_code  
FROM dds.biden join dds.states on dds.biden.state_code = dds.states.abbreviation 
GROUP BY dds.biden.state_code) as co_b JOIN 
dds.states on co_b.state_code = dds.states.abbreviation
JOIN (SELECT COUNT(dds.trump.tweet_id)+0.0 as trump_count, dds.trump.state_code  
FROM dds.trump join dds.states on dds.trump.state_code = dds.states.abbreviation 
GROUP BY dds.trump.state_code) AS co_t on co_t.state_code = dds.states.abbreviation
join dds.votes on dds.states.abbreviation = dds.votes.state_code
""")
conn.commit()

curs.execute("select * from dm.results")
result = curs.fetchall()
correl = pd.DataFrame(result)
print(correl[1].astype(float).corr(correl[0].astype(float)))
conn.close()

print("oK")