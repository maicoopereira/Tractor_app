import sqlite3
import json
conn = sqlite3.connect('machines.db')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_name TEXT,
        model_name TEXT,
        series_num TEXT,
        license_plate TEXT,
        hour_meter TEXT,
        service_date TEXT,
        service_done TEXT,
        machine_list TEXT
    )
''')

def main():
    brand_name = ''
    model_name = ''
    series_num = ''
    license_plate = ''
    hour_meter = ''
    service_date = ''
    service_done = ''
    machine_list = []
    
    while True:
        print("Enter service details (or type 'exit' to finish):")
        # Collect service details from the user
        # If the user types 'exit', break the loop
        brand_name = input("Brand Name or type exit to quit: ")
        if brand_name.lower() == 'exit':    
            break
        model_name = input("Model Name: ")
        series_num = input("Series Number: ")
        license_plate = input("License Plate: ")
        hour_meter = input("Hour Meter: ")
        service_date = input("Service Date (YYYY-MM-DD): ")
        service_done = input("Service Done: ")

        # Append the service details to the list
        machine_list.append({
            'brand_name': brand_name,
            'model_name': model_name,
            'series_num': series_num,
            'license_plate': license_plate,
            'hour_meter': hour_meter,
            'service_date': service_date,
            'service_done': service_done
        })
        # Insert the service details into the database
        cursor.execute("INSERT INTO services (brand_name, model_name, series_num, license_plate, hour_meter, service_date, service_done, machine_list) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (brand_name, model_name, series_num, license_plate, hour_meter, service_date, service_done, json.dumps(machine_list)))
        conn.commit()
        add_another = input("Do you want to add another machine? (yes/no): ")
        if add_another.lower() != 'yes':
            break
        
    # Close the database connection
    conn.close()



    # Print the collected service details
    print("\nCollected Service Details:")  
    print(machine_list)



if __name__ == '__main__':
    main()