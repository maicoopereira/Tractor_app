import sqlite3
import json
import model.machines as machines
import controller.databaseCursor as db




#Create a file to connect to the database
#create objects, for the machines, services, clients, technicians, expendables
#use the main file to run the program
#use functions to create, read, update and delete the objects
#use functions to create, read, update and delete the objects in the database

#create a model, controller, view structure
#use the model to create the objects
#use the controller to create the functions
#use the view to create the user interface
#use the main file to run the program

#the view inicially will be a command line interface
#than we can create a graphical user interface using tkinter or pyqt
#the database will be sqlite3
#the objects will be stored in the database





# conn = sqlite3.connect('machines.db')
# cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS services (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         brand_name TEXT,
#         model_name TEXT,
#         client_name TEXT,
#         series_num TEXT,
#         license_plate TEXT,
#         hour_meter TEXT,
#         service_date TEXT,
#         service_done TEXT,
#         machine_list TEXT
#     )
# ''')

def main():
    brand_name = ''
    model_name = ''
    client_name = ''
    series_num = ''
    license_plate = ''
    hour_meter = ''
    service_date = ''
    service_done = ''
    #machine_list = []
    
    while True:
        #select a database
        database = input("Enter the database name (or type 'exit' to quit): ")
        if database.lower() == 'exit':
            break
        database = database.lower if database.endswith('.db') else database + '.db'
        database = 'data/machines.db'  #default database
        #create a database connection
        print(f"Using database: {database}")
        print("Creating database connection...")
        print("..." * 10)
        db_cursor = db.DatabaseCursor(database)
        db_cursor.set_database(database)
        
        #create a machine object
        print("..." * 10)
        brand_name = input("Brand Name or type exit to quit: ")
        if brand_name.lower() == 'exit':    
            break
        model_name = input("Model Name: ")
        client_name = input("Qual o cliente: ")
        series_num = input("Series Number: ")
        license_plate = input("License Plate: ")
        hour_meter = input("Hour Meter: ")
        service_date = input("Service Date (YYYY-MM-DD): ")
        service_done = input("Service Done: ")
        new_machine = machines.Machines(brand_name, model_name, client_name, series_num, license_plate, hour_meter, service_date, service_done)
        
        
        new_machine.display_details()
 
        confirmation = input("Are these details correct? (yes/no): ")
        if confirmation.lower() == 'yes':
            print("Details confirmed.")
            new_machine.add_to_database(db_cursor)
        else:
            print("Details discarded. Please re-enter the information.")
            
        # Insert the service details into the database
        

        #  # Append the service details to the list
        # machine_list.append({
        #      'brand_name': brand_name,
        #      'model_name': model_name,
        #      'client_name': client_name,
        #      'series_num': series_num,
        #      'license_plate': license_plate,
        #      'hour_meter': hour_meter,
        #      'service_date': service_date,
        #      'service_done': service_done
        #  })
        #  # Insert the service details into the database
        #  cursor.execute("INSERT INTO services (brand_name, model_name,client_name, series_num, license_plate, hour_meter, service_date, service_done, machine_list) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (brand_name, model_name, client_name, series_num, license_plate, hour_meter, service_date, service_done, json.dumps(machine_list)))
        #  conn.commit()
        #  add_another = input("Do you want to add another machine? (yes/no): ")
        #  if add_another.lower() != 'yes':
        #      break
     
    # # Close the database connection
    # conn.close()



    # Print the collected service details
    # print("\nCollected Service Details:")  
    # print(machine_list)



if __name__ == '__main__':
    main()