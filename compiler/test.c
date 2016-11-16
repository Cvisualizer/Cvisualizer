struct test {
	int foot;
	char *name;
	struct test *next;
};



int hogehoge(int hoge,int piyo);

int main(){
	struct test *sample;
	for(int i=0;i<100;i++){
		sample->foot = hogehoge(i,i);
		sample->name = "takashi";
		sample->next = (struct test *)malloc(sizeof(struct test));
		sample = sample->next;
	}
}

int hogehoge(int hoge,int piyo){
	return hoge + piyo;
}