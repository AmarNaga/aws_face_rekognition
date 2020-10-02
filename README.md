# aws_face_rekognition
**Pre-requisites**
1. python
2. aws cli

**steps**
1. get aws cli info from aws educate account -> vocareum workbench -> account details
2. Copy paste the info in .aws/credentials in the local machine
3. Run the code

Note: aws cli info needs to get renewed every 1 hour

**About the code**
This is the facial rekognition feature under amazon analytics services provided by the AWS itsself.  
Note that you will need an aws account few credits to run the code effectively.  
It uses the detect_faces method by boto3  
Refer this documentation for more available features by boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html  
This program can rekognize details like age range, gender, sunglasses, smile, moustache and beard (if the face is detected to be Male) and other emotions in the image that is provided in the "file".  
Finally the facial attributes will be saved in image_info.json file in sorted JSON format.  
The commented code can be run to see the full emotion type and confidence of provided image and to view all the available facial attributes provided by boto3's detect_faces.  

**Expected Output**
'''
The detected face is between 31and 47 years old.  
The detected face is of Male.  
The detected face is not wearing a sunglass.  
The detected face is not Smiling.  
The detected face has Beard.  
The detected face has Mustache.  
The detected face is CONFUSED with 65.20594787597656% confidence.  
'''
