# inserting data

add_student = ("INSERT INTO students "
               "(name, group_num, year)"
               "VALUES (%s, %s, %s)")

add_professor = ("INSERT INTO professors "
                 "(name)"
                 "VALUES (%s)")

add_course = ("INSERT INTO courses "
              "(name, type, prof_id)"
              "VALUES (%s, %s, %s)")

add_year = ("INSERT INTO year "
            "(course_id, year)"
            "VALUES (%s, %s)")

add_group = ("INSERT INTO group_num "
             "(course_id, group_num)"
             "VALUES (%s, %s)")

add_choice = ("INSERT INTO by_choice "
              "(course_id, stud_id)"
              "VALUES (%s, %s)")

# selecting data

# simple select
student_by_id = "SELECT name, group_num, year FROM students WHERE stud_id=%s"

student_by_name = "SELECT group_num, year FROM students WHERE name=%s"

group_list = "SELECT name FROM students WHERE group_num=%s"

year_list = "SELECT name FROM students WHERE year=%s"

# simple select from multiple tables
# two tables
professors_courses = ("SELECT courses.name FROM courses, professors "
                      "WHERE professors.prof_id=courses.prof_id "
                      "AND professors.name=%s")

year_courses = ("SELECT courses.name FROM courses, year "
                "WHERE year.year=%s AND year.course_id=courses.course_id")

# three tables
choice_list = ("SELECT students.name, students.group_num, students.year "
               "FROM students, by_choice, courses "
               "WHERE courses.name=%s AND by_choice.course_id=courses.course_id "
               "AND by_choice.stud_id=students.stud_id")

# complex select
students_courses = ("SELECT name, course_id FROM courses "
                    "WHERE course_id IN(SELECT by_choice.course_id FROM by_choice, students "
                    "WHERE by_choice.stud_id=students.stud_id AND students.name=%s)"
                    "OR "
                    "course_id IN(SELECT group_num.course_id FROM group_num, students "
                    "WHERE group_num.group_num=students.group_num AND students.name=%s) "
                    "OR "
                    "course_id IN(SELECT year.course_id FROM year, students "
                    "WHERE year.year=students.year AND students.name=%s)")

# updating data

change_students_group = "UPDATE students SET group_num=%s WHERE name=%s"

change_students_year = "UPDATE students SET group_num=%s, year=%s WHERE name=%s"

change_students_name = "UPDATE students SET name=%s WHERE name=%s"
