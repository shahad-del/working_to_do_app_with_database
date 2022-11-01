import mysql.connector
dbconfig = {
	'host': '127.0.0.1',
	'database': 'bucket_list',
	'user': 'root',
	'password': 'mysqlroot'
}
def insert_sql(dataToInsert):
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	_sql = 'INSERT INTO list(items)values(%s)'
	cursor.execute(_sql,dataToInsert)
	conn.commit()
	cursor.close()
	conn.close()
def getAll():
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	_sql = 'SELECT * FROM list ORDER BY id DESC'
	cursor.execute(_sql)
	records = cursor.fetchall()
	cursor.close
	return records
def edit_data(data_to_edit,updated_info):
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	_sql = 'UPDATE list SET items = %s  where items = %s'
	val = (updated_info,data_to_edit)
	cursor.execute(_sql,val)
	conn.commit()
	cursor.close()
	conn.close()
def delete_data(item_to_delete):
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	_sql = 'DELETE FROM list WHERE items = %s'
	cursor.execute(_sql,item_to_delete)
	conn.commit()
	cursor.close()
	conn.close()