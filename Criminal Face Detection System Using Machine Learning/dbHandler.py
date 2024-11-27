import pymysql

def insertData(data):
    rowId = 0

    db = pymysql.connect(host="localhost",
                         user= "root",
                         password= "12345678", 
                         database="criminal")
    cursor = db.cursor()
    print("database connected")

    print(data)
    query = "INSERT INTO criminals(name, father_name, gender, dob, crimes_done) VALUES('%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["Father's Name"], data["Gender"],
             data["DOB(yyyy-mm-dd)"], data["Crimes Done"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except Exception as e: 
        print(e)
        db.rollback()
        print("Data insertion failed")


    db.close()
    print("connection closed")
    return rowId

def retrieveData(name):
    id = None
    criminaldata1 = None

    db = pymysql.connect(host="localhost",
                         user= "root",
                         password= "12345678", 
                         database="criminal")
    cursor = db.cursor()
    print("database connected")

    query = "SELECT * FROM criminals WHERE name='%s'"%name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        id=result[0]
        criminaldata1 = {
            "Name" : result[1],
            "Father's Name" : result[2],
            "Gender" : result[3],
            "DOB(yyyy-mm-dd)" : result[4],
            "Crimes Done" : result[5]
        }

        print("data retrieved")
    except Exception as e: 
        print(e)
        print("Error: Unable to fetch data")

    db.close()
    print("connection closed")

    return (id, criminaldata1)
