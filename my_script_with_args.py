#!/usr/bin/python3
import jenkins
import pprint
import datetime
import sys
#print('arguments are  ', str(sys.argv))
if len(sys.argv) != 3:
    print("""\Some argument is missed, please check...
    Usage: ./<Script_name> <Job_name> <Build_num>
    """)
    sys.exit(1)
job_name = sys.argv[1]
build_num = sys.argv[2]
server = jenkins.Jenkins('http://<jenkins_host>:<jenkins_port>', username='<jenkins_user>', password='<jenkins_password>')
info = server.get_build_info(job_name, int(build_num))
#pprint.pprint(info)
job_actions = info['actions']
job_started_by = job_actions[0]['causes'][0]['userName']
artf_num = len(info['artifacts'])
artf_name = info['artifacts']
dur = info['duration']
dur_in_formatt = datetime.timedelta(milliseconds=dur)
result = info['result']

## print output
print("Job : " +str(job_name))
print("     Build number :" + str(build_num) + "    started by:   " + str(job_started_by))
print("     Build status:    " + str(result))
print("     Build duration :   " + str(dur_in_formatt))
print("     Artifacts number is  " + str(artf_num) + " : ")
for i in artf_name:
    print("          -      " + i['fileName'])
