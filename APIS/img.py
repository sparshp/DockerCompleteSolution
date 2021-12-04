import subprocess

def img_serv(subser,mydata):
    if subser == "pull":
        img_name = mydata.getvalue("img_name")
        print(subprocess.getoutput("sudo docker pull "+img_name))
    
    elif subser == "push":
        print("Connecting with dockerhub.....")
        uname = mydata.getvalue("uname")
        passwd = mydata.getvalue("passwd")
        print(subprocess.getoutput("sudo docker login --username "+uname+" --password "+passwd))
        print()
        print("Taging....")
        ver = mydata.getvalue("ver")
        img_name = mydata.getvalue("img_name")
        print(subprocess.getoutput("sudo docker tag "+ver+" "+uname+"/"+img_name))
        print()
        print("pushing the image....")
        print(subprocess.getoutput("sudo docker push "+uname+"/"+img_name))
        
    elif subser == "list":
        print(subprocess.getoutput("sudo docker images"))
        
    elif subser == "rm_img_by_id":
        img_id = mydata.getvalue("img_id")
        print(subprocess.getoutput("sudo docker rmi "+img_id+""))
        
    elif subser == "img_hist":
        img_id = mydata.getvalue("img_id")
        print(subprocess.getoutput("sudo docker image history "+img_id))
    
    elif subser == "img_inspect":
        img_id = mydata.getvalue("img_id")
        print(subprocess.getoutput("sudo docker image inspect "+img_id))
        
                    