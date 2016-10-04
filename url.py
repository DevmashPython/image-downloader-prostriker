import urllib
import re

file = urllib.urlopen("https://www.tutorialspoint.com")
s = file.read()
new = open("urls.txt","w")
new.write(s)
new.close

store = re.compile('img src=".*\.jpg"')
findit= store.findall(s)
str1=''.join(findit)
store_num=re.compile('\w*\.jpg')
count_it=re.findall(store_num,str1)
count=str(count_it)
count.strip('img src=')
str1.strip('img src=')
string="https://www.tutorialspoint.com/"
for i in range (0,len(findit)):
	findit[i]=findit[i].replace('img src=','')
for i in range (0,len(findit)):
	print string+findit[i].replace('"','')
