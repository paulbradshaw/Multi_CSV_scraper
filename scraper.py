
#import our libraries
import scraperwiki
import csv
import lxml.html

allcsvs = 'http://www.tennis-data.co.uk/usopen.php'
baseurl = 'http://www.tennis-data.co.uk/'
idno = 0
def scrape_and_find_csv(url, idno):
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    #this selects all HTML containing link: <li><a>
    csvs = root.cssselect('p[align=left] a')
    print csvs
    for link in csvs:
        #this prints the result of adding the base URL to the relative link grabbed
        print link.attrib.get('href')
        if link.attrib.get('href')[-3:] == "csv":
            data = scraperwiki.scrape(baseurl+link.attrib.get('href'))
            reader = csv.DictReader(data.splitlines())
            for row in reader:
                idno = idno+1
                for key, value in row.iteritems():
                    print key
                    print value
                row['id'] = idno
                row['url'] = link
                scraperwiki.sqlite.save(['id'], row)

scrape_and_find_csv(allcsvs, idno)
