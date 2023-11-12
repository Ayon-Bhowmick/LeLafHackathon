import base64

# Define global variables
currImg = "None"
awsresp = 'None'

class ImgDataService():
    def getImg():
        return currImg

    def setImg(input):
        global currImg
        currImg = input

    def getresp():
        return awsresp

    def setresp(input):
        global awsresp
        awsresp = input
