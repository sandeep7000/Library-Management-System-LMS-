import sqlite3
con=sqlite3.connect("lms.db")

def main_menu():
     print(" --> Enter 1 to \'ADD Book\' ")
     print(" --> Enter 2 to \'Issue Book\' ")
     print(" --> Enter 3 to \'Return Book\' ")
     print(" --> Enter 4 to \'Display list of all Books\' ")
     print(" --> Enter 5 to \'Display list of issue data\' ")
     print(" --> Enter 6 to \'Update Book Details\' ")
     print(" --> Enter 7 to \'Update Issue Details\' ")
     print(" --> Enter 8 to \'EXIT\' ")
     ans=int(input("Your response ="))
     if(ans==1):
           add_book()
     elif(ans==2):
           issue_book()
     elif(ans==3):
           return_book()
     elif(ans==4):
           show_list()
     elif(ans==5):
           show_issue_list()
     elif(ans==6):
           update_book()
     elif(ans==7):
           update_issue()
     elif(ans==8):
           exit()
     else:
           
           print("Please Enter a Valid Input")
           main_menu()

def add_book():
     no=int(input("Book No. ="))
     name=input("NAME =")
     author=input("Author =")
     con=sqlite3.connect("lms.db")
     con.execute('insert into books VALUES(?,?,?)',(no,name,author))
     con.commit()
     con.close()
     print("Data Added Successfully")
     next()

def issue_book():
     no=int(input("Book number ="))
     book_name=input("NAME =")
     name=input("Issued By =")
     phone_no=int(input("Phone number ="))
     issue_date=input("Date of issue =")
     return_date=input("Date of return =")
     con=sqlite3.connect("lms.db")
     con.execute('insert into issue VALUES(?,?,?,?,?,?)',(no,book_name,name,phone_no,issue_date,return_date))
     con.commit()
     con.close()
     print("Data Added Successfully")
     next()

def return_book():
     no=int(input("Book number ="))
     book_name=input("Book name =")
     name=input("Returned By =")
     return_date=input("Date of return =")
     con=sqlite3.connect("lms.db")
     con.execute('insert into return VALUES(?,?,?,?)',(no,book_name,name,return_date))
     con.commit()
     con.close()
     print("Data Added Successfully")
     next()

def show_list():
     con=sqlite3.connect("lms.db")
     data=con.execute(" select * from books " )
     print("")
     print("")
     for n in data:
          print(n[0],"        ",n[1],"          ",n[2])
          print("")
     next()

def show_issue_list():
     con=sqlite3.connect("lms.db")
     data=con.execute(" select * from issue " )
     print("")
     print("")
     for n in data:
          print(n[0],"        ",n[1],"          ",n[2],"        ",n[3],"        ",n[4],"          ",n[5])
          print("")
     next()

def update_book():
      con=sqlite3.connect("lms.db")
      print("--> Enter 1 to Update Book no")
      print("--> Enter 2 to Update Name")
      print("--> Enter 3 to Update Author")
      res=int(input("Your Response ="))
      if(res==1):
                  con=sqlite3.connect("lms.db")
                  name=input("Enter Name of Book whose Book_no. you wanna Update =")
                  no=input("Enter Correct Name =")
                  con.execute('Update books set book_no= ? where book_name= ? ',(no,name))
                  con.commit()
                  con.close()
                  print("Data Updated Successfully")
                  next()
      elif(res==2):
                  con=sqlite3.connect("lms.db")
                  no=input("Enter Book_No of book whose NAME you Wanna change =")
                  name=input("Enter New Name =")
                  con.execute('Update  books set book_name=? where book_no= ?',(name,no))
                  con.commit()
                  con.close()
                  print("Data Updated Successfully")
                  next()
      elif(res==3):
                  con=sqlite3.connect("lms.db")
                  no=input("Enter Book_No of book whose NAME you Wanna change =")
                  author=int(input("Enter New author ="))
                  con.execute('Update books set author=? where book_no=?',(no,author))
                  con.commit()
                  con.close()
                  print("Data Updated Successfully")
                  next()
      else:
                  print("Please Enter a Valid Input")
                  update_book()
def update_issue():
      con=sqlite3.connect("lms.db")
      print("--> Enter 1 to Update Book no")
      print("--> Enter 2 to Update Book Name")
      print("--> Enter 3 to Update issued by")
      print("--> Enter 4 to Update Phone no")
      print("--> Enter 5 to Update Issue date")
      print("--> Enter 6 to Update return date")
      res=int(input("Your Response ="))
      if(res==1):
                  con=sqlite3.connect("lms.db")
                  name=input("Enter Name of Book whose Book_no. you wanna Update =")
                  no=input("Enter Correct number =")
                  con.execute('Update issue set book_no= ? where book_name= ? ',(no,name))
                  con.commit()
                  con.close()
                  print("Data Updated Successfully")
                  next()
      elif(res==2):
                  con=sqlite3.connect("lms.db")
                  no=input("Enter Book_No of book whose NAME you Wanna change =")
                  name=input("Enter New Name =")
                  con.execute('Update issue set book_name=? where book_no= ?',(name,no))
                  con.commit()
                  con.close()
                  print("Data Updated Successfully")
                  next()
      elif(res==3):
                  con=sqlite3.connect("lms.db")
                  no=input("Enter phone No of person whose NAME you Wanna change =")
                  name=input("Enter New Name =")
                  con.execute('Update issue set issued_by=? where phone_no= ?',(name,no))
                  con.commit()
                  con.close()
                  print("Data Updated Successfully")
                  next()
      elif(res==4):
                  con=sqlite3.connect("lms.db")
                  name=input("Enter Name of person whose phone number you Wanna change =")
                  no=input("Enter phone no  =")
                  con.execute('Update issue set phone_no=? where issued_by= ?',(no,name))
                  con.commit()
                  con.close()
                  print("Data Updated Successfully")
                  next()
      elif(res==5):
                  con=sqlite3.connect("lms.db")
                  name=input("Enter Name of book whose issue date you Wanna change =")
                  date=input("Enter new date =")
                  con.execute('Update issue set issue_date=? where book_name= ?',(date,name))
                  con.commit()
                  con.close()
                  print("Data Updated Successfully")
                  next()
      elif(res==6):
                  con=sqlite3.connect("lms.db")
                  name=input("Enter Name of book whose return date you Wanna change =")
                  date=input("Enter new date =")
                  con.execute('Update issue set return_date=? where book_name= ?',(date,name))
                  con.commit()
                  con.close()
                  print("Data Updated Successfully")
                  next()
      else:
                  print("Please Enter a Valid Input")
                  update_issue()

def start():
      print("--->> Enter 1 for MAIN MENU")
      print("--->> Enter 2 to EXIT")
      rs=int(input("Your response ="))
      if(rs==1):
            main_menu()
      elif(rs==2):
            exit()
      else:
            print("Please Enter a Valid Input")
            start()

def next():
     print("Enter 1 for \'Main Menu\'")
     print("Enter 0 to \'EXIT\'")
     res=int(input("Your Response ="))
     if(res==1):
           con=sqlite3.connect("pps.db")
           main_menu()
     elif(res==0):
           exit()
     else:
           print("Please Enter a Valid Input")
           next()
def exit():
      print("")
      print("            \'THANK YOU\'")
start()