from os import path
import json
import sys
import threading
import time
import unittest

def main():
    choice=0
    while(1):
       choice=int(input('For insertion type 1\nFor reading type 2\nFor deleting type 3\nFor exiting type anything other than that:'))
       if choice==1:
           insert()
       elif choice==2:
           filename=input('Enter the file that is needed to be read:')
           if path.exists(filename):
               key=input('Enter the rollno:')
               read(filename,key)
       elif choice==3:
           filename=input('Enter the file that is needed to be deleted:')
           key=input('Enter the rollno:')
           delete(filename,key)
       else:
           return None
    
def insert():
    c=input('Enter the file name along with the path:')
    if path.exists(c):
        classdata=[]
        print('File',c,'already existed')
        rollno=input('Enter student rollno:')
        if len(rollno)>32:
            print('Key value too large..Should be less than 32 characters')
            return False
        name=input('Name:')
        email=input('Email:')
        phno=input('Number:')
        section=input('Section:')
        data = {}
        data[rollno]=[]
        data[rollno].append({'name':name,
                             'email':email,
                             'phno':phno,
                             'section':section
                       })
        size=0
        size=sys.getsizeof(data)
        if size>(32*1024):
            print('Object size is larger than 32Bytes')
            return False
        with open(c,'r') as outfile:
            classdata = json.load(outfile)
        for i in classdata:
            for j in i:
                if j==rollno:
                    print('Key',rollno,' already exits')
                    return False
        classdata.append(data)    
        with open(c,'w') as outfile:
            json.dump(classdata,outfile)
        print('Data has been appended')
        lock = threading.Lock()
        t1 = threading.Thread(target=ttlfunc, args=(lock,c,rollno))
        ttl=input('Do you want to activate TTl-if yes then type y or type n:')
        if ttl=='y':
             lock = threading.Lock()
             t1 = threading.Thread(target=ttlfunc, args=(lock,c,rollno))
             t1.start()
             t1.join()
             return True
        else:
            return True
    else:
        f = open(c, "x")
        print('File',c,'is created')
        classdata=[]
        rollno=input('Enter student rollno:')
        if len(rollno)>32:
            print('Key too large..Should be less than 33 characters')
            return False
        name=input('Name:')
        phno=input('Number:')
        email=input('Email:')
        section=input('Section:')
        data = {}
        data[rollno]=[]
        data[rollno].append({'name':name,
                        'email':email,
                        'phno':phno,
                       'section':section
        })
        size=0
        size=sys.getsizeof(data)
        if not objsize(size):
            print('Object size is larger than 32Bytes')
            return False
        classdata.append(data)
        with open(c, 'w') as outfile:
            json.dump(classdata, outfile)
        print('Data written sucessfully')
        ttl=input('Do you want to activate TTl-if yes then type y or type n:')
        if ttl=='y':
             lock = threading.Lock()
             t1 = threading.Thread(target=ttlfunc, args=(lock,c,rollno))
             t1.start()
             t1.join()
             return True
        else:
            return True
    
def read(filename,key):
    
    if path.exists(filename):
        classdata=[]
        with open(filename,'r') as outfile:
            classdata = json.load(outfile)
            filesize=sys.getsizeof(classdata)
            if filesize>(1024*1024*1024):
                print('File reached max size')
                return False
            flag=0
            for i in classdata:
                if flag==1:
                    break
                for j in i:
                    if j==key:
                        print(i)
                        flag=1
                        break
            if flag==0:
                print('Key not found')
                return False
        return True
            
    else:
        print('File does not exist')
        return False
def delete(filename,key):
    if path.exists(filename):
        with open(filename,'r') as outfile:
            classdata = json.load(outfile)
            k=0
            flag=0
            classdata1=[]
            for i in classdata:
                for j in i:
                    if j==key:
                        k=1
                        print('Key has been deleted')
                        flag=1
                if k!=1:
                    classdata1.append(i)
                k=0
            
        if flag==0:
            print('Key not found')
            return False
        with open(filename, 'w') as outfile:
            json.dump(classdata1, outfile)
        return 'Key has been deleted'
    else:
        print('File does not exist')
        return False

        
def ttlfunc(lock,filename,key): 
 
        time1=int(input('Enter the time to live(In seconds):'))
        lock.acquire()
        time.sleep(time1)
        delete(filename,key)
        lock.release()
        return True
def objsize(size):
    if(size<32*1024):
        return True
    else:
        return False
if __name__ == "__main__":
        main()    
        


