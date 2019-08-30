classlist = []
fin = ['FINISH', 'finish', 'Finish']
def classloop():
  classinput = input("Enter your class name. Enter 'Finish' when all classes have been entered. ")
  if classinput in fin: #close loop by typing 'Finish'
      print(*classlist, sep="\n") #breaks list into individual lines
  else:
      classlist.append(classinput) #Add class to list
      print(*classlist, sep="\n") #breaks list into individual lines
      classloop()
classloop()
