from datetime import datetime
import psycopg

on_going_removals_appenditures_report = ""
inventory_updates = ""
connection = psycopg.connect(
    dbname="DB_NAME",
    user="username",
    password="password",
    host="host",
    port="portnumber"
)
cursor = connection.cursor()
cursor.execute("SELECT item_name, selling_price,units FROM inventory_table")
rows = cursor.fetchall()
intial_price_unit_values = [row for row in rows]
intial_date_of_record = datetime.now().strftime("%Y-%m-%d")


def add_to_inventory():
    new_item = []
    item_id = int(input("Enter item_id that you would like to input into the inventory: "))
    cursor.execute("SELECT * FROM inventory_table")
    rows = cursor.fetchall()
    for row in rows:
        if row[0] == int(item_id): 
            print(f"Sorry, the item_id {item_id} already exists in the inventory. Try updating the inventory of these particular values using the update command")
            break
        else: 
            selling_price =  float(input("Enter selling price: "))
            item_name = input("Enter the item name: ")
            units = int(input("Enter number of units: "))
            new_item = (item_id, item_name, int(input("Enter the current quantity in stock: ")), int(input("Enter the reorder_level: ")),
            float(input("Enter the cost_price: ")), selling_price, datetime.now().strftime("%Y-%m-%d"),int(input("Enter batch number: ")), units , input("Enter stock_status: "))
            sql = "INSERT INTO inventory_table (item_id, item_name, quantity_in_stock, reorder_level, cost_price, selling_price, last_update_date, batch_number, units, stock_status) VALUES" + str(new_item)
            cursor.execute(sql)
            connection.commit()
            print(f'Item {item_id} added to Inventory on {{datetime.now().strftime("%Y-%m-%d")}}')
            on_going_removals_appenditures_report += f'Item {item_id} added to Inventory on {datetime.now().strftime("%Y-%m-%d")}'
            intial_price_unit_values.append((item_name, selling_price))


def view_inventory():
    cursor.execute("SELECT * FROM inventory_table")
    for row in cursor.fetchall():
        print(row)

def delete_from_inventory():
    id_delete = int(input("What is the id of the item you would like to delete: "))
    sql_query = f"DELETE FROM inventory_table WHERE item_id = {id_delete};"
    cursor.execute(sql_query)
    connection.commit()
    print(f"Item {id_deleted} on {datetime.now().strftime('%Y-%m-%d')}\n")
    on_going_removals_appenditures_report += f'Item {id_deleted} on {datetime.now().strftime("%Y-%m-%d")}\n'

def update_inventory():
    item_id = int(input("Select the item_id you would like to update: "))
    value = input("Select the column you would like to update: ")
    change = input("Enter the change you would like to make to the input: ")
    update_query = f"UPDATE inventory_table SET {value} = {change} where item_id = {item_id}"
    print("Inventory Updated")
    cursor.execute(update_query)
    inventory_updates += f"Update made to {item_id}. The {value} was changed to {change} on {datetime.now().strftime('%Y-%m-%d')}\n"

def generate_Inventory_report():
    print(f"All recorded inventory updates: {invetory_updates}")
    print(f"All recorded inventory appends and deltes: {on_going_removals_appenditures_report}")

def generate_sales_report(intial_values): 

    #Gets new values 

    cursor.execute("SELECT item_name, selling_price, units, FROM inventory_table")
    rows = cursor.fetchall()
    new_values = [row for row in rows]
    for value in new_values: 
        print(f"{values[0]}: Units Sold: {init_values[2] - values[2]}. Money earned {int(value[1]) * (init_values[2] - values[2])}")



while True: 
    options = input("Would you like to generate Inventory report(I), generate sales report(S), update inventory(U), delete from inventory(D), View inventory(V), add to inventory(A), or exit(E): ")
    if options == "I": 
        generate_Inventory_report()
    elif options == "S":
        generate_sales_report()
    elif options == "U":
        update_inventory()
    elif options == "D":
        delete_from_inventory()
    elif options == "V":
        view_inventory()
    elif options == "A":
        add_to_inventory()
    elif options == "E":
        break
        cursor.close()
        conn.close()
    else: 
        print("Enter a valid command.")
