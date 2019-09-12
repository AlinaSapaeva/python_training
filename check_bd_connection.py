import pymysql.cursors

connection = pymysql.connect(host = "127.0.0.1", database = "addressbook", user = "root", password = "")

try:
    cursor = connection.cursor()
    cursor.execute("select firstname, middlename, lastname, nickname, title,"
                           " company, address, home, mobile, work, fax, email, email2, email3, homepage,  "
                           "address2, phone2 , notes from addressbook")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()