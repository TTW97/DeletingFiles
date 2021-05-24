

import os
import shutil
import time
path=input("Enter path: ")
days=0
seconds=time.time()-(days*24*60*60)
if (os.path.exists(path)):
    for root,dirs,files in os.walk(path,topdown=True):
        for name in files:
            path=os.path.join(root,name)
            c_time=os.stat(path).st_c_time
            if (seconds>=c_time):
                os.remove(path)
                print("\n Deleted the path" + path + "successfully")
        for name in dirs:
            path = os.path.join(root, name)
            c_time = os.stat(path).st_c_time

            if (seconds >= c_time):
                shutil.rmtree(path)
                print("\n Deleted the path " + path + " successfully")
else:
    print("\n Path not found")