import urllib2
import re
import csv

hdr = {'User-Agent': 'Chrome/49.0.2623.87'}
request = urllib2.Request("http://www.drugs.com/imprints.html",headers=hdr)
response = urllib2.urlopen(request)
page = response.read()
html = page.decode()

srno = 0

#here if we use .* instead of .*? then we get a list
#with a single entry in it....basically it picks up the first link and then
#matches everything in between and then picks up the last link and matches till
# .html....this shows re is quite powerful as it finds the last occurence of
# .html to match....while in our case .*? the '?' slows down .* in a sense that
#as soon as it finds the first match for .html it stops .* from pulling in more
#characters....and hence starts looking for the next match in line!!

for match in re.findall("\/imprint.*?\.html",html):
    url = "http://www.drugs.com" + match
    request = urllib2.Request(url,headers=hdr)
    response = urllib2.urlopen(request)
    html = response.read()
    #html = page.decode()
    for imprint in re.findall("\/imprints\/(.*?)\.html",html):
        info_url = "http://www.drugs.com/imprints/" + imprint + ".html"
        request = urllib2.Request(info_url,headers=hdr)
        response = urllib2.urlopen(request)
        html = response.read()

        generic_name = re.findall('<dt>Generic Name:<\/dt>\s*?<dd>(.*?)<\/dd>',html)
        strength = re.findall('<dt>Strength:<\/dt>\s*<dd>(.*?)<\/dd>',html)
        color = re.findall('<dt>Color:<\/dt>\s*<dd>(.*?)<\/dd>',html)
        shape = re.findall('<dt>Shape:<\/dt>\s*<dd>(.*?)<\/dd>',html)
        for atr in (imprint,generic_name,strength,color,shape):
        	if len(atr) == 0:
        		atr.append('*')

        global srno
        srno += 1
        with open('re.csv', 'ab') as csvfile:
       		spamwriter = csv.writer(csvfile,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    		spamwriter.writerow([srno,imprint,''.join(generic_name),''.join(strength),''.join(color),''.join(shape)])
        
        print imprint,generic_name,strength,color,shape
