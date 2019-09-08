import sqlite3

class DbConnect:
    def __init__(self):
        self._db=sqlite3.connect("Reservation.db")
        self._db.row_factory=sqlite3.Row
        self._db.execute("create table if not exists Ticket(ID integer primary key autoincrement,Name text ,Gender text,Comment text)")
        self._db.commit()

    def Add(self,Name,Gender,Comment):
        self._db.row_factory = sqlite3.Row
        #add records
        self._db.execute("insert into Ticket(Name,Gender,Comment) values(?,?,?)",(Name,Gender,Comment))
        self._db.commit()
        return("record is added")

    def ListTickets(self):
        cursor=self._db.execute("select * from Ticket")
        return cursor

    def DeleteRecord(self,ID):
        self._db.row_factory=sqlite3.Row
         #delete records
        self._db.execute("delete from Ticket where ID=?".format(ID))
        self._db.commit()
        return ("record is deleted")

    def UpdateRecord(self,ID,Comment):
        self._db.row_factory = sqlite3.Row
        #add records
        self._db.execute("update Ticket set Comment=? where ID=?".format(Comment,ID))
        self._db.commit()
        return ("record is updated")

