import scraperwiki
import csv
#guidance on csv library at https://scraperwiki.com/docs/python/python_csv_guide/

#scrape the csv file into new variable 'data'
data = scraperwiki.scrape('http://www.offa.org.uk/wp-content/uploads/2013/07/OFFA-data-for-2013-06.csv')

#use .reader function and .splitlines() method to put 'data' into csv object 'reader'
reader = csv.reader(data.splitlines())
print reader

record = {}

idno = 0
for row in reader:
    record['Department'] = row[0]
    record['Entity'] = row[1]
    record['Payment date'] = row[2]
    record['Expenditure Type'] = row[3]
    record['Cost Centre'] = row[4]
    record['Supplier/Institution'] = row[5]
    record['Transaction No'] = row[6]
    record['Value'] = row[7]
    idno += 1
    record['ID'] = idno
    print record
    scraperwiki.sqlite.save(['ID'], record)

#After first (header) row, this will generate an error with this data:
#SqliteError: Binary strings must be utf-8 encoded

#To see what happens next, go to: https://scraperwiki.com/scrapers/birminghamcouncilexpenditure_2nd/
