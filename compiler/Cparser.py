#coding=utf-8
from clang.cindex import Index
from clang.cindex import Config
from collections import namedtuple


code = namedtuple(
	"program_code",
	["assign",
	"refer",
	"lvardecl",
	"gvardecl",
	"funcdecl",
	"structdecl",
	"mov",
	"ifjump",
	"jump"
	"push",
	"calc",
	"comp",
	"call",
	"return",
	"halt"])

virtual_code = code(range(9))

class Program():
	def __init__(self,number,args):
		self.number = number
		self.args = args


class SymbolTable():
	
	def __init__(self):
		self.global_symbol = []
		self.local_symbol = []

	def add_global_symbol(self,node):
		self.global_symbol.append(node)

	def add_local_symbol(self,node):
		self.local_symbol.append(node)

	def clear_local_symbol(self,node):
		del self.localSymbol__

class StackVirtualMachine():
	def __init__(self):
		self.program_stack = {}
		self.program_couter = 0
		self.program_code = code(range(9))
		self.labels = {}
		self.frame_register = 0
		self.stack_pointer = 0
		now_function = ""
		num_labels = 0
		now_label = ""

	def stack_code(self,label,code):
		self.program_stack[label].append(code)

	def add_label(self,label):
		self.labels[label] = []

	def assert_next_node(node):
		for child in node.get_children():
			assert_node(child)

	def assert_node(node):
		if "STMT" in node.kind.name[-4:]:
			assert_stmt(node)
		elif "OPERATOR" in node.kind.name[-8:]:
			assert_operator(node)
		elif "EXPR" in node.kind.name[-4]:
			assert_expr(node)
		elif "DECL" == node.kind.name[-4:]:
			assert_decl(node)
		else:
			assert_next_node(node)

	def assert_function(self,node): 
		"""
		１．スタックに引数に積む
		２．戻りアドレスを積む
		３．ローカル変数を積む
		"""
		num_labels = 0
		self.labels[node.spelling] = {}
		self.labels[node.spelling]["line"] = node.location.line
		now_function = node.spelling 
		now_label = now_function
		assert_next_node(node)
		return 

	def assert_stmt(self,node):
		"""
		文を評価
		制御構造を決定する
		statementに出会ったときに呼び出される
		"""
		if node.kind.name == "IF_STMT":
			assert_node(node.get_children()[0])
			stack_code(now_label,[program_code.jre,now_function+"_IF_"+str(num_labels)])
			now_label = now_function+"_IF_"+str(num_labels)
			add_label(now_label,[])
			for child in node.get_children()[1:]:
				assert_node(child)
		elif node.kind.name == "FOR_STMT":
			for op in node.get_children()[:3]:
				assert_node(op)
			stack_code(now_label,[program_code.jre,now_function+"_FOR_"+str(num_labels)])
			now_label = now_function+"_FOR_"+str(num_labels)
			for child in node.get_children()[4:]:
				assert_node(child)
		elif node.kind.name == "WHILE_STMT":
			assert_node(node.get_children()[0])
			stack_code(now_label,[program_code.jre,now_function+"_WHILE_"+str(num_labels)])
			now_label = now_function+"_WHILE_"+str(num_labels)
			for child in node.get_children()[1:]:
				assert_node(child)
		elif node.kind.name == "DECL_STMT":
			assert_next_node(node)
		elif node.kind.name == "COMPOUND_STMT":
			assert_next_node(node)
		return


	def assert_operator(self,node):
		"""
		式単体を評価
		"""
		assert_next_node(node)
		if node.kind.name == "BINARY_OPERATOR":
			stack_code(now_label,[program_code.calc,node.get_tokens()[1]])
		elif node.kind.name == "UARY_OPERATOR":
			stack_code(now_label,[program_code.calc,node.get_tokens()[1]])

	def assert_expr(self,node):
		if node.kind.name == "DECL_REF_EXPR":
			stack_code(now_label,[program_code.push,"%"+node.get_tokens()[0]])
		elif node.kind.name == "UNEXPOSED_EXPR":
			assert_next_node(node)
		elif node.kind.name == "MEMBER_REF_EXPR":
			assert_next_node(node)
		elif node.kind.name == "CSTYLE_CAST_EXPR":
			assert_next_node(node)
		return

	def assert_decl(self,node):
		if node.kind.name == "VAR_DECL":
			stack_code(program_code.var_decl,["%"+node.get_tokens()[1]])
		elif node.kind.name == "FUNCTION_DECL":
			stack_code(program_code.functdecl,["%"+node.get_tokens()[1],[x.spelling for x in node.get_params()])
		elif node.kind.name == "STRUCT_DECL":


	def assert_literal_node(self,node):
		stack_code(now_label,[program_code.push,node.get_tokens()[0]])
		return


def main():
	stable = SymbolTable()
	source = index.parse('test.c')
	ast = get_node_info(source.cursor)
	#グローバル変数を登録
	for gsymbol in ast.get_children():
		self.add_global_symbol(gsymbol)
	vm = StackVirtualMachine()
	#関数を評価する
	for node in gsymbol:
		if node.kind.name == "FUNCTION_DECL":
			if node.spelling == "main":
				vm.stack_code("main","start")
			vm.assert_function(node)


				