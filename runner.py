from parser import GraphQLParser

parser = GraphQLParser()
ast = parser.parse("""
{
  user(id: 4) {
    id
    name
    profilePic
    avatar: profilePic(width: 30, height: 30)
  }
}
""")
print(ast)



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