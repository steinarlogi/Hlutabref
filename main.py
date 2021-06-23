import data_manager
import db_connection as db

connection = data_manager.DataConnection()
db_connection = db.DatabaseConnection("database/test.db")

print(db_connection.getallceos())
