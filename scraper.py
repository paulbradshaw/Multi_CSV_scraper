import scraperwiki
import csv
#guidance on csv library at https://scraperwiki.com/docs/python/python_csv_guide/

#scrape the csv file into new variable 'data'
data = scraperwiki.scrape('https://data.birmingham.gov.uk/dataset/14492d37-1a77-4d46-9204-27363fc62149/resource/bacf38dd-3530-4c95-a0c3-83e21c9b2259/download/sgmsreportsvcsfreportsvcsfreports201415vcsfreport2014qtr1final.csv')

#use .reader function and .splitlines() method to put 'data' into csv object 'reader'
reader = csv.reader(data.splitlines())
print reader

record = {}

idno = 0
for row in reader:
    record['Councillor'] = row[0]
    record['Basic'] = row[1]
    record['SRA'] = row[2]
    record['Basic Arrs'] = row[3]
    '''




    record['SRA Arrs'] = row[4]
    record['Travel'] = row[5]
    record['Dep Care'] = row[6]
    record['Mileage'] = row[7]
    '''
    idno += 1
    record['ID'] = idno
    print record
    scraperwiki.sqlite.save(['ID'], record)

#After first (header) row, this will generate an error with this data:
#SqliteError: Binary strings must be utf-8 encoded

#To see what happens next, go to: https://scraperwiki.com/scrapers/birminghamcouncilexpenditure_2nd/
