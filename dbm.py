import pymysql as p

def getconnection():
    
    return p.connect(host="localhost",user="root",password="",database="db2")

t=('sam','samhere@gmail.com','sam@123',9922056281)

def insertrec(t):
    db=getconnection()
    cr=db.cursor()
    sql="insert into my_table values(%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

##insertrec(t)

def displayrec():
    db=getconnection()
    cr=db.cursor()
    sql="select * from my_table"
    cr.execute(sql)
    data=cr.fetchall()
##    print(data)
    db.commit()
    db.close()
    return data

##displayrec()

def deleterec(email):
    db=getconnection()
    cr=db.cursor()
    sql="delete from my_table where email=%s"
    cr.execute(sql,email)
    db.commit()
    db.close()

##deleterec(102)

def selectrec(email):
    db=getconnection()
    cr=db.cursor()
    sql="select email,password from my_table where email=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    #print(data)
    db.commit()
    db.close()
    return data



##a=selectrec("sam@123")
#print(a)
def selectrec1(email):
    db=getconnection()
    cr=db.cursor()
    sql="select * from my_table where email=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

def sel(email):
    db=getconnection()
    cr=db.cursor()
    sql="select * from my_table where email=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data[0]
    
#print(sel("sam@123"))

#t=('hina','hina123@gmail.com','hina@123',2587421565,103)
def updaterec(t):
    db=getconnection()
    cr=db.cursor()
    sql="update my_table set name=%s,email=%s,password=%s,contact=%s where email=%s"
    cr.execute(sql,t)
    db.commit()
    db.close()

#updaterec(t)
