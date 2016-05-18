#!/usr/bin/python  
# -*- coding:utf-8 -*-  
#author: weiwu jiang @ 2016.3.38
import urllib                                                    
import urllib2                                                   
import re
import os 

def reporthook(block_read,block_size,total_size):  
  if not block_read:  
    print "connection opened";  
    return  
  if total_size<0:  
    #unknown size  
    print "read %d blocks (%dbytes)" %(block_read,block_read*block_size)
  else:  
    amount_read=block_read*block_size;  
    print 'Read %d blocks,or %d/%d' %(block_read,block_read*block_size,total_size)

def getPDFFromNet(inputURL,localDir):  
        req = urllib2.Request(inputURL)  
        f = urllib2.urlopen(req)                                 
                  
        urlList = []                                                
        for eachLine in f:                                        
                line = eachLine.strip()                            
                if re.match('.*pdf.*', line):                      
                        wordList = line.split('\">')                                    
                        for word in wordList:                     #遍历每个字符串  
                            if re.match('.* href=.*\.pdf$', word):    #去匹配含有“.pdf”的字符串，只有url中才有
                                urlList.append(word)                  #将提取的url存入列表  
        for everyURL in urlList:                                      #遍历列表的每一项，即每一个PDF的url 
                wordItems = everyURL.split('</td><td><a href="')                   
                for item in wordItems:                            
                        if re.match('.*\.pdf$', item):             
                                PDFName = item                    
                                #print PDFName
                localPDF = localDir + PDFName                     
                everyURL = inputURL + PDFName
                #print localPDF,everyURL
                try:                                               
                        urllib.urlretrieve(everyURL, localPDF)    #按照url进行下载，并以其文件名存储到本地目录
                        ##urllib.urlretrieve(everyURL, localPDF, reporthook=reporthook) 
                except Exception,e:  
                        continue  

if __name__ == '__main__':

  localDir = '.\\pdf\\'          #本地存储目录 
  if not os.path.isdir(localDir):
            os.mkdir(localDir)
  getPDFFromNet('http://courses.cs.washington.edu/courses/cse546/14au/slides/',localDir)  



	
	
