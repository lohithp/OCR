# importing XML file from the OCR API created by vignesh
from PIL import Image
def ocr(path,X,Y,W,H):
    #image = Image.open(path).convert('RGB')
    import requests

    url = "http://10.63.33.120:9987/getTextsXML"

    payload = {"screen":open(path,'rb')}
    #payload = {"screen":open("C:\\Users\\LPashupathi\\Desktop\\original.jpg",'rb')}
    response = requests.request("POST", url, files=payload)

    print(response.text)
    with open('OCR.xml', 'wb') as file:
        file.write(response.content)
    # Parsing the XML file
    import xml.etree.ElementTree as ET
    tree = ET.parse('OCR.xml')
    list = []
    values = []
    inpb = []
    texts = []
    root = tree.getroot()
    # for child in root:
#   print(child.tag, child.attrib)
# [elem.tag for elem in root.iter()]
# print(ET.tostring(root, encoding='utf8').decode('utf8'))
    for item in root.iter('text'):
      list.append(item.attrib)
    #print(list)
    for i in list:
       # for j in list[1]:
       # print(list[0])"""
       for k, v in i.items():
          values.append(v)
        # print()
#print(values)
# How many elements each
# list should have
    n = 7
# using list comprehension
    final = [values[i * n:(i + 1) * n] for i in range((len(values) + n - 1) // n)]
    #printing final list
    print (final)
    for i in final:
        h = float(i[5]) - float(i[6])
        w = float(i[2]) - float(i[3])
        text = i[0]
        x = float(i[1])
        y = float (i[3])
        inpb.append([x,y,h,w])
        texts.append(text)
    print(texts)
    print(inpb)
    InterUnion = []
# declaring a and b this should be changed according to the user input and AI model
#a = [float(x) for x in input().split()]
    inpu = 4
#inpa =[695.0, 462.0, 94.0, 26.0]
#a = [695.0, 462.0, 94.0 + inpa[0], 26.0 +inpa[1]]
#print(a)
    # inpa = [float(x) for x in input("enter the coordinates in the order X,Y,W,H: ").split(",")]
    # for i in inpa:
    #     a = [inpa[0], inpa[1], inpa[2] + inpa[0], inpa[3] +inpa[1]]
    # print(a)
    X1=int(X)
    Y1=int(Y)
    W1=int(W)
    H1=int(H)
    a=[X1,Y1,X1+W1,Y1+H1]
#a = [float(x) for x in input("enter the coordinates in the order X,Y,H,W: ").split()]
#print(a)
#a = [700.5, 680.0, 100.0, 30.0]
    b =[]
#inb = inpb
#print(inpb)
#b =[]
    for i in inpb:
        m = [i[0], i[1] , i[2] + i[0] , i[3] + i[1]]
        b.append(m)
    print(b)
    M = []
    def get_iou(a, b, e=1e-5):
        # COORDINATES OF THE INTERSECTION BOX
        x1 = max(a[0], b[0])
        y1 = max(a[1], b[1])
        x2 = min(a[2], b[2])
        y2 = min(a[3], b[3])

        width = abs(x2 - x1)
        height = abs(y2 - y1)
        if (width<0) or (height <0):
            return 0.0
        area_overlap = width * height
        area_a = (a[2] - a[0]) * (a[3] - a[1])
        area_b = (b[2] - b[0]) * (b[3] - b[1])
        area_combined = area_a + area_b - area_overlap
        #M = []
        iou = area_overlap / (area_combined+e)
        #M.append(iou)
        if iou < 0 or iou > 1:
            iou = 0
        M.append(iou)
        print("IOU : " , iou)
        return iou
    for i in range(len(b)):
        #print("coordinates :", a,b[i])
        get_iou(a, b[i] , e=1e-5)
    LIOU = max(M)
    print(LIOU)
    pos = M.index(LIOU)
    coo = a,b[pos]

    print("coordinates with max IOU is : ", coo)

    print("corresponding IOU is : ", LIOU)
    ind = b.index(b[pos])
#print(ind)
    tex = texts[ind]
    print("OCR : " , tex)
    #str = "OCR TEXT : %s " % (tex)
    # str=str(coo)+","+str(LIOU)+","+tex
    #str = str(tex)
    return coo,LIOU,tex
    #return tex
    #return tex
    #298.0, 263return(coo).0, 320.0, 334.0



