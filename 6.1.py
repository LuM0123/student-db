import mysql.connector
from mysql.connector import errorcode

class MySqlHelper:
    def __init__(self, host = None, user = None, password = None, database = None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db = None
        self.cursor = None

        if self.database == None:
            db = mysql.connector.connect(host = self.host,
                                         user = self.user,
                                         password = self.password)
            create_db = input("Would you like to create a database?")
            if create_db == 'yes':
                db_name = input("Please enter the name for your database: ")
                self.database = db_name
                mycursor = db.cursor()
                mycursor.execute("CREATE DATABASE {}".format(db_name))
                mycursor.execute("USE {}".format(db_name))

            else:
                exit(1)

        while True:
            try:
                db = mysql.connector.connect(host = self.host,
                                             user = self.user,
                                             password = self.password,
                                             database = self.database)
                self.db = db
                self.cursor = db.cursor()

                break

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Invalid user name or password, please try again")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                    create_db = input("Would you like to create a database?")
                    if create_db == "Yes":
                        db = mysql.connector.connect(host=self.host,
                                                     user=self.user,
                                                     password=self.password)
                        db_name = input("Please enter the name for your database: ")
                        self.database = db_name
                        mycursor = db.cursor()
                        mycursor.execute("CREATE DATABASE {}".format(db_name))
                        mycursor.execute("USE {}".format(db_name))

                    elif create_db == "No":
                        print("please try again")

                    else:
                        exit(1)

                else:
                    print(err)

    def SELECT(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def INSERT(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def UPDATE(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def DELETE(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.close()










