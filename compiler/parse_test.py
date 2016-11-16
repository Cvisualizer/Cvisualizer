from clang.cindex import Index
from clang.cindex import Config

def print_node(node,iter=0):
	print "-" * iter + "%s:%s" %(node.kind.name,node.location.line)
	print "-" * iter + "%s" %([x.spelling for x in node.get_tokens()])
	if node.kind.name == "FUNCTION_DECL":
		for arg in node.get_arguments():
			print arg.spelling
	for child in node.get_children():
		print_node(child,iter+1)

index = Index.create()
source = index.parse('test.c')
print_node(source.cursor)

