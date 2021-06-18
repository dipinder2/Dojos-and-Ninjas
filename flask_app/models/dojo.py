from ..configs.mysqlconnection import connectToMySQL
from ..models.ninja import Ninja


class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;";
        con = connectToMySQL("dojos_and_ninjas_schema")
        results = con.query_db(query)
        dojoObj = []
        for res in results:
            dojoObj.append(Dojo(res))
        return dojoObj
        
    
    @classmethod
    def add_dojo(cls,data):
        query = 'INSERT INTO dojos(name,created_at,updated_at) values( %(name)s,NOW(),NOW());'
        con = connectToMySQL("dojos_and_ninjas_schema")
        results = con.query_db(query,data)
        return results

    @classmethod
    def get_one(cls,data):
        con = connectToMySQL("dojos_and_ninjas_schema")
        queryNinjas = 'SELECT * from dojos LEFT JOIN'\
            ' ninjas ON ninjas.dojos_id= dojos.id'\
            ' WHERE dojos.id = %(id)s;'
        results = con.query_db(queryNinjas,data)
        dojo = Dojo(results[0])
        
        ninjas = []
        if results[0]['ninjas.id'] != None:
            for ninja in results:
                row_data = {'id':ninja["ninjas.id"],'first_name':ninja["first_name"],'last_name':ninja['last_name'],'age':ninja['age'],'dojos_id':ninja['dojos_id'],'created_at':ninja['ninjas.created_at'],'updated_at':ninja['ninjas.updated_at']}
                dojo.ninjas.append(Ninja(row_data))
        
        return dojo   
    
    
    # @classmethod
    # def get_ninjas_of_dojo(cls,data):
    #     query = 'SELECT * from dojos JOIN'\
    #         ' ninjas ON ninjas.dojos_id= dojos.id'\
    #         ' WHERE dojos.id = %(id)s;'
    #     con = connectToMySQL("dojos_and_ninjas_schema")
    #     results = con.query_db(query,data)
    #     ninjas = []
    #     for ninja in results:
    #         ninjas.append(
    #             Ninja({'id':ninja["ninjas.id"],'first_name':ninja["first_name"],'last_name':ninja['last_name'],'age':ninja['age'],'dojos_id':ninja['dojos_id'],'created_at':ninja['ninjas.created_at'],'updated_at':ninja['ninjas.updated_at']}))
    #     return ninjas