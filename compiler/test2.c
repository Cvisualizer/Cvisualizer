int main(){
	int a = 1;
	int b,d = 0 + 1;
	char *e = "abc";
	while(b)a++;
	if(a<b){
		b = a * b;
	} 
	else if(b==a){
		b = a + b + b;
	} 
	else {
		b = a - b;
	}
	return 1;
}