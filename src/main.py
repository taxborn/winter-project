import utils
from models.student import Student
from models.course import Course


def main():
    # Used https://app.json-generator.com/zT_NwqNKE-l1 to generate the random
    # data. Currently use this template in `students_generator.js`.

    # Step 1: Create the courses
    math121 = Course("MATH-121", 4, "C-")
    cis115 = Course("CIS-115", 4, "C-")
    cis121 = Course("CIS-121", 4, "C-")
    cis122 = Course("CIS-122", 4, "C-")
    cis223 = Course("CIS-223", 4, "C-")
    cis224 = Course("CIS-224", 4, "C-")

    # Step 2: Create a course sequence. All this is doing is hooking each
    # Course up to one another
    courses = [math121, cis115, cis121, cis122, cis223, cis224]
    Course.create_course_sequence(courses)
    cis121.add_prereq(math121)

    # Step 3: Construct a list of students. This is currently loaded in
    # from the students2.json file, which is generated by student_generator.py
    # file. It will soon be able to be parameterized to simulate random data
    students = utils.get_list_of_students("students2.json", courses)

    # Step 4: Populate each course with their respective class sizes.
    Course.update_course_sizes(students, courses)

    # Print the current class sizes
    print("{} course size: {}".format(cis115.course_name, cis115.class_size))
    print("{} course size: {}".format(cis121.course_name, cis121.class_size))
    print("{} course size: {}".format(cis122.course_name, cis122.class_size))
    print("{} course size: {}".format(cis223.course_name, cis223.class_size))
    print("{} course size: {}".format(cis224.course_name, cis224.class_size))

    # cis121students = calculateNumberInCIS121(students, number incoming)


if __name__ == "__main__":
    main()
