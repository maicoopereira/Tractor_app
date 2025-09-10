import sqlite3
import json
conn = sqlite3.connect('machines.db')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expendables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        quantity FLOAT,
        date_aquisition TEXT,
        item_list TEXT
    )
''')

def main():
    item = ''
    quantity = ''
    date_aquisition = ''
    item_list = []
    
    while True:
        print("Enter item details (or type 'exit' to finish):")
        # Collect service details from the user
        # If the user types 'exit', break the loop
        item = input("Item name or type exit to quit: ")
        if item.lower() == 'exit':    
            break
        quantity = input("Quantity of " + item + ": ")
        date_aquisition = input("Date of aquisition: ")

        # Append the service details to the list
        item_list.append({
            'item': item,
            'quantity': quantity,
            'date_aquisition': date_aquisition
        })
        # Insert the service details into the database
        cursor.execute("INSERT INTO expendables (item, quantity, date_aquisition, item_list) VALUES (?, ?, ?, ?)", (item, quantity, date_aquisition, json.dumps(item_list)))
        conn.commit()
        add_another = input("Do you want to add another item? (yes/no): ")
        if add_another.lower() != 'yes' or add_another.lower() != 'sim' or add_another.lower() != 's':
            break
        
    # Close the database connection
    conn.close()



    # Print the collected service details
    print("\nCollected Service Details:")  
    print(item_list)



if __name__ == '__main__':
    main()