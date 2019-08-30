classlist = []
fin = ['FINISH', 'finish', 'Finish']
def classloop():
  classinput = input("Enter your class name. Enter 'Finish' when all classes have been entered. ")
  if classinput in fin:
      print(*classlist, sep="\n")
  else:
      classlist.append(classinput)
      print(*classlist, sep="\n")
      classloop()
classloop()
