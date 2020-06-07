
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'documentAT BANG BRACE_L BRACE_R BRACKET_L BRACKET_R COLON DOLLAR EQUALS FALSE FLOAT_VALUE FRAGMENT INT_VALUE MUTATION NAME NULL ON PAREN_L PAREN_R QUERY SPREAD STRING_VALUE TRUE\n        document : definition_list\n        \n        document : selection_set\n        \n        definition_list : definition_list definition\n        \n        definition_list : definition\n        \n        definition : operation_definition\n                   \n        \n        operation_definition : operation_type name variable_definitions directives selection_set\n        \n        operation_definition : operation_type name variable_definitions selection_set\n        \n        operation_definition : operation_type name directives selection_set\n        \n        operation_definition : operation_type name selection_set\n        \n        operation_definition : operation_type variable_definitions directives selection_set\n        \n        operation_definition : operation_type variable_definitions selection_set\n        \n        operation_definition : operation_type directives selection_set\n        \n        operation_definition : operation_type selection_set\n        \n        operation_type : QUERY\n                       | MUTATION\n        \n        selection_set : BRACE_L selection_list BRACE_R\n        \n        selection_list : selection_list selection\n        \n        selection_list : selection\n        \n        selection : field\n\n        \n        field : alias name arguments directives selection_set\n        \n        field : name arguments directives selection_set\n        \n        field : alias name directives selection_set\n        \n        field : alias name arguments selection_set\n        \n        field : alias name arguments directives\n        \n        field : name directives selection_set\n        \n        field : name arguments selection_set\n        \n        field : name arguments directives\n        \n        field : alias name selection_set\n        \n        field : alias name directives\n        \n        field : alias name arguments\n        \n        field : alias name\n        \n        field : name arguments\n        \n        field : name directives\n        \n        field : name selection_set\n        \n        field : name\n        \n        directives : directive_list\n        \n        directive_list : directive_list directive\n        \n        directive_list : directive\n        \n        directive : AT name arguments\n                  | AT name\n        \n        arguments : PAREN_L argument_list PAREN_R\n        \n        argument_list : argument_list argument\n        \n        argument_list : argument\n        \n        argument : name COLON value\n        \n        variable_definitions : PAREN_L variable_definition_list PAREN_R\n        \n        variable_definition_list : variable_definition_list variable_definition\n        \n        variable_definition_list : variable_definition\n        \n        variable_definition : DOLLAR name COLON type default_value\n        \n        variable_definition : DOLLAR name COLON type\n        \n        variable : DOLLAR name\n        \n        default_value : EQUALS const_value\n        \n        name : NAME\n             | FRAGMENT\n             | QUERY\n             | MUTATION\n             | ON\n             | TRUE\n             | FALSE\n             | NULL\n        \n        alias : name COLON\n        \n        value : variable\n              | INT_VALUE\n              | FLOAT_VALUE\n              | STRING_VALUE\n              | null_value\n              | boolean_value\n              | enum_value\n              | list_value\n              | object_value\n        \n        const_value : INT_VALUE\n                    | FLOAT_VALUE\n                    | STRING_VALUE\n                    | null_value\n                    | boolean_value\n                    | enum_value\n                    | const_list_value\n                    | const_object_value\n        \n        boolean_value : TRUE\n                      | FALSE\n        \n        null_value : NULL\n        \n        enum_value : NAME\n                   | FRAGMENT\n                   | QUERY\n                   | MUTATION\n                   | ON\n        \n        list_value : BRACKET_L value_list BRACKET_R\n                   | BRACKET_L BRACKET_R\n        \n        value_list : value_list value\n        \n        value_list : value\n        \n        const_list_value : BRACKET_L const_value_list BRACKET_R\n                         | BRACKET_L BRACKET_R\n        \n        const_value_list : const_value_list const_value\n        \n        const_value_list : const_value\n        \n        object_value : BRACE_L object_field_list BRACE_R\n                     | BRACE_L BRACE_R\n        \n        object_field_list : object_field_list object_field\n        \n        object_field_list : object_field\n        \n        object_field : name COLON value\n        \n        const_object_value : BRACE_L const_object_field_list BRACE_R\n                           | BRACE_L BRACE_R\n        \n        const_object_field_list : const_object_field_list const_object_field\n        \n        const_object_field_list : const_object_field\n        \n        const_object_field : name COLON const_value\n        \n        type : named_type\n             | list_type\n             | non_null_type\n        \n        named_type : name\n        \n        list_type : BRACKET_L type BRACKET_R\n        \n        non_null_type : named_type BANG\n                      | list_type BANG\n        '
    
