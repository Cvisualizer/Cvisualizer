from clang.cindex import Index
from clang.cindex import Config
import json

def get_node_info(node):
	return {
		"name":node.spelling,
		"type":node.kind.name,
		"is_definition":node.is_definition(),
		"location":{
			"line":node.location.line,
			"column":node.location.column
		},
		"child":[get_node_info(child) for child in node.get_children()]
	}

def parse()

def main():
	ast = {}
	index = Index.create()
	source = index.parse('test.c')
	ast = get_node_info(source.cursor)
	ast_json = json.dumps(ast)
	print >> open('test.json','w') ,ast_json

if __name__ == '__main__':
	main()