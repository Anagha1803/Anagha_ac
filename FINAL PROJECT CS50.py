





studentnamelist=[]
english=[]
maths=[]
englishaveragemarks=[]
ans="yes"#control variable
while ans=="yes":
   choice=""
   print("STUDENT MANAGEMENT SYSTEM")
   print("1.Add student details")
   print("2.Display details of all students")
   print("3.Delete all the data")
   print("4.Display all the names of the children")
   print("5.Calculating the percentage")
   print("6.Checking if the student is part of the class")
   print("7.Average of english")
   print("8.For below,equal or above average")
   print("9.Average of maths")
   choice= input("Enter you choice")
   choice=int(choice)
   if choice==1:
      print("Add student details")
      mname=input("Enter the name of the student")
      studentnamelist.append(mname)
      menglish=input("Enter the english marks")
      menglish=int(menglish)
      english.append(menglish)
      mmaths=input("Enter the maths marks")
      mmaths=int(mmaths)
      maths.append(mmaths)
   elif choice==2:
      print("Display student details")
      print("name of students",studentnamelist)
      print("english mark list",english)
      print("maths mark list",maths)
   elif choice==3:
        print("Deleting all details")
        studentnamelist.clear()
        english.clear()
        maths.clear()
   elif choice==4:
      print("Display names of all the students")
      c=0
      numberofstudents=len(studentnamelist)
      while c<numberofstudents:
         print(studentnamelist[c])
         c=c+1
    
   elif choice==5: 
     print("Calculating the percentage")
     c=0
     numberofstudents=len(studentnamelist)
     while c<numberofstudents:
       total=0
       total=english[c]+maths[c]
       per=(total*100)/200
       percentage.append(per)
       c=c+1
       print(per)
   elif choice==6:
      name=input("Enter the name of the student to search")
      if name in studentnamelist:
         print(name,"is a student of the class")
      else:
         print(name,"is not a student of the class")
   elif choice==7:
      studentname=["aaa","bbb","ccc","ddd","eee"]
      english=[11,22,33,44,55]
      avg=0
      total=0
      for i in range(5):
       total=total+english[i]
       avg=total/5
       print("average marks in english is",avg)
   elif choice==8:
      aboveavg=[]
      belowavg=[]
      for i in range(5):
         if english[i]>=avg:
          aboveavg.append(studentname[i])
         else:
          belowavg.append(studentname[i])

         print("all students who got above or equal to average are")
         print(aboveavg)
         print("All the students that got below average")
         print(belowavg)

   elif choice==9:
      studentname=["aaa","bbb","ccc","ddd","eee"]
      maths=[11,22,33,44,55]
      avg=0
      total=0
      for i in range(5):
       total=total+english[i]
       avg=total/5
       print("average marks in maths is",avg) 

      
      else :
       print("Wrong choice")
   ans=input("Do you want to repeat the menu")
   
   
      

