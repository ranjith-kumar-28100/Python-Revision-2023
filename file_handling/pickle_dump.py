import pickle,student

st1 = student.Student(1,"RKG",12)
f = open('new_file.dat','ab')
pickle.dump(st1,f)
f.close()