from pymongo import MongoClient

def get_database():
 
   CONNECTION_STRING = "mongodb://localhost:27017/"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['res_system']

database_name = get_database()
collection_name = database_name["restaurant"]

choice = input("Select a Option \n(1) Query Data from the database \n(2) Insert Data into the database \nOption: ")
if choice == "1":
    documents = collection_name.find()
    for document in documents:
        print(f"{document['name']}\t{document['phone_number']}\t{document['address']}")
elif choice == "2":
    item_1 = {
        "name": "Rising Peak Restaurant",
        "phone_number": "+275402309",
        "address": "40 Aambeeld, Pretoria, South Africa",
        "waiter":{
            "name":"John Doe",
            "phone_number": "+264811122334"
        },
        "dishes": [
            {
                "name":"Grouse and tofu panini", 
                "price":2199.99
                
            },
            {
                "name":"Grouse and apple ciabatta", 
                "price":2599.99
                
            },

            {
                "name":"Grouse and gruyere toastie", 
                "price":199.99
            },
            {
                
                "name":"Grouse and parmesan bagel", 
                "price": 299.99
            }
        ],
        "reservations":[
            {
                "title":"Sara Fischer", 
                "date":"2025-01-30", 
                "start_time":"20:00:00", 
                "party_size": 5, 
                "contact_number":"+264813027483", 
                "table":10,
                "bill_total":5499.99,
                "dishes":[
                    {
                        "name":"Grouse and tofu panini", 
                        "price":2199.99
                        
                    },
                    {
                        "name":"Grouse and apple ciabatta", 
                        "price":2599.99
                        
                    },
            
                    {
                        "name":"Grouse and gruyere toastie", 
                        "price":199.99
                    },
                    {
                        "name":"Grouse and gruyere toastie", 
                        "price":199.99
                    },
                    {
                        
                        "name":"Grouse and parmesan bagel", 
                        "price": 299.99
                    }
                ]
            }
        ]
    }

    resultId = collection_name.insert_one(item_1).inserted_id
    print(f"Inserted Restaurant ID : {resultId}")
    