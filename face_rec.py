'''import sys
import cv2 
#import face_recognition
import pickle
name=input("enter name:")
ref_id=input("enter id:")
try:
    f=open("ref_name.pkl","rb")

    ref_dictt=pickle.load(f)
    f.close()
except:
    ref_dictt={}
ref_dictt[ref_id]=name


f=open("ref_name.pkl","wb")
pickle.dump(ref_dictt,f)
f.close()

try:
    f=open("ref_embed.pkl","rb")

    embed_dictt=pickle.load(f)
    f.close()
except:
    embed_dictt={}'''

''''
a=input(int())
b=input(int())
print(a)
print(b)


'''





name=input("what si ")
print('hi'+name)