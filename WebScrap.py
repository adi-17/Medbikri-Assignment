from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl
import csv

#Author- Aditya Tomar
#Email- tomar.17aditya@gmail.co

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url="https://www.netmeds.com/prescriptions"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(req, context=ctx).read()         #ropening our requested url
soup = BeautifulSoup(html, "html.parser")       #parsing through the webpage
tags=soup('a')                                  #looking for the anchor tags
c=0
with open('task.csv', 'w', newline='') as file: #csv file to write the data
    writer = csv.writer(file)
    writer.writerow(["Disease Category", "Link", "Medicines"])      #the defining rows

    for tag in tags:
        if c<10:            #accessing only the first 10 entries, too much data on website for my RAM to handle :D

            if 'https://www.netmeds.com/prescriptions/' in tag.get('href'):     #finding all the deases on webpage 1
                c+=1
                pg1 = tag.get('href')
                pg1_txt=tag.contents[0]
                url1 = pg1
                req1 = Request(url1, headers={'User-Agent': 'Mozilla/5.0'})     #moving on to  webpage2 of each link
                html1 = urlopen(req1, context=ctx).read()
                soup1 = BeautifulSoup(html1, "html.parser")
                tags1 = soup1('a', {"class": "drug-list-title"})                #finding all anchor tags of a particular class
                pg2=[]
                for tag1 in tags1:
                    pg2.append(tag1.contents[0])

                writer.writerow([pg1_txt,pg1,pg2])                              #writing in our csv file
        else:
            break

print("Check the Database")