import pymongo
from .databaseTable import DatabaseTable


class Restaurants2(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def get_restaurants_by_neighborhood(self, db):
        restaurants = db[self.name].aggregate([
            {
                "$group": {
                    "_id": "$neighborhood", "count": {"$sum": 1}
                }
            }
        ])

        restaurants = list(restaurants)
        output = []
        for restaurant in restaurants:
            if '_id' in restaurant:
                output.append(
                    {
                        "neighborhood": str(restaurant['_id']),
                        "count": restaurant['count']
                    }
                )

        return output

    def get_restaurants_by_meals(self, db):
        output = []
        meals=['dessert','latenight','lunch','dinner','brunch','breakfast']

        for meal in meals:
            restaurants = db[self.name].aggregate([
                {
                    "$match": {"attributes.GoodForMeal."+meal: True}
                },
                {
                    "$group": {"_id": meal, "count": {"$sum":1}}
                }
            ])

            restaurants = list(restaurants)
            
            for restaurant in restaurants:
                if '_id' in restaurant:
                    output.append(
                        {
                            "meal": str(restaurant['_id']),
                            "count": restaurant['count']
                        }
                    )

        return output

    def get_restaurants_by_ambience(self, db):
            output = []
            ambiences=['romantic','intimate','classy','hipster','divey','touristy','trendy','upscale','casual']

            for am in ambiences:
                restaurants = db[self.name].aggregate([
                    {
                        "$match": {"attributes.Ambience."+am: True}
                    },
                    {
                        "$group": {"_id": am, "count": {"$sum":1}}
                    }
                ])

                restaurants = list(restaurants)
                
                for restaurant in restaurants:
                    if '_id' in restaurant:
                        output.append(
                            {
                                "ambience": str(restaurant['_id']),
                                "count": restaurant['count']
                            }
                        )

            return output

    def get_restaurants_by_music(self, db):
            output = []
            music=['dj','background_music','no_music','jukebox','live','video','karaoke']

            for m in music:
                restaurants = db[self.name].aggregate([
                    {
                        "$match": {"attributes.Music."+m: True}
                    },
                    {
                        "$group": {"_id": m, "count": {"$sum":1}}
                    }
                ])

                restaurants = list(restaurants)
                
                for restaurant in restaurants:
                    if '_id' in restaurant:
                        output.append(
                            {
                                "music": str(restaurant['_id']),
                                "count": restaurant['count']
                            }
                        )

            return output
        
    def get_restaurants_by_day(self, db):
        output = []
        dates=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

        for d in dates:
            restaurants = db[self.name].aggregate([
                {
                    "$match": {"attributes.BestNights."+d: True}
                },
                {
                    "$group": {"_id": d, "count": {"$sum":1}}
                }
            ])

            restaurants = list(restaurants)
            
            for restaurant in restaurants:
                if '_id' in restaurant:
                    output.append(
                        {
                            "day": str(restaurant['_id']),
                            "count": restaurant['count']
                        }
                    )

        return output