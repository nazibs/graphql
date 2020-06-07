from parser import GraphQLParser

parser = GraphQLParser()
ast = parser.parse("""
{
  user(id: 4) {
    id
    name
    profilePic
  }
}
""")
print(type(ast))
# print(ast.right())
print(getattr(ast, 'definitions'))
print(type(getattr(ast, 'definitions')[0]))
print(getattr(ast, 'definitions')[0])
print(type(getattr(getattr(ast, 'definitions')[0], 'selections')))
print(getattr(getattr(ast, 'definitions')[0], 'selections')[0])

print(getattr(getattr(ast, 'definitions')[0], 'selections')[0])

'''
<
Document: 
  definitions=[
    < Query: 
      selections=[
        <Field: 
            name=user, 
            arguments=[<Argument: name=id, value=4>], 
            selections=[<Field: name=id>, 
        <Field: name=name>, 
        <Field: name=profilePic>, 
        <Field: 
            name=profilePic, 
            alias=avatar, 
            arguments=[
              <Argument: name=width, value=30>, 
              <Argument: name=height, value=30>]>
              ]
        >
      ]
    > 
  ]
>

'''


Final_output = '''
{
    "data": {
        "user": {
            "id": 4
            "name": Nazib
        } 
    }
}
'''
