from ..configs.mysqlconnection import connectToMySQL

class Ninja:
    
    
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojos_id = data["dojos_id"] 
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    
    @classmethod
    def add_ninja(cls,data):
        query = 'INSERT INTO ninjas(first_name,last_name,age,created_at,updated_at,dojos_id) values(%(first_name)s,%(last_name)s,%(age)s,NOW(),NOW(),%(dojo_id)s);';
        con = connectToMySQL("dojos_and_ninjas_schema")
        results = con.query_db(query,data)