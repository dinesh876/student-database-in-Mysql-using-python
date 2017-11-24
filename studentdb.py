import getpass
import mysql.connector
import sys
class Student:
    con=''
    def __init__(self,user,password):
        self.user=user
        self.password=password
    def validate(self):
        if self.user=='admin' and self.password=='admin':
            Student.connect()
            Student.mainMenu()
        else:
            print("Access is denied.please try again!")
            sys.exit()
    def addStudent(self,batchno,Name,Depart_name,contact_phone,contact_email):
        cur=Student.con.cursor()
        str="insert into student values('%d','%s','%s','%d','%s')"
        args=(batchno,Name,Depart_name,contact_phone,contact_email)
        cur.execute(str % args)
        Student.con.commit()
        print("Successfully added...")
    def updateStudent(self,batchno):
        cur=Student.con.cursor()
        print("{:-^30}".format('UPDATE DETAILS'))
        print("{:<10}".format("d -DEPARTMENT NAME"))
        print("{:<10}".format("n -NAME"))
        print("{:<10}".format("p -CONTACT_PHONE"))
        print("{:<10}".format("e -CONTACT_EMAIL"))
        print("{:<10}".format("x -EXIT"))
        print("{:-^30}".format(''))
        while True:
            opt=input('Which information you want update?')
            if opt=='d':
                depart_name=input('Enter the department name: ')
                query="update student set Deptname='%s' where Regno='%d'"
                args=(depart_name,batchno)
                cur.execute(query % args)
                Student.con.commit()
                print('successfully updated')
            elif opt=='n':
                name=input('Enter the name: ')
                query="update student set name='%s' where Regno='%d'"
                args=(name,batchno)
                cur.execute(query % args)
                Student.con.commit()
                print('successfully updated')
            elif opt=='p':
                phone=int(input('Enter the contact phone: '))
                query="update student set contact_phone='%d' where Regno='%d'"
                args=(phone,batchno)
                cur.execute(query % args)
                Student.con.commit()
                print('successfully updated')
            elif opt=='e':
                email=input('Enter the contact email: ')
                query="update student set contact_phone='%d' where Regno='%d'"
                args=(email,batchno)
                cur.execute(query % args)
                Student.con.commit()
                print('successfully updated')
            else:
                Student.mainMenu()
                break
    def studentDetails(self,batchno):
        cur=Student.con.cursor()
        query="select * from student where Regno='%d'"
        cur.execute(query % (batchno))
        row=cur.fetchone()
        while row is not None:
            reg=row[0]
            name=row[1]
            depart_name=row[2]
            phone=row[3]
            email=row[4]
            row=cur.fetchone()
        print("{:-^40}".format("STUDENT DETAILS"))
        print("{:20}".format("REGISTER NUMBER: "),reg)
        print("{:20}".format("STUDENT NAME: "),name)
        print("{:20}".format("DEPARTMENT NAME: "),depart_name)
        print("{:20}".format("CONTACT PHONE: "),phone)
        print("{:20}".format("CONTACT EMAIL:"),email)
        print("{:-^40}".format(''))
    def delete(self,batchno):
        cur=Student.con.cursor()
        query="delete from student where Regno='%d'"
        cur.execute(query % (batchno))
        Student.con.commit()
        print("Deleted successfully")
    @staticmethod
    def connect():
        Student.con=mysql.connector.connect(host='localhost',database='mysql',user='root',password='password')
        if Student.con.is_connected():
            print('connected to mysql database')
    @staticmethod
    def mainMenu():
        print("{:=^30}".format("MAIN MENU"))
        print("{:^30}".format("A - Add new student"))
        print("{:^30}".format("D - Student details"))
        print("{:^20}".format("U - Update"))
        print("{:^30}".format("DEL -delete details"))
        print("{:^17}".format("E -Exit"))
        print("{:=^30}".format(''))
        print()


if __name__=="__main__":
   username=input("Enter the username: ")
   Password=getpass.getpass(prompt="password:",stream=None)
   admin=Student(username,Password)
   admin.validate()
   while(True):
       option=input('Enter the option: ')
       if option=='E' or option=='e':
           sys.exit()
       elif option=='A' or option=='a':
           print("{:-^40}".format("FORM"))
           batchno=int(input("Enter the regno: "))
           Name=input("Enter the name: ")
           Depart_name=input("Enter the Departmentname: ")
           contact_phone=int(input("Enter the contact number: "))
           contact_email=input("Enter the Email id: ")
           print("{:-^40}".format(''))
           admin.addStudent(batchno,Name,Depart_name,contact_phone,contact_email)
       elif option=='U' or option=='u':
           batchno=int(input('Enter the batchno: '))
           admin.updateStudent(batchno)
       elif option=='D' or option=='d':
           batchno=int(input('Enter the batchno: '))
           admin.studentDetails(batchno)
       elif option=='DEL' or option=='del':
           batchno=int(input('Enter the batchno: '))
           admin.delete(batchno)
        