_lr_action_items = {'BRACE_L':([0,7,8,9,15,16,17,18,19,20,21,22,23,24,25,26,29,30,34,35,36,40,41,43,49,50,51,52,54,60,64,67,68,72,74,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,105,106,107,108,110,114,118,119,120,122,124,125,126,127,128,129,130,131,132,136,137,138,140,143,144,145,147,],[5,5,-14,-15,5,-52,-53,-54,-55,-56,-57,-58,-59,5,5,5,-36,-38,5,5,5,5,5,5,-37,-40,5,5,5,5,-45,-39,5,-41,98,-61,-62,-63,-64,-65,-66,-67,-68,-69,-80,-78,-79,-81,-82,-83,-84,-85,98,-50,98,-87,-89,-95,133,-86,-88,-94,98,-70,-71,-72,-73,-74,-75,-76,-77,133,133,-91,-93,-100,-90,-92,-99,133,]),'QUERY':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,27,29,30,31,32,33,34,35,36,37,38,39,42,44,45,48,49,50,51,52,53,54,55,56,57,58,61,62,63,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,104,105,106,107,108,109,110,111,114,118,119,120,121,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,143,144,145,146,147,148,],[8,8,-4,18,-5,18,-14,-15,-3,18,-18,-19,18,-35,-52,-53,-54,-55,-56,-57,-58,-59,-13,-36,-38,18,-16,-17,-31,-32,-33,-34,-60,18,-9,-11,-12,18,-37,-40,-30,-29,-28,-27,-26,-25,18,-43,-7,-8,-10,-39,-24,-23,-22,-21,-41,-42,94,-6,18,-20,-44,-61,-62,-63,-64,-65,-66,-67,-68,-69,18,-80,-78,-79,-81,-82,-83,-84,-85,94,18,18,-50,94,-87,-89,18,-95,-97,94,-86,-88,-94,-96,94,-70,-71,-72,-73,-74,-75,-76,-77,94,18,-98,94,-91,-93,18,-100,-102,-90,-92,-99,-101,94,-103,]),'MUTATION':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,27,29,30,31,32,33,34,35,36,37,38,39,42,44,45,48,49,50,51,52,53,54,55,56,57,58,61,62,63,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,104,105,106,107,108,109,110,111,114,118,119,120,121,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,143,144,145,146,147,148,],[9,9,-4,19,-5,19,-14,-15,-3,19,-18,-19,19,-35,-52,-53,-54,-55,-56,-57,-58,-59,-13,-36,-38,19,-16,-17,-31,-32,-33,-34,-60,19,-9,-11,-12,19,-37,-40,-30,-29,-28,-27,-26,-25,19,-43,-7,-8,-10,-39,-24,-23,-22,-21,-41,-42,95,-6,19,-20,-44,-61,-62,-63,-64,-65,-66,-67,-68,-69,19,-80,-78,-79,-81,-82,-83,-84,-85,95,19,19,-50,95,-87,-89,19,-95,-97,95,-86,-88,-94,-96,95,-70,-71,-72,-73,-74,-75,-76,-77,95,19,-98,95,-91,-93,19,-100,-102,-90,-92,-99,-101,95,-103,]),'$end':([1,2,3,4,6,10,27,32,42,44,45,61,62,63,75,],[0,-1,-2,-4,-5,-3,-13,-16,-9,-11,-12,-7,-8,-10,-6,]),'NAME':([5,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,48,49,50,51,52,53,54,55,56,57,58,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,104,105,106,107,108,109,110,111,114,118,119,120,121,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,143,144,145,146,147,148,],[16,16,-14,-15,16,-18,-19,16,-35,-52,-53,-54,-55,-56,-57,-58,-59,-36,-38,16,-16,-17,-31,-32,-33,-34,-60,16,16,-37,-40,-30,-29,-28,-27,-26,-25,16,-43,-39,-24,-23,-22,-21,-41,-42,92,16,-20,-44,-61,-62,-63,-64,-65,-66,-67,-68,-69,16,-80,-78,-79,-81,-82,-83,-84,-85,92,16,16,-50,92,-87,-89,16,-95,-97,92,-86,-88,-94,-96,92,-70,-71,-72,-73,-74,-75,-76,-77,92,16,-98,92,-91,-93,16,-100,-102,-90,-92,-99,-101,92,-103,]),'FRAGMENT':([5,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,48,49,50,51,52,53,54,55,56,57,58,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,104,105,106,107,108,109,110,111,114,118,119,120,121,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,143,144,145,146,147,148,],[17,17,-14,-15,17,-18,-19,17,-35,-52,-53,-54,-55,-56,-57,-58,-59,-36,-38,17,-16,-17,-31,-32,-33,-34,-60,17,17,-37,-40,-30,-29,-28,-27,-26,-25,17,-43,-39,-24,-23,-22,-21,-41,-42,93,17,-20,-44,-61,-62,-63,-64,-65,-66,-67,-68,-69,17,-80,-78,-79,-81,-82,-83,-84,-85,93,17,17,-50,93,-87,-89,17,-95,-97,93,-86,-88,-94,-96,93,-70,-71,-72,-73,-74,-75,-76,-77,93,17,-98,93,-91,-93,17,-100,-102,-90,-92,-99,-101,93,-103,]),'ON':([5,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,48,49,50,51,52,53,54,55,56,57,58,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,104,105,106,107,108,109,110,111,114,118,119,120,121,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,143,144,145,146,147,148,],[20,20,-14,-15,20,-18,-19,20,-35,-52,-53,-54,-55,-56,-57,-58,-59,-36,-38,20,-16,-17,-31,-32,-33,-34,-60,20,20,-37,-40,-30,-29,-28,-27,-26,-25,20,-43,-39,-24,-23,-22,-21,-41,-42,96,20,-20,-44,-61,-62,-63,-64,-65,-66,-67,-68,-69,20,-80,-78,-79,-81,-82,-83,-84,-85,96,20,20,-50,96,-87,-89,20,-95,-97,96,-86,-88,-94,-96,96,-70,-71,-72,-73,-74,-75,-76,-77,96,20,-98,96,-91,-93,20,-100,-102,-90,-92,-99,-101,96,-103,]),'TRUE':([5,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,48,49,50,51,52,53,54,55,56,57,58,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,104,105,106,107,108,109,110,111,114,118,119,120,121,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,143,144,145,146,147,148,],[21,21,-14,-15,21,-18,-19,21,-35,-52,-53,-54,-55,-56,-57,-58,-59,-36,-38,21,-16,-17,-31,-32,-33,-34,-60,21,21,-37,-40,-30,-29,-28,-27,-26,-25,21,-43,-39,-24,-23,-22,-21,-41,-42,90,21,-20,-44,-61,-62,-63,-64,-65,-66,-67,-68,-69,21,-80,-78,-79,-81,-82,-83,-84,-85,90,21,21,-50,90,-87,-89,21,-95,-97,90,-86,-88,-94,-96,90,-70,-71,-72,-73,-74,-75,-76,-77,90,21,-98,90,-91,-93,21,-100,-102,-90,-92,-99,-101,90,-103,]),'FALSE':([5,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,48,49,50,51,52,53,54,55,56,57,58,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,104,105,106,107,108,109,110,111,114,118,119,120,121,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,143,144,145,146,147,148,],[22,22,-14,-15,22,-18,-19,22,-35,-52,-53,-54,-55,-56,-57,-58,-59,-36,-38,22,-16,-17,-31,-32,-33,-34,-60,22,22,-37,-40,-30,-29,-28,-27,-26,-25,22,-43,-39,-24,-23,-22,-21,-41,-42,91,22,-20,-44,-61,-62,-63,-64,-65,-66,-67,-68,-69,22,-80,-78,-79,-81,-82,-83,-84,-85,91,22,22,-50,91,-87,-89,22,-95,-97,91,-86,-88,-94,-96,91,-70,-71,-72,-73,-74,-75,-76,-77,91,22,-98,91,-91,-93,22,-100,-102,-90,-92,-99,-101,91,-103,]),'NULL':([5,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,48,49,50,51,52,53,54,55,56,57,58,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,104,105,106,107,108,109,110,111,114,118,119,120,121,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,143,144,145,146,147,148,],[23,23,-14,-15,23,-18,-19,23,-35,-52,-53,-54,-55,-56,-57,-58,-59,-36,-38,23,-16,-17,-31,-32,-33,-34,-60,23,23,-37,-40,-30,-29,-28,-27,-26,-25,23,-43,-39,-24,-23,-22,-21,-41,-42,89,23,-20,-44,-61,-62,-63,-64,-65,-66,-67,-68,-69,23,-80,-78,-79,-81,-82,-83,-84,-85,89,23,23,-50,89,-87,-89,23,-95,-97,89,-86,-88,-94,-96,89,-70,-71,-72,-73,-74,-75,-76,-77,89,23,-98,89,-91,-93,23,-100,-102,-90,-92,-99,-101,89,-103,]),'PAREN_L':([7,8,9,15,16,17,18,19,20,21,22,23,24,34,50,],[28,-14,-15,39,-52,-53,-54,-55,-56,-57,-58,-59,28,39,39,]),'AT':([7,8,9,15,16,17,18,19,20,21,22,23,24,25,29,30,34,35,40,49,50,51,64,67,72,],[31,-14,-15,31,-52,-53,-54,-55,-56,-57,-58,-59,31,31,31,-38,31,31,31,-37,-40,31,-45,-39,-41,]),'BRACE_R':([11,12,13,15,16,17,18,19,20,21,22,23,29,30,32,33,34,35,36,37,49,50,51,52,53,54,55,56,67,68,69,70,71,72,77,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,98,105,107,109,110,111,118,120,121,124,125,126,127,128,129,130,131,133,135,137,139,140,141,143,145,146,148,],[32,-18,-19,-35,-52,-53,-54,-55,-56,-57,-58,-59,-36,-38,-16,-17,-31,-32,-33,-34,-37,-40,-30,-29,-28,-27,-26,-25,-39,-24,-23,-22,-21,-41,-20,-61,-62,-63,-64,-65,-66,-67,-68,-69,-80,-78,-79,-81,-82,-83,-84,-85,110,-50,-87,120,-95,-97,-86,-94,-96,-70,-71,-72,-73,-74,-75,-76,-77,140,-98,-91,145,-100,-102,-90,-99,-101,-103,]),'COLON':([15,16,17,18,19,20,21,22,23,59,66,112,142,],[38,-52,-53,-54,-55,-56,-57,-58,-59,74,76,122,147,]),'BANG':([16,17,18,19,20,21,22,23,99,101,102,134,],[-52,-53,-54,-55,-56,-57,-58,-59,-107,115,116,-108,]),'EQUALS':([16,17,18,19,20,21,22,23,99,100,101,102,103,115,116,134,],[-52,-53,-54,-55,-56,-57,-58,-59,-107,114,-104,-105,-106,-109,-110,-108,]),'PAREN_R':([16,17,18,19,20,21,22,23,46,47,57,58,65,73,78,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,99,100,101,102,103,105,107,110,113,115,116,118,120,123,124,125,126,127,128,129,130,131,134,137,140,143,145,],[-52,-53,-54,-55,-56,-57,-58,-59,64,-47,72,-43,-46,-42,-44,-61,-62,-63,-64,-65,-66,-67,-68,-69,-80,-78,-79,-81,-82,-83,-84,-85,-107,-49,-104,-105,-106,-50,-87,-95,-48,-109,-110,-86,-94,-51,-70,-71,-72,-73,-74,-75,-76,-77,-108,-91,-100,-90,-99,]),'DOLLAR':([16,17,18,19,20,21,22,23,28,46,47,65,74,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,106,107,108,110,113,115,116,118,119,120,122,123,124,125,126,127,128,129,130,131,134,137,140,143,145,],[-52,-53,-54,-55,-56,-57,-58,-59,48,48,-47,-46,88,-61,-62,-63,-64,-65,-66,-67,-68,-69,-80,-78,-79,-81,-82,-83,-84,-85,88,-107,-49,-104,-105,-106,-50,88,-87,-89,-95,-48,-109,-110,-86,-88,-94,88,-51,-70,-71,-72,-73,-74,-75,-76,-77,-108,-91,-100,-90,-99,]),'BRACKET_R':([16,17,18,19,20,21,22,23,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,99,101,102,103,105,106,107,108,110,115,116,117,118,119,120,124,125,126,127,128,129,130,131,132,134,136,137,138,140,143,144,145,],[-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-80,-78,-79,-81,-82,-83,-84,-85,107,-107,-104,-105,-106,-50,118,-87,-89,-95,-109,-110,134,-86,-88,-94,-70,-71,-72,-73,-74,-75,-76,-77,137,-108,143,-91,-93,-100,-90,-92,-99,]),'INT_VALUE':([16,17,18,19,20,21,22,23,74,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,105,106,107,108,110,114,118,119,120,122,124,125,126,127,128,129,130,131,132,136,137,138,140,143,144,145,147,],[-52,-53,-54,-55,-56,-57,-58,-59,80,-61,-62,-63,-64,-65,-66,-67,-68,-69,-80,-78,-79,-81,-82,-83,-84,-85,80,-50,80,-87,-89,-95,124,-86,-88,-94,80,-70,-71,-72,-73,-74,-75,-76,-77,124,124,-91,-93,-100,-90,-92,-99,124,]),'FLOAT_VALUE':([16,17,18,19,20,21,22,23,74,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,105,106,107,108,110,114,118,119,120,122,124,125,126,127,128,129,130,131,132,136,137,138,140,143,144,145,147,],[-52,-53,-54,-55,-56,-57,-58,-59,81,-61,-62,-63,-64,-65,-66,-67,-68,-69,-80,-78,-79,-81,-82,-83,-84,-85,81,-50,81,-87,-89,-95,125,-86,-88,-94,81,-70,-71,-72,-73,-74,-75,-76,-77,125,125,-91,-93,-100,-90,-92,-99,125,]),'STRING_VALUE':([16,17,18,19,20,21,22,23,74,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,105,106,107,108,110,114,118,119,120,122,124,125,126,127,128,129,130,131,132,136,137,138,140,143,144,145,147,],[-52,-53,-54,-55,-56,-57,-58,-59,82,-61,-62,-63,-64,-65,-66,-67,-68,-69,-80,-78,-79,-81,-82,-83,-84,-85,82,-50,82,-87,-89,-95,126,-86,-88,-94,82,-70,-71,-72,-73,-74,-75,-76,-77,126,126,-91,-93,-100,-90,-92,-99,126,]),'BRACKET_L':([16,17,18,19,20,21,22,23,74,76,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,104,105,106,107,108,110,114,118,119,120,122,124,125,126,127,128,129,130,131,132,136,137,138,140,143,144,145,147,],[-52,-53,-54,-55,-56,-57,-58,-59,97,104,-61,-62,-63,-64,-65,-66,-67,-68,-69,-80,-78,-79,-81,-82,-83,-84,-85,97,104,-50,97,-87,-89,-95,132,-86,-88,-94,97,-70,-71,-72,-73,-74,-75,-76,-77,132,132,-91,-93,-100,-90,-92,-99,132,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'document':([0,],[1,]),'definition_list':([0,],[2,]),'selection_set':([0,7,15,24,25,26,34,35,36,40,41,43,51,52,54,60,68,],[3,27,37,42,44,45,53,55,56,61,62,63,69,70,71,75,77,]),'definition':([0,2,],[4,10,]),'operation_definition':([0,2,],[6,6,]),'operation_type':([0,2,],[7,7,]),'selection_list':([5,],[11,]),'selection':([5,11,],[12,33,]),'field':([5,11,],[13,13,]),'alias':([5,11,],[14,14,]),'name':([5,7,11,14,31,39,48,57,76,88,98,104,109,133,139,],[15,24,15,34,50,59,66,59,99,105,112,99,112,142,142,]),'variable_definitions':([7,24,],[25,40,]),'directives':([7,15,24,25,34,35,40,51,],[26,36,41,43,52,54,60,68,]),'directive_list':([7,15,24,25,34,35,40,51,],[29,29,29,29,29,29,29,29,]),'directive':([7,15,24,25,29,34,35,40,51,],[30,30,30,30,49,30,30,30,30,]),'arguments':([15,34,50,],[35,51,67,]),'variable_definition_list':([28,],[46,]),'variable_definition':([28,46,],[47,65,]),'argument_list':([39,],[57,]),'argument':([39,57,],[58,73,]),'value':([74,97,106,122,],[78,108,119,135,]),'variable':([74,97,106,122,],[79,79,79,79,]),'null_value':([74,97,106,114,122,132,136,147,],[83,83,83,127,83,127,127,127,]),'boolean_value':([74,97,106,114,122,132,136,147,],[84,84,84,128,84,128,128,128,]),'enum_value':([74,97,106,114,122,132,136,147,],[85,85,85,129,85,129,129,129,]),'list_value':([74,97,106,122,],[86,86,86,86,]),'object_value':([74,97,106,122,],[87,87,87,87,]),'type':([76,104,],[100,117,]),'named_type':([76,104,],[101,101,]),'list_type':([76,104,],[102,102,]),'non_null_type':([76,104,],[103,103,]),'value_list':([97,],[106,]),'object_field_list':([98,],[109,]),'object_field':([98,109,],[111,121,]),'default_value':([100,],[113,]),'const_value':([114,132,136,147,],[123,138,144,148,]),'const_list_value':([114,132,136,147,],[130,130,130,130,]),'const_object_value':([114,132,136,147,],[131,131,131,131,]),'const_value_list':([132,],[136,]),'const_object_field_list':([133,],[139,]),'const_object_field':([133,139,],[141,146,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> document","S'",1,None,None,None),
  ('document -> definition_list','document',1,'p_document','parser.py',42),
  ('document -> selection_set','document',1,'p_document_shorthand','parser.py',48),
  ('definition_list -> definition_list definition','definition_list',2,'p_definition_list','parser.py',72),
  ('definition_list -> definition','definition_list',1,'p_definition_list_single','parser.py',78),
  ('definition -> operation_definition','definition',1,'p_definition','parser.py',84),
  ('operation_definition -> operation_type name variable_definitions directives selection_set','operation_definition',5,'p_operation_definition1','parser.py',98),
  ('operation_definition -> operation_type name variable_definitions selection_set','operation_definition',4,'p_operation_definition2','parser.py',109),
  ('operation_definition -> operation_type name directives selection_set','operation_definition',4,'p_operation_definition3','parser.py',119),
  ('operation_definition -> operation_type name selection_set','operation_definition',3,'p_operation_definition4','parser.py',129),
  ('operation_definition -> operation_type variable_definitions directives selection_set','operation_definition',4,'p_operation_definition5','parser.py',135),
  ('operation_definition -> operation_type variable_definitions selection_set','operation_definition',3,'p_operation_definition6','parser.py',145),
  ('operation_definition -> operation_type directives selection_set','operation_definition',3,'p_operation_definition7','parser.py',154),
  ('operation_definition -> operation_type selection_set','operation_definition',2,'p_operation_definition8','parser.py',163),
  ('operation_type -> QUERY','operation_type',1,'p_operation_type','parser.py',169),
  ('operation_type -> MUTATION','operation_type',1,'p_operation_type','parser.py',170),
  ('selection_set -> BRACE_L selection_list BRACE_R','selection_set',3,'p_selection_set','parser.py',176),
  ('selection_list -> selection_list selection','selection_list',2,'p_selection_list','parser.py',182),
  ('selection_list -> selection','selection_list',1,'p_selection_list_single','parser.py',188),
  ('selection -> field','selection',1,'p_selection','parser.py',194),
  ('field -> alias name arguments directives selection_set','field',5,'p_field_all','parser.py',203),
  ('field -> name arguments directives selection_set','field',4,'p_field_optional1_1','parser.py',210),
  ('field -> alias name directives selection_set','field',4,'p_field_optional1_2','parser.py',217),
  ('field -> alias name arguments selection_set','field',4,'p_field_optional1_3','parser.py',223),
  ('field -> alias name arguments directives','field',4,'p_field_optional1_4','parser.py',229),
  ('field -> name directives selection_set','field',3,'p_field_optional2_1','parser.py',235),
  ('field -> name arguments selection_set','field',3,'p_field_optional2_2','parser.py',241),
  ('field -> name arguments directives','field',3,'p_field_optional2_3','parser.py',247),
  ('field -> alias name selection_set','field',3,'p_field_optional2_4','parser.py',253),
  ('field -> alias name directives','field',3,'p_field_optional2_5','parser.py',259),
  ('field -> alias name arguments','field',3,'p_field_optional2_6','parser.py',265),
  ('field -> alias name','field',2,'p_field_optional3_1','parser.py',271),
  ('field -> name arguments','field',2,'p_field_optional3_2','parser.py',277),
  ('field -> name directives','field',2,'p_field_optional3_3','parser.py',283),
  ('field -> name selection_set','field',2,'p_field_optional3_4','parser.py',289),
  ('field -> name','field',1,'p_field_optional4','parser.py',295),
  ('directives -> directive_list','directives',1,'p_directives','parser.py',360),
  ('directive_list -> directive_list directive','directive_list',2,'p_directive_list','parser.py',366),
  ('directive_list -> directive','directive_list',1,'p_directive_list_single','parser.py',372),
  ('directive -> AT name arguments','directive',3,'p_directive','parser.py',378),
  ('directive -> AT name','directive',2,'p_directive','parser.py',379),
  ('arguments -> PAREN_L argument_list PAREN_R','arguments',3,'p_arguments','parser.py',386),
  ('argument_list -> argument_list argument','argument_list',2,'p_argument_list','parser.py',392),
  ('argument_list -> argument','argument_list',1,'p_argument_list_single','parser.py',398),
  ('argument -> name COLON value','argument',3,'p_argument','parser.py',404),
  ('variable_definitions -> PAREN_L variable_definition_list PAREN_R','variable_definitions',3,'p_variable_definitions','parser.py',410),
  ('variable_definition_list -> variable_definition_list variable_definition','variable_definition_list',2,'p_variable_definition_list','parser.py',416),
  ('variable_definition_list -> variable_definition','variable_definition_list',1,'p_variable_definition_list_single','parser.py',422),
  ('variable_definition -> DOLLAR name COLON type default_value','variable_definition',5,'p_variable_definition1','parser.py',428),
  ('variable_definition -> DOLLAR name COLON type','variable_definition',4,'p_variable_definition2','parser.py',434),
  ('variable -> DOLLAR name','variable',2,'p_variable','parser.py',440),
  ('default_value -> EQUALS const_value','default_value',2,'p_default_value','parser.py',446),
  ('name -> NAME','name',1,'p_name','parser.py',452),
  ('name -> FRAGMENT','name',1,'p_name','parser.py',453),
  ('name -> QUERY','name',1,'p_name','parser.py',454),
  ('name -> MUTATION','name',1,'p_name','parser.py',455),
  ('name -> ON','name',1,'p_name','parser.py',456),
  ('name -> TRUE','name',1,'p_name','parser.py',457),
  ('name -> FALSE','name',1,'p_name','parser.py',458),
  ('name -> NULL','name',1,'p_name','parser.py',459),
  ('alias -> name COLON','alias',2,'p_alias','parser.py',465),
  ('value -> variable','value',1,'p_value','parser.py',471),
  ('value -> INT_VALUE','value',1,'p_value','parser.py',472),
  ('value -> FLOAT_VALUE','value',1,'p_value','parser.py',473),
  ('value -> STRING_VALUE','value',1,'p_value','parser.py',474),
  ('value -> null_value','value',1,'p_value','parser.py',475),
  ('value -> boolean_value','value',1,'p_value','parser.py',476),
  ('value -> enum_value','value',1,'p_value','parser.py',477),
  ('value -> list_value','value',1,'p_value','parser.py',478),
  ('value -> object_value','value',1,'p_value','parser.py',479),
  ('const_value -> INT_VALUE','const_value',1,'p_const_value','parser.py',485),
  ('const_value -> FLOAT_VALUE','const_value',1,'p_const_value','parser.py',486),
  ('const_value -> STRING_VALUE','const_value',1,'p_const_value','parser.py',487),
  ('const_value -> null_value','const_value',1,'p_const_value','parser.py',488),
  ('const_value -> boolean_value','const_value',1,'p_const_value','parser.py',489),
  ('const_value -> enum_value','const_value',1,'p_const_value','parser.py',490),
  ('const_value -> const_list_value','const_value',1,'p_const_value','parser.py',491),
  ('const_value -> const_object_value','const_value',1,'p_const_value','parser.py',492),
  ('boolean_value -> TRUE','boolean_value',1,'p_boolean_value','parser.py',498),
  ('boolean_value -> FALSE','boolean_value',1,'p_boolean_value','parser.py',499),
  ('null_value -> NULL','null_value',1,'p_null_value','parser.py',505),
  ('enum_value -> NAME','enum_value',1,'p_enum_value','parser.py',511),
  ('enum_value -> FRAGMENT','enum_value',1,'p_enum_value','parser.py',512),
  ('enum_value -> QUERY','enum_value',1,'p_enum_value','parser.py',513),
  ('enum_value -> MUTATION','enum_value',1,'p_enum_value','parser.py',514),
  ('enum_value -> ON','enum_value',1,'p_enum_value','parser.py',515),
  ('list_value -> BRACKET_L value_list BRACKET_R','list_value',3,'p_list_value','parser.py',521),
  ('list_value -> BRACKET_L BRACKET_R','list_value',2,'p_list_value','parser.py',522),
  ('value_list -> value_list value','value_list',2,'p_value_list','parser.py',528),
  ('value_list -> value','value_list',1,'p_value_list_single','parser.py',534),
  ('const_list_value -> BRACKET_L const_value_list BRACKET_R','const_list_value',3,'p_const_list_value','parser.py',540),
  ('const_list_value -> BRACKET_L BRACKET_R','const_list_value',2,'p_const_list_value','parser.py',541),
  ('const_value_list -> const_value_list const_value','const_value_list',2,'p_const_value_list','parser.py',547),
  ('const_value_list -> const_value','const_value_list',1,'p_const_value_list_single','parser.py',553),
  ('object_value -> BRACE_L object_field_list BRACE_R','object_value',3,'p_object_value','parser.py',559),
  ('object_value -> BRACE_L BRACE_R','object_value',2,'p_object_value','parser.py',560),
  ('object_field_list -> object_field_list object_field','object_field_list',2,'p_object_field_list','parser.py',566),
  ('object_field_list -> object_field','object_field_list',1,'p_object_field_list_single','parser.py',574),
  ('object_field -> name COLON value','object_field',3,'p_object_field','parser.py',580),
  ('const_object_value -> BRACE_L const_object_field_list BRACE_R','const_object_value',3,'p_const_object_value','parser.py',586),
  ('const_object_value -> BRACE_L BRACE_R','const_object_value',2,'p_const_object_value','parser.py',587),
  ('const_object_field_list -> const_object_field_list const_object_field','const_object_field_list',2,'p_const_object_field_list','parser.py',593),
  ('const_object_field_list -> const_object_field','const_object_field_list',1,'p_const_object_field_list_single','parser.py',601),
  ('const_object_field -> name COLON const_value','const_object_field',3,'p_const_object_field','parser.py',607),
  ('type -> named_type','type',1,'p_type','parser.py',613),
  ('type -> list_type','type',1,'p_type','parser.py',614),
  ('type -> non_null_type','type',1,'p_type','parser.py',615),
  ('named_type -> name','named_type',1,'p_named_type','parser.py',621),
  ('list_type -> BRACKET_L type BRACKET_R','list_type',3,'p_list_type','parser.py',627),
  ('non_null_type -> named_type BANG','non_null_type',2,'p_non_null_type','parser.py',633),
  ('non_null_type -> list_type BANG','non_null_type',2,'p_non_null_type','parser.py',634),
]