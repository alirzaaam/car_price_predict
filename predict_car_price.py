from bs4 import BeautifulSoup
import requests
import re
import mariadb
from sklearn import tree
import sys

x = []
y = []
# for 100 pages
for i in range(1,100):
    geturl = requests.get('https://www.truecar.com/used-cars-for-sale/listings/?buyOnline=true&page=%d'%i)
    soup = BeautifulSoup(geturl.text, 'html.parser')
# connect to the database
    try :
        conn = mariadb.connect(user='root', password='2552', database='python')
    
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cursor = conn.cursor()
    main_s = soup.find_all('div', class_='d-flex flex-column w-100')
        
    for i in main_s:
            price = i.find('div', class_='heading-3 margin-y-1 font-weight-bold')
            miles = i.find('div', class_='d-flex w-100 justify-content-between')
            miles_noname = re.sub('[a-zA-Z,]+', '', miles.text)
            car_name = i.find('span', class_='vehicle-header-make-model text-truncate')
            # car_name_ws = re.sub('[\s]','',car_name.text)
            year = i.find('span',class_='vehicle-card-year font-size-1')
            priceSS = re.sub('[,$]','',price.text)
            cursor.execute("INSERT INTO cars (name, miles,year, price) VALUES (%s, %s,%s, %s)", (car_name.text, miles_noname,year.text ,priceSS))
            conn.commit()

name_vorodi = input("Enter Your Car name : ")
cursor.execute("SELECT miles,year,price FROM cars  WHERE name = '%s'"%(name_vorodi))

conn.commit()


for i in cursor : 
    
    x.append(i[0:2])
    y.append(i[2])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

karkard = input("Miles : ")
salemashin = input("Year : ")

new_data = [[karkard,salemashin]]
answer = clf.predict(new_data)
print ('Price :',answer[0],'$')
conn.close()



