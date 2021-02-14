#landport

height = int(input('enter height'))
width = int(input('enter width'))

if height <0 or width <0:
    print("negative value")
    exit(0)
    #return // if funcn
    
if height > width :
    print("portrait")
else:
    print("landscape")