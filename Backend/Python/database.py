import psycopg2

class Database():
    def __init__(self, user, password, host, name):
        #Params for connect Postgres database
        '''
        self.USER_DB="macia"
        self.PASSW_DB= "maica"
        self.HOST_DB="localhost"
        self.NAME_DB="marvel"
        '''
        self.USER_DB=user
        self.PASSW_DB= password
        self.HOST_DB=host
        self.NAME_DB=name
        self.connection = psycopg2.connect(
            host=self.HOST_DB,
            database=self.NAME_DB,
            user=self.USER_DB,
            password=self.PASSW_DB)


    def make_insert_database(self, inserts : list):
        '''
        param: inserts [] list of differents inserts.

        Connect to database and execute the differents inserts of param 'inserts'
        '''
        cur = self.connection.cursor()
        for insert in inserts:
            cur.execute(insert)

        cur = self.connection.cursor()
        self.connection.commit()
        cur.close()
    

    def join_all_inserts(self, all_inserts : list, on_conflict_insert=""):
        '''
        Join differents insert for the same table.
        Return a string with all this inserts.

        For example if we have
        Insert into <table>(...) values (...);  :a1
        Insert into <table>(...) values (...);  :a2
        ...
        Insert into <table>(...) values (...);  :an

        For do this inserts more efectivly is better do
        Insert into <table>(...) values a1, ..., an;
        '''
        if len(all_inserts)==0:
            return -1

        if len(all_inserts)==1:
            return all_inserts[0] + " "+ on_conflict_insert
        
        final_insert=""
        first_value=True
        for i in all_inserts:
            #aux=i.upper().split("VALUES (")
            aux=i.split("VALUES (")
            if first_value:
                final_insert+=aux[0]+" VALUES (" #This is INSERT INTO <table> values
                final_insert+=aux[1]
                first_value=False
            else:
                final_insert+=", " #For separate diferents inserts
                final_insert+="("+aux[1]
        final_insert += " "+ on_conflict_insert
        return final_insert
