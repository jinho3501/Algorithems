word= input()
list1 =["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in list1:
    word = word.replace(i,"#")
print(len(word))
