import mysql.connector
from mysql.connector import errorcode

from conf import user_pswd


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


DB_NAME = 'final_project'

TABLES = {}

TABLES['students'] = (
    "CREATE TABLE `students` ("
    "  `stud_id` int NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(255) NOT NULL,"
    "  `group_num` int NOT NULL,"
    "  `year` int NOT NULL,"
    "  PRIMARY KEY (`stud_id`)"
    ") ENGINE=InnoDB")

TABLES['professors'] = (
    "CREATE TABLE `professors` ("
    "  `prof_id` int NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(255) NOT NULL,"
    "  PRIMARY KEY (`prof_id`)"
    ") ENGINE=InnoDB")

TABLES['courses'] = (
    "CREATE TABLE `courses` ("
    "  `course_id` int NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(255) NOT NULL,"
    "  `type` varchar(255) NOT NULL,"
    "  `prof_id` int NOT NULL,"
    "  PRIMARY KEY (`course_id`)"
    ") ENGINE=InnoDB")

TABLES['year'] = (
    "CREATE TABLE `year` ("
    "  `course_id` int NOT NULL,"
    "  `year` int NOT NULL"
    ") ENGINE=InnoDB")

TABLES['group_num'] = (
    "CREATE TABLE `group_num` ("
    "  `course_id` int NOT NULL,"
    "  `group_num` int NOT NULL"
    ") ENGINE=InnoDB")

TABLES['by_choice'] = (
    "CREATE TABLE `by_choice` ("
    "  `course_id` int NOT NULL,"
    "  `stud_id` int NOT NULL"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='user', password=user_pswd)
cursor = cnx.cursor()

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()