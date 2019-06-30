# DROP TABLES
    # SONGPLAYS TABLE
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
    # USERS TABLE
user_table_drop = "DROP TABLE IF EXISTS users"
    # SONGS TABLE
song_table_drop = "DROP TABLE IF EXISTS songs"
    # ARTISTS TABLE
artist_table_drop = "DROP TABLE IF EXISTS artists"
    # TIME TABLE
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
    # SONGPLAYS TABLE
songplay_table_create = ("""
CREATE TABLE songplays(songplay_id serial primary key,start_time timestamp not null,user_id int not null,level varchar,song_id varchar,artist_id varchar,session_id int not null,location varchar,user_agent varchar)
""")
    # USERS TABLE
user_table_create = ("""
CREATE TABLE users(user_id int primary key,first_name varchar,last_name varchar,gender varchar,level varchar)
""")
    # SONGS TABLE
song_table_create = ("""
CREATE TABLE songs(song_id varchar primary key,title varchar not null,artist_id varchar not null,year int,duration float)
""")
    # ARTISTS TABLE
artist_table_create = ("""
CREATE TABLE artists(artist_id varchar primary key,name varchar not null,location varchar,lattitude float,longitude float)
""")
    # TIME TABLE
time_table_create = ("""
CREATE TABLE time(start_time timestamp primary key,hour int,day int,week int,month int,year int,weekday int)
""")

# INSERT RECORDS
    # SONGPLAYS TABLE
songplay_table_insert = ("""
INSERT INTO songplays(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")
    # USERS TABLE
user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE set level = EXCLUDED.level
""")
    # SONGS TABLE
song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING """)
    # ARTISTS TABLE
artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, lattitude, longitude)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")
    # TIME TABLE
time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS
song_select = ("""
select s.song_id songid, s.artist_id artistid
from songs s inner join artists a on s.artist_id = a.artist_id
where s.title = %s and a.name = %s and s.duration = %s
""")

# QUERY LISTS
    # CREATE ALL TABLES
create_table_queries =[songplay_table_create,user_table_create,song_table_create,artist_table_create,time_table_create]
    # DROP ALL TABLES
drop_table_queries = [songplay_table_drop,user_table_drop,song_table_drop,artist_table_drop,time_table_drop]