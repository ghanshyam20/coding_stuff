#json =javascript notation

#json is a syntax for storing and excanging data.
#json is text, written with javascript object  notation.
#python object =-everything in python is object ie, list,tuple,dictionary,set etc 

#python has a built-in package called json,which can be used to  work with json data.


import json


#some example of Json
x='{"name":"John","age":30,"city":"New Work"}'


#parse x:
#json lai load garera python object ma convert gariyo
y=json.loads(x)


print(y["age"])
print(y["name"])
print(y["city"])



#python to json 
#create python object and convert it into json
