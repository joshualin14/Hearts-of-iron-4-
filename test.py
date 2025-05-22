import sqllite3 

DATABASE = 'Hoi4.db'

def print_all_countries():
    searching = input('What country ? ')
with sqllite3.connect(DATABASE) as db:
    cursor = db.cursor()
    sql = "Select country_name, leader FROM countries"
    cursor.execute(sql,(searching,))