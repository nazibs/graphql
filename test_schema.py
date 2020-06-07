import graphene
from datetime import datetime 
import json

class User(graphene.ObjectType):
	id = graphene.ID()
	username = graphene.String()
	last_login = graphene.DateTime()


class QueryUsers(graphene.ObjectType):
	users = graphene.List(User)

	def resolve_users(self, info):
		return [
			User(username = 'Nazib', last_login = datetime.now()),
			User(username = 'Rashmi', last_login = datetime.now()),
		]


schema_users = graphene.Schema(query = QueryUsers)

users_results = schema_users.execute(
	'''
	{
		users{
			username
			lastLogin
		}
	}
	'''
	)

items = dict(users_results.data.items())
print(json.dumps(items, indent = 4))



class Query(graphene.ObjectType):
	is_staff = graphene.Boolean()


	def resolve_is_staff(self, info):
		return True


schema = graphene.Schema(query=Query)


result = schema.execute(
	'''
	{
		isStaff
	}
	'''
)



# print(result.data.items())



