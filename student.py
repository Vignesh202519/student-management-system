class Classroom:
    students=[]

    def __init__(self,name,std,rollno):
        self.name=name
        self.std=std
        self.rollno=rollno
        Classroom.students.append(self)

    #for display
    @classmethod
    def display(cls):
        for i in cls.students:
            print(i.name)

    #for delete
    @classmethod
    def delete(cls,std):
        cls.students.remove(std)
        print(std.name,"is removed from the classroom")
        del std

    #for search
    @classmethod
    def search(cls,rno):
        for i in cls.students:
            if i.rollno==rno:
                print(f"Roll no{rno} belongs to {i.name}")
                break
            else:
                print("Student with the given roll number not found")
                break

std1=Classroom("Ram",9,25)
std2=Classroom("Ravi",10,27)
Classroom.display()

Classroom.delete(std1)
Classroom.display()

Classroom.search(27)
Classroom.display()


