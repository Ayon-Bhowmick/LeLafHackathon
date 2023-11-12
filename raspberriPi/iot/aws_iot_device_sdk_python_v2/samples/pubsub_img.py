import base64

class ImgDataService():
    def getImg():
        data = ''
        # with open("hua.jpg","rb") as f:
        #     data = f.read()
        # print(base64.b64encode(data))
        print("BETE")

    currImg = "None"

    def getImg():
        return currImg

    def setInput(input):
        currImg = input   

    awsresp = 'None'
    def getresp():
        return awsresp 

    def setresp(input):
        awsresp = input
    
