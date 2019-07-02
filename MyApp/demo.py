import mysql.connector


def GetCountry():
    con=mysql.connector.connect(host="localhost",user="root",passwd="admin123",database="world",port=3306)
    #con=mysql.connector.connect(host="anil5042001.mysql.pythonanywhere-services.com",user="anil5042001",passwd="admin123",database="anil5042001$SubmitProfile",port=3306)
    print("Connecetd")
    cur=con.cursor()
    # cur.execute("select Id,CountryName from Country")
    cur.execute("select Code,Name from Country")
    print("res1")
    rows=cur.fetchone()
    print("res")
    result=rows[0]
    print(result)
    

    con.close()
    return result

GetCountry()
