#create class for student which include their information of enrollment in school
class student:
    number_student =0 #create data member
    def __init__(self,n,a):# constructor for the class of the student
        self.full_name = n #take the student name
        self.age =a #take the age of the student
    def count(self):#create function to calculate number of student
        self.__class__.number_student += 1
    def detail1(self):#print the student information
        return "Student %s age is %s" %(self.full_name,int(self.age))
class rollno_student(student):#make inheritance of the class 'student'
    def __init__(self,n,a,r):
        student.__init__(self,n,a)#take the previous attribute from class 'student'
        self.rollno=r
    def detail2(self):#print the student information
        return "Student %s age is %s and roll no  is %s" % (self.full_name,int(self.age),int(self.rollno))
class grade_student(rollno_student):#make inheritance of the class 'rollno_student'
    def __init__(self,n,a,r,g):
        rollno_student.__init__(self,n,a,r)#take the previous attribute from class 'rollno_student'
        self.grade=g
    def detail3(self):#print the student information
        return "Student %s age is %s and roll no is %s and grade is %s" % (self.full_name,int(self.age),int(self.rollno),self.grade)
class midterm:
    def __init__(self,p,q):
        self.name1=p
        self.midterm =q
class final:
    def __init__(self,r):
        self.final =r
class result(midterm,final):#make double inheritance by class midterm and final
    def __init__(self,p,q,r):
        midterm.__init__(self,p,q)#use the super call
        final. __init__(self,r)
    def detail4(self):#print the student information
        return "student %s midterm mark is %s and final mark is %s" %(self.name1,int(self.midterm),int(self.final))


student1= student("Moqbull",24)#input for first class
print student1.detail1()
student1.count()
student2 = rollno_student("Hossen",24,20)#input for second class
print student2.detail2()
student2.count()
student3 = grade_student("Ponir",24,20,"A")#input for third class
print student3.detail3()
student3.count()
print "the number of student",student3.__class__.number_student
student4 = result("Pinky",85,88)#input for double inheritance
print student4.detail4()




