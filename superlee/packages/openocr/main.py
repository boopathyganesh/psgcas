from ocr import *

name=input("Enter the Student Name:")
names=name.split()
cert_name=input(f"{name}, Please Enter the Document Name of Your Marksheet:")
cropper(cert_name)
scan('namefield.jpg')
for name in names:
    sts = txtchecker(name)
#print(sts)
if sts in names:
    scan('board.jpg')
    sts = txtchecker('tamilnadu')
    if sts == 'tamilnadu':
        print('Certificate is identified as TamilNadu State Board Certificate')
        sslc = ['secondary', 'school', 'leaving', 'certificate']
        hsc= ['higher','secondary','certificate']
        for key in sslc:
            sts = txtchecker(key)
            print("Certificate Verifying . . . . . ")
            if sts in key:
                print("Certificate is Secondary School Leaving Certificate")
                scan('marks.jpg')
                marks = numcheck2()
                print(marks)
                if len(marks) != 0:
                    total = sum(marks)
                    percentage = total / 5
                    print(f"Total Marks:{total}\n Percentage:{percentage}%")
                    break
                else:
                    print('mark not found')
                    break

            else:
                print("Certificate is Unrecognizable")
    else:
        print("ERROR 404")
else:
    print("ERROR 404")