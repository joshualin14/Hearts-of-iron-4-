import sqlite3 

DATABASE = 'Hoi4.db'

#Asks for what country you are looking for#
def print_all_countries():
    searching = input('what country are you looking for ? ')
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "Select country_name, leader FROM countries"
        cursor.execute(sql,(searching,))
        results = cursor.fetchall()


        for country in results:
            print(f"Country: {country[2]} Leader : {country[3]}")

if __name__ == "__main__":
    print_all_countries()


