from parser import GraphQLParser
import json
from data import get_information
from exceptions import ParseError

allowed_definitions = ['Query']
debug_mode = True

def raiseException(message):
    # raise Exception(message)
    print(message)
    raise SystemExit(0)

def write(message):
    if debug_mode:
        print(message)

class Interpreter():

    # def __init__(self, ast):
    #     self.ast = ast

    def checkDefinitionType(self, definition):
        def_type = str(type(definition))
        if def_type.split('.')[1].split('\'')[0] in allowed_definitions:
            return True
        else:
            return False

    def interpret(self, ast):
        definitions = getattr(ast, 'definitions')

        result = []
        error_occured = False
        error_message = ''
        for definition in definitions:

            if not self.checkDefinitionType(definition):
                # raiseException('Invalid Definition Type found!')
                error_occured = True
                error_message = 'Invalid Definition Type found!'
                # raise ParseError(message = error_message)

            selections = getattr(definition, 'selections')
            # print('selections: ', selections)

            if len(selections) > 1:
                # raiseException('Invalid syntax')
                error_occured = True
                error_message = 'Invalid syntax'

            for field in selections:
                # print('selection type: ',type(field))
                field_name = getattr(field,'name')
                print('Field Name: ', field_name)
                arguments = getattr(field,'arguments')
                # print('arguments: ',arguments)
                field_arguments = {}
                for argument in arguments:
                    arg_name = getattr(argument,'name')
                    arg_val = getattr(argument,'value')
                    field_arguments[arg_name] = arg_val
                print('Extracted Arguments: ', field_arguments)

                selection_set = getattr(field,'selections')
                selection_set_fields = []
                # print('selections: ', selection_set)
                for selection_set_field in selection_set:
                    selection_set_fields.append(getattr(selection_set_field, 'name'))
                print('selection_set_fields: ', selection_set_fields)


        final_data_result = {}
        if not error_occured:
            result, error_occured, error_message = get_information(field_name, field_arguments, selection_set_fields)

            if not error_occured:
                final_result = {}
                final_result [field_name] = result

                final_data_result['data'] = final_result
            else:
                error_dict = {}
                error_dict['message'] = error_message
                final_data_result['errors'] = error_dict
        else:
            error_dict = {}
            error_dict['message'] = error_message
            final_data_result['errors'] = error_dict

        # print('Extracted result: ', result)
        result_json = json.dumps(final_data_result)
        return result_json


def main():

    parser = GraphQLParser()
#     query = '''
# {
#     user(id: 4) {
#         id
#         name
#         profile
#     }
# }
#     '''

    query = '''
    query abc {
          droid(id: 2001) {
            # comments
            id
            name
          }
        }
    '''

    print('Query: ', query)
    query_ast = parser.parse(query)
    print('AST for the query: \n',query_ast, '\n')
    print('Now interpreting the AST...\n')
    interpreter = Interpreter()
    result = interpreter.interpret(query_ast)
    print('\nResult: ',result)





if __name__ == '__main__':
    main()
