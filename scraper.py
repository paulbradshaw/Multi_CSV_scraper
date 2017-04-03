import scraperwiki
import csv
import lxml.html

allcsvs = 'https://data.birmingham.gov.uk/dataset/voluntary-and-community-sector-funding-information'

def scrape_and_find_csv(url):
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    #this selects all HTML containing link: <li><a>
    csvs = root.cssselect('li a')
    print csvs
    for link in csvs:
    #this prints the result of adding the base URL to the relative link grabbed
    print baseurl+link.attrib.get('href')


data = scraperwiki.scrape('https://data.birmingham.gov.uk/dataset/14492d37-1a77-4d46-9204-27363fc62149/resource/bacf38dd-3530-4c95-a0c3-83e21c9b2259/download/sgmsreportsvcsfreportsvcsfreports201415vcsfreport2014qtr1final.csv')

reader = csv.DictReader(data.splitlines())

for row in reader:
    for key, value in row.iteritems():
        print key
    row['Actual Funding Award'] = row['Actual Funding Award'].decode("latin-1")
    row['Annual Total 2012/2013'] = row['Annual Total 2012/2013'].decode("latin-1")
    row['Annual Total 2013/2014'] = row['Annual Total 2013/2014'].decode("latin-1")
    row['Annual Total2014/2015'] = row['Annual Total2014/2015'].decode("latin-1")
    row['Overall Total Paid'] = row['Overall Total Paid'].decode("latin-1")
    print row['Ref. No.']
    scraperwiki.sqlite.save(['Ref. No.'], row)
