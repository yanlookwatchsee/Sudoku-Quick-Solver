#!/usr/bin/python
# Author: Yan Li
# Licence: BSD-like licence

import copy
import sys
import time
import argparse

class unit:
    def __init__(self):
        self.ready=False
        self.checkbox=[False]*9
        self.value=0
    def isReady(self):
        return self.ready
    def check(self, num):
        if self.ready:
            return True
        self.checkbox[num-1]=True
    def avalibleValue(self):
        count=9;
        value=0;
        for i in range(0,9):
            if self.checkbox[i]:
                count=count-1
            else:
                value=i;
        if count==1:
            return value+1
        else:
            return 0
    def assign(self, num):
        if self.ready:
            raise Exception('error')
        self.ready=True
        self.value=num
    def canbe(self, num):
        if self.ready:
            return False
        if self.checkbox[num-1]:
            return False
        else:
            return True

COL=0
ROW=1
BLOCK=2

class sudoku:
    def __init__(self, vlist=[]):
        self.matrix=[]
        for i in range(0,81):
            self.matrix.append(unit())
        for elem in vlist:
            self.matrix[elem["pos"]].assign(elem["val"])
    def checkReadyCount(self):
        count=0
        for i in range(0,81):
            if self.matrix[i].isReady():
                count+=1
        return count
    def oneAreaCheck(self, where, pos, num):
        if where==BLOCK:
            block_i=pos/3*3
            block_j=pos%3*3
            i=block_i
            j=block_j
            for i in range(block_i,block_i+3):
                for j in range(block_j, block_j+3):
                    self.matrix[9*i+j].check(num)
            return
        head=0
        tail=0
        step=0
        if where==COL:
            head=pos
            tail=head+72
            step=9
        elif where == ROW:
            head=pos*9
            tail=head+8
            step=1
        else:
            print "error"
            sys.exit(0)
            return
        i=head
        while i<=tail:
            self.matrix[i].check(num)
            i=i+step

    def oneAreaElect(self, where, pos):
        if where==BLOCK:
            block_i=pos/3*3
            block_j=pos%3*3
            i=block_i
            j=block_j
            tmp=-1
            for target in range(1,10):
                haveone=False
                count=0
                for i in range(block_i,block_i+3):
                    for j in range(block_j, block_j+3):
                        k=9*i+j
                        if self.matrix[k].canbe(target):
                            count+=1
                            tmp=k
                        if self.matrix[k].isReady() and self.matrix[k].value==target:
                            haveone=True
                if count==1:
                    self.matrix[tmp].assign(target)
                    return tmp
                if not haveone and count==0:
                    raise Exception
            return -1

        head=0
        tail=0
        step=0
        tmp=-1
        if where==COL:
            head=pos
            tail=head+72
            step=9
        elif where == ROW:
            head=pos*9
            tail=head+8
            step=1
        else:
            print "error"
            return -1
        for target in range(1,10):
            count=0
            haveone=False
            i=head
            while i<=tail:
                if self.matrix[i].canbe(target):
                    count+=1
                    tmp=i
                if self.matrix[i].isReady() and self.matrix[i].value==target:
                    haveone=True
                i=i+step
            if count==1:
                self.matrix[tmp].assign(target)
                return tmp
            if haveone and not count==0:
                raise Exception
            if not haveone and count==0:
                raise Exception
        return -1
    def fullCheckForOneUnit(self, pos):
        if not self.matrix[pos].isReady():
            return
        num=self.matrix[pos].value
        col=pos%9
        self.oneAreaCheck(COL,col,num)
        row=pos/9
        self.oneAreaCheck(ROW,row,num)
        block=row/3*3+col/3
        self.oneAreaCheck(BLOCK,block,num)
    def electOnce(self):
        for i in range(0,9):
            ret=self.oneAreaElect(COL,i)
            if ret>=0:
                return ret
            ret=self.oneAreaElect(ROW,i)
            if ret>=0:
                return ret
            ret=self.oneAreaElect(BLOCK,i)
            if ret>=0:
                return ret
        return -1
    def scanOnce(self):
        for i in range(0,81):
            if not self.matrix[i].isReady() and self.matrix[i].avalibleValue():
                self.matrix[i].assign(self.matrix[i].avalibleValue())
                return i;
        return -1
    def fulldump(self):
        print "full dump!"
        for i in range(0,81):
            if self.matrix[i].isReady():
                continue
            print i,":",
            for j in range(0,9):
                if not self.matrix[i].checkbox[j]:
                    print j+1,
            print ""
    def dump(self):
        print str(81-self.checkReadyCount()),"units unsolved..."
        for i in range(0,9):
            for j in range(0,9):
                pos=i*9+j
                if self.matrix[pos].isReady():
                    print self.matrix[pos].value,
                else:
                    print "-",
                if j%3==2 and not j==8:
                    print "|",
                print " ",
            if i%3==2 and not i==8:
                print " "
                for j in range(0,9):
                    print "---",
            print " " 
    def scan(self):
        for i in range(0,81):
            self.fullCheckForOneUnit(i)
        try:
            while True:
                ret=self.scanOnce()
                if ret<0:
                    ret=self.electOnce()
                if ret<0:
                    break
                self.fullCheckForOneUnit(ret)
        except Exception:
            return 2
        if self.checkReadyCount()==81:
            #print "Done"
            return 0
        else:
            return 1
    
def deepScan(s):
    #find a alternative
    i=0
    for i in range(0,81):
        if not s.matrix[i].isReady():
            break
    if i==81:
        return False

    for j in range(0,9):
        if s.matrix[i].checkbox[j]:
            continue
        a=copy.deepcopy(s)
        a.matrix[i].assign(j+1)
        ret=a.scan()
        if ret==0:
            a.dump()
            return True
        elif ret==1:
            if deepScan(a):
                return True
        
    if j==9:
        return False

                

vlist=[]
def loadvList(data):
    pos=0
    for i in range(0,9):
        for c in data[i]:
            if c>="0" and c <="9":
                if not c=="0":
                    vlist.append({"pos":pos,"val":int(c)})
                pos+=1
    if not pos==81:
        return False
    return True
           
import argparse
parser = argparse.ArgumentParser(description='A python programe to solve sudoku problem')
parser.add_argument('rows', nargs=9, metavar='row', help='9 rows of sudoku to be solved')
args=parser.parse_args()
    
if not loadvList(args.rows):
    print "error args!"
    sys.exit(0)

s=sudoku(vlist)
print "********* SOLVE BEGIN *********\n\n\n"
begin=time.time()
s.dump()

print "\n\n\nThe solutin is ...\n"
ret=s.scan()
if ret==0:
    s.dump()
elif ret==1:
    deepScan(s)
else:
    print "I can't solve this"
timeCost=(time.time()-begin)*1000
print "********* SOLVE DONE*********"
print "Total Cost: ",timeCost,"Mili Seconds"
