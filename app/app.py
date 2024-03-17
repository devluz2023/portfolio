import pymysql
import logging

# Set up logging
logging.basicConfig(filename='mysql_log.log', level=logging.INFO)

# Connect to MySQL
connection_master = pymysql.connect(host='localhost',
                                    user='root',
                                    password='master_password',
                                    database='mydatabase',
                                    cursorclass=pymysql.cursors.DictCursor)

connection_slave = pymysql.connect(host='localhost',
                                   user='root',
                                   password='slave_password',
                                   database='mydatabase',
                                   cursorclass=pymysql.cursors.DictCursor)

# Function to insert data into MySQL and log the action
def insert_data(connection, data):
    try:
        with connection.cursor() as cursor:
            # Insert some data
            sql = "INSERT INTO `mytable` (`data`) VALUES (%s)"
            cursor.execute(sql, (data,))
            connection.commit()
            logging.info(f"Data '{data}' inserted into {connection.host}")
    except Exception as e:
        logging.error(f"Error inserting data: {str(e)}")

# Test data insertion
insert_data(connection_master, 'Data from master')
insert_data(connection_slave, 'Data from slave')

# Close connections
connection_master.close()
connection_slave.close()
