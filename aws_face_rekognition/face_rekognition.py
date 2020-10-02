import boto3
import base64
import json
import os

rekognition_client = boto3.client('rekognition')

file = open('images/male.jpg','rb').read()

response = rekognition_client.detect_faces(
    Image={
        "Bytes":file
    },
    Attributes=['ALL']
)

#age group and gender
for face in response['FaceDetails']:
    print('The detected face is between ' +str(face['AgeRange']['Low']) + 'and ' + str(face['AgeRange']['High']) + ' years old.')
    print('The detected face is of ' + str(face['Gender']['Value'] + '.'))
    

#To see if the face has sunglass   
Sunglasses = str(face['Sunglasses']['Value'])

if Sunglasses == "True":
    print("The detected face is wearing a sunglass.")
else:
    print("The detected face is not wearing a sunglass.")


#To see if the face is smiling
Smile = str(face['Smile']['Value'])

if Smile == "True":
    print('The detected face is Smiling.')
else:
    print('The detected face is not Smiling.')

#If the detected face is Male Check if he has beard and mustache
Gender = str(face['Gender']['Value'])
if Gender == "Male":
    Beard = str(face['Beard']['Value'])
    Mustache = str(face['Mustache']['Value'])

    if Beard == "True":
        print('The detected face has Beard.')
    else:
        print('The detected face doesnot have Beard.')


    if Mustache == "True":
        print('The detected face has Mustache.')
    else:
        print('The detected face doesnot have Mustache.')

#for emotion in face
emotion_confidence = 0
emotion_type='None'
for emotion in face['Emotions']:
    if emotion['Confidence'] >= emotion_confidence:
        emotion_confidence = emotion['Confidence']
        emotion_type = emotion['Type']
print ("The detected face is {} with {}% confidence.".format(emotion_type, emotion_confidence)) 
        
#to view all the face emotion types with confidence

# 	# emotions
# for emotion in face['Emotions']:
        
# 	print ("  {Type} : {Confidence}%".format(**emotion))
	

#to view all available attributes
# print('Here are the other attributes: ')
# print(json.dumps(face, indent = 4, sort_keys =True))

#saving the facial features in json file
with open('image_info.json', 'w') as outfile:
    json.dump(face, outfile, indent= 4, sort_keys=True)


