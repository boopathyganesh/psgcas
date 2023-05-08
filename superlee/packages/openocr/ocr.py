import easyocr
import cv2
import re

# specify languages and other configs
reader = easyocr.Reader(['en','ta'],gpu=True)
def scan(file):
    image = cv2.imread(file) # read image
    result = reader.readtext(image,detail=0,output_format=list)
    with open('text.txt', 'w', encoding="utf-8") as fp:
        for item in reader.readtext(image,detail=0,output_format=list):
            # write each item on a new line
            fp.write("%s\n" % item)
        #print('Done')
    fp.close()
    return result

def check(string):
    regex = '^[0-9]+$'
    if len(string) == 4:
        if string[0] == 'O' or string[0] == 'o' or string[0] == '0':
            string=string[1:]
        if re.search(regex, string):
            if (int(string) < 100 and int(string) > 9):  #2 and 3 digit checking
                string=int(string)
    return string

def numcheck2():
    regex = '^[0-9]+$'
    marks=[]
    i=0
    with open('text.txt','r',encoding="utf-8") as f:
        lines = f.readlines()

        for string in lines:
            if len(string) == 4:
                if string[0] == 'O' or string[0] == 'o' or string[0] == '0':
                    string = string[1:]
                if re.search(regex, string):
                    if (int(string) <= 100 and int(string) > 0):  # 2 and 3 digit checking
                        marks.append(int(string))
    f.close()
    return marks
def numcheck3():
    regex = '^[0-9]+$'
    marks=[]
    i=0
    with open('text.txt','r',encoding="utf-8") as f:
        lines = f.readlines()

        for string in lines:
            if len(string) == 4:
                if string[0] == 'O' or string[0] == 'o' or string[0] == '0':
                    string = string[1:]
                if re.search(regex, string):
                    if (int(string) <= 200 and int(string) > 0):  # 2 and 3 digit checking
                        marks.append(int(string))
    f.close()
    return marks

def txtchecker(string):
    #with open('text.txt', 'r',encoding='utf-8') as fp:
        file1 = open("text.txt", "r",encoding='utf-8')

        # setting flag and index to 0
        flag = 0
        index = 0
        # Loop through the file line by line
        for line in file1:
            index +=1
            if string.casefold() in line.casefold():
                flag = 1
                break

                # checking condition for string found or not
        if flag == 0:
            return "404"
        else:
            #print(string)
            return string



def cropper(img):
    global m, n
    img=cv2.imread(img)
    dim = img.shape
    print(dim)
    print(f"Your Marksheet file has {dim[1]}px X {dim[0]}px dimension")
    n=dim[0]/2339
    m=dim[1]/1655
    cropped_image=img[int(n*100):int(n*550), int(m*80):int(m*1600)]
    #cv2.imshow("board",cropped_image)
    cv2.imwrite("board.jpg", cropped_image)
    # Cropping NAMEFEILD
    cropped_image=img[int(n*550):int(n*765),int(m*100):int(m*1600)]
    #cv2.imshow('name',cropped_image)
    cv2.imwrite("namefield.jpg", cropped_image)
    # Cropping SUBJECTS
    cropped_image=img[int(n*850):int(n*1600),int(m*100):int(m*720)]
    #cv2.imshow('subject',cropped_image)
    cv2.imwrite("subjects.jpg", cropped_image)
    cropped_image = img[int(n * 850):int(n * 1600), int(m * 980):int(m * 1500)]
    #cv2.imshow('mark_algo', cropped_image)
    cv2.imwrite("marks.jpg", cropped_image)


if __name__ == '__main__':
    cropper('test2.jpg')
    scan('board.jpg')
    sts=txtchecker('tamilnadu')
    if sts == 'tamilnadu':
        print('Certificate is identified as TamilNadu State Board Certificate')
        sslc=['secondary','school','leaving' ,'certificate']
        for key in sslc:
            sts=txtchecker(key)
            print("Certificate Verifying . . . . . ")
            if sts in key:
                print("Certificate is Secondary School Leaving Certificate")
                scan('marks.jpg')
                marks = numcheck2()
                print(marks)
                if len(marks) != 0:
                    total = sum(marks)
                    #sts=txtchecker()
                    percentage = total / 5
                    print(f"\nTotal Marks:{total}\nPercentage:{percentage}%")
                    break
                else:
                    print('mark not found')
                    break
            else:
                print("Certificate is Unrecognizable")
    else:
        print("ERROR 404")