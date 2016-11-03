function test(){
	var req = new XMLHttpRequest();

	req.onreadystatechange = function(){
		if(req.readyState==4){
			if(req.status==200){
				var ast = eval('(' + req.responseText + ')');
				console.log('sucess');
				console.log(ast);
				return ast;
			}
		}
	}
	req.open('GET','http://192.168.56.101:8880');
	req.send(null);
}

