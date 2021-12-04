import subprocess

def img_serv(subser,mydata):
    if subser == "ls":
        print(subprocess.getoutput("sudo docker ps"))
    
    elif subser == "inspect_by_id":
        cont_id = mydata.getvalue("cont_id")
        print(subprocess.getoutput("sudo docker container inspect "+cont_id))
    
    elif subser == "inspect_by_name":
        cont_name = mydata.getvalue("cont_name")
        print(subprocess.getoutput("sudo docker container inspect "+cont_name))
        
    elif subser == "deploy":
        in_port=mydata.getvalue("in_port")
        out_port=mydata.getvalue("out_port")
        img_name_with_tag=mydata.getvalue("img_name_with_tag")
        cont_name = mydata.getvalue("cont_name")
        print(subprocess.getoutput("sudo docker run -dit --name "+cont_name+" -p "+out_port+":"+in_port+" "+img_name_with_tag))
    
    elif subser == "stop":
        cont_name = mydata.getvalue("cont_name")
        print(subprocess.getoutput("sudo docker container stop "+cont_name))
    
    elif subser == "start":
        cont_name = mydata.getvalue("cont_name")
        print(subprocess.getoutput("sudo docker container start "+cont_name))
    
    elif subser == "log":
        cont_name = mydata.getvalue("cont_name")
        print(subprocess.getoutput("sudo docker container logs --tail 100 "+cont_name))          