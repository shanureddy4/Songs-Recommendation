import io
import os
from google.cloud import vision
from google.cloud.vision_v1 import types
import numpy as np
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vision.json'

import cv2 as cv
from PIL import Image
camera = cv.VideoCapture(0)
for i in range(12):
    return_val , image = camera.read()
    if i==11:
       cv.imwrite('test'+'.jpg',image)
del(camera)
img = Image.open('test.jpg')
img.show()


client = vision.ImageAnnotatorClient()


filename = 'test.jpg'



with io.open(filename,'rb') as img:
    content = img.read()

    image = types.Image(content=content)

    labelresponse = client.label_detection(image=image)
    faceresponse = client.face_detection(image=image)
    labels = labelresponse.label_annotations





print("\nThis image contains : ")

for label in labels:
    print(label.description)




faces=faceresponse.face_annotations

#there might be one or many faces , so in case :::: emotions ,,,, anger ,,,, sorrow ,,,,,joy ,,, surprise



print('\n\n::::Resultant Emotion::::::\n\n')

print('Anger','  Sorrow','  Joy','  Surprise')
for face in faces:
    print(face.anger_likelihood,'\t',face.sorrow_likelihood,'\t ',face.joy_likelihood,'\t',face.surprise_likelihood)





#'UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY'

#  0              1              2           3          4          5





#import threading as td




#scale them to energy and valence /////


#energy = user input
#valence = arousal value // happines ?????
#now we set valence accordingly since my assumption is happiness = sigmoid(k.valence) where k = 0 to 1  1/(1+exp(-x))
if face.joy_likelihood>face.sorrow_likelihood:
    valence = 1/(1+np.exp(-face.joy_likelihood))
elif face.sorrow_likelihood>face.joy_likelihood:
    valence = 1/(1+np.exp(face.sorrow_likelihood))
else:
    valence = 1/(1+np.exp(0))
    
#valence = [0 -----sadness  ----- < 0.5 = unknown  ----happiness-----1.00]


# In[26]:


valence#now this looks like valence value ????? sad 


# In[63]:


#time for energy to be calculated 


# In[64]:


#engage user to take get energy values by asking a question .
#question : Hey , Will you dance with me ??
import time
print('\n\n')
question = 'Hey , will you dance with me ? ?'
#engage user
for letter in question:
    print(letter,end='')
    time.sleep(0.05)


# In[105]:


time.sleep(1)
q1 ='Sorry to ask you out of nowhere ....\n .\n .\nI wont mind if you\'d say no  \n:('
opt = ['Kinda ya but ...', 'Hey some other time','NOOOOOOO' ,'Let\'s do that', 'Yaaaayyy']


# In[106]:


for letter in q1:
    print(letter,end='')
    time.sleep(0.03)


# In[107]:


time.sleep(0.2)
print('Here are your options : ')
op =1
for op in range(1,(len(opt))+1):
    print('Press :  \"', op ,'\"for :',opt[op-1])
    time.sleep(0.3)    
    


# In[108]:


a = int(input())
if a>3:
    energy = 1/(1+np.exp(-a))
else:
    energy  =1/(1+np.exp(a))
    


# In[109]:


#valence and energy found
time.sleep(0.5)
print('I\'ll calculate your energy index and happiness .. ...')


# In[110]:


for i in range(3):
    print('.')
    time.sleep(1)


# In[214]:

print('Energy    :  ',energy)
print('Valence   :  ',valence)


# In[215]:


#run this through a database which has no happiness no sadness label
# but neural nets can help this thing up .... just to check our KNN



import pandas as pd
import matplotlib.pyplot as plt

#file name or dataset
filename = 'spotifydata.csv'
#knnalgo(energy,valence,filename)




#def knnalgo(energy,valence,filename):
dist= []
df = pd.read_csv(filename)

db_energy = np.array(df['energy'])
db_valence = np.array(df['valence'])
for i in range(len(db_energy)):
    a  = (db_energy[i]-energy)**2
    b  = (db_valence[i]-valence)**2
    c = np.sqrt(a+b)
    dist.append(c)
        

        
    
    


df.head()


x = np.array(df['track_name'])



dfnew = pd.DataFrame({'song':x,'dist':dist})



dfnew.head()


# In[222]:


sdt=dfnew.sort_values(by=['dist'])


# In[223]:


sdt


# In[224]:
print("###### here are few songs that you can go for  ######")

count = 0
for i in sdt['song']:
    if count>(20):
        break
    else:
        print(i)
        count+=1
        time.sleep(0.5)





