from flask_restful import Resource


class ResellerResource(Resource):

    def get(self):
        return {"return": "it's run"}
