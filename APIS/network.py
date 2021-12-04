import subprocess

def net_serv(subser,mydata):
    if subser == "ls":
        print(subprocess.getoutput("sudo docker network ls"))
        
    elif subser =="create":
        subnet = mydata.getvalue("subnet")
        net_name = mydata.getvalue("net_name")
        print(subprocess.getoutput("sudo docker network create --subnet="+subnet+" "+net_name))
    
    elif subser == "deploy_with_static":
        ip = mydata.getvalue("ip")
        net_name = mydata.getvalue("net_name")
        in_port = mydata.getvalue("in_port")
        out_port = mydata.getvalue("out_port")
        cont_name = mydata.getvalue("cont_name")
        img_name_with_tag = mydata.getvalue("img_name_with_tag")
        print(subprocess.getoutput("sudo docker run -dit --net "+net_name+" --ip "+ip+" -p "+out_port+":"+in_port+" --name "+cont_name+" "+img_name_with_tag))
    
    elif subser == "cap_ip":
        cont_name = mydata.getvalue("cont_name")
        print(subprocess.getoutput("docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}'"+cont_name))