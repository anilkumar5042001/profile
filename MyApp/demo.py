import mysql.connector


def GetCountry():
    con=mysql.connector.connect(host="localhost",user="root",passwd="admin123",database="world",port=3306)
    print("Connecetd")
    cur=con.cursor()
    cur.execute("select Code,Name from country")
    print("res1")
    rows=cur.fetchone()
    print("res")
    result=rows[0]
    print(result)
    

    con.close()
    return result

GetCountry()
