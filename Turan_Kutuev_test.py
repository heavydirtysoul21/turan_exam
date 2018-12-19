class Student:
    number=''
    name=""
    last_name=""
    favorite_foods=[]
def print_student_ffoods(self):
    print("Student number: ",self.number,'\n')
    print("name: ",self.name,'\n')
    print("last name: ",self.last_name,"\n")
    print("favorite foods: ",self.favorite_foods,"\n","\n")
Student1=Student()
Student2=Student()
Student3=Student()
Student4=Student()
Student5=Student()

Student1.number=1
Student1.name="Bekbolot"
Student1.last_name="Akylbek uulu"
Student1.favorite_foods=["Honey","Manty","Waverma"]

Student2.number=2
Student2.name="Jarkynai"
Student2.last_name="Maratova"
Student2.favorite_foods=["Fat","Ice cream","Water"]

Student3.number=3
Student3.name="Adakhan"
Student3.last_name="Azizbaev"
Student3.favorite_foods=["Fish","Samsa","Plov"]

Student4.number=4
Student4.name="Bermet"
Student4.last_name="Ismailova"
Student4.favorite_foods=["Lagman","Chocolates","Pancakes"]

Student5.number=5
Student5.name="Daniyar"
Student5.last_name="Zholmatov"
Student5.favorite_foods=["Plov","Samsa","Oromo"]

print_student_ffoods(Student1)
print_student_ffoods(Student2)
print_student_ffoods(Student3)
print_student_ffoods(Student4)
print_student_ffoods(Student5)

Dictionary={}
Dictionary[Student1.name]=Student1.favorite_foods
Dictionary[Student2.name]=Student2.favorite_foods
Dictionary[Student3.name]=Student3.favorite_foods
Dictionary[Student4.name]=Student4.favorite_foods
Dictionary[Student5.name]=Student5.favorite_foods

print(Dictionary)

