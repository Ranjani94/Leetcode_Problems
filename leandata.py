
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# name = 'Jack' -> 'John'



def populate():

    NumberOfCourses = getCourses()
    NumberOfClubs = getClubs()

    studentList = getStudents()  # ['Mary','John', 'Jack']
    studentList[1] = 'Ross'

    SaveToDatabase(studentList)

    print(studentList)
    print(NumberOfClubs)
    print(NumberOfCourses)

    result = []
    dic = {'student-id': []}
    for student in studentList:
        result.append(student.id, student.name, student.numberOfCourses, student.numberOfClubs)
        print(result)
        result = []
        
    return result


    # [1,'Mary', 3, 2]
    # [2, 'Ross', 4, 5]






