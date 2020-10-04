
class Item():

    def __init__(self, item):
        self.ID = item["list_id"]
        self.publication_date = item["first_publication_date"]
        #self.expiration_date = item["expiration_date"]
        self.status = item["status"]
        self.categorie = item["category_name"]
        self.sujet = item["subject"]
        self.definition = item["body"]
        self.type = item["ad_type"]
        self.url = item["url"]
        if "price" not in item:
            self.prix = 0
        else:
            self.prix = item["price"][0]
        self.images = item["images"]
        self.attributes = item["attributes"]

        ## Maybe do a specific class for location
        #self.localisation = item["location"]
        self.region = item["location"]["region_name"]
        self.departement = item["location"]["department_name"]
        self.ville = item["location"]["city"]
        self.code_postal = item["location"]["zipcode"]
        #self.coordonee.lat = item["location"]["lat"]
        #self.coordonee.lng = item["location"]["lng"]

        #Doing stuff with owner
        self.owner = Owner(item["owner"])


        self.has_phone = item["has_phone"]
        if "calendar" in item:
            self.calendar = item["calendar"]

    def do_print(self):
        print(self.definition)

class Owner():

    def __init__(self, owner):
        self.store_id = owner["store_id"]
        self.id = owner["user_id"]
        self.type = owner["type"]
        self.name = owner["name"]
        self.salesmen = not owner["no_salesmen"]
