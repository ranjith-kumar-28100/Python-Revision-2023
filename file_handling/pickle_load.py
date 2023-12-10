import pickle

f = open("new_file.dat","rb")
st1 = pickle.load(f)
st1.display()
f.close()