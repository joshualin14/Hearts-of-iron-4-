import sqlite3 

DATABASE = 'Hoi4.db'
while True:
    print("What are you looking for ?")

    print("print all countires = 1")
    print("print by leader = 2")
    print("print by date = 3") 
    print("print by ideology = 4")
    print("Exit the database = 5")
    Promt = input("Searching for ? ")
    
   


#Asks for what country you are looking for#
def country():
    with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "Select country_name, leader FROM countries"
            cursor.execute(sql,(searching,))
            results = cursor.fetchall()


            for country in results:
                 print(f"Country: {country[2]} ")
db.close()
                


   




  





