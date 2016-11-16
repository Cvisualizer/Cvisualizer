let astJson;

function test(){
	var req = new XMLHttpRequest();

	req.onreadystatechange = function(){
		if(req.readyState==4){
			if(req.status==200){
				var ast = eval('(' + req.responseText + ')');
				console.log('success');
				console.log(ast);
				astJson = ast;
			}
		}
	}
	req.open('GET','http://192.168.56.101:8880');
	req.send(null);
}

let VMStack = new Array();

function VMcode(code,line,address,frame){
	this.code = code;
	this.line = line;
	this.address = address;
	this.frame = frmae;
}

let symbolType = {
	GVAL : 0,
	FUNC : 1,
	LVAL : 2,
	PARAM : 3
}

let localTable = new Array();
function localSymbol(kind,name,type,address,location){
	this.kind = kind;
	this.name = name;
	this.type = type;
	this.address = address;
	this.location = location;
}

let globalTable = new Array();
function globalSymbol(kind,name,type,address,location,param,){
	this.kind = kind;
	this.name = name;
	this.type = type;
	this.address = address;
	this.location = location;
	this.param = param;
}

let source_ast = astJson.child

function setGlobalSymbol(){
	for(node of source_ast){
		switch(node.type){
			case "FUNCTION_DECL":
				let param_num = 0;
				params = node.child;
				for(param of params){
					if(param.type=="ParamVarDecl"){
						param_num += 1;
					}
				}
				globalTable.push(new globalSymbol(node.type,node.name,node.))
		}

	}
}