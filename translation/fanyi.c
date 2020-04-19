#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<pthread.h>
#include<errno.h>
typedef struct User
{
	char *str;
	FILE *fp;
}STR;

void UserError(char *str);//error
void *UserStr(STR *str);//普通翻译
void *UserLog(char *str);//翻译列表
void *paraStr(STR *str);//翻译命令报错信息

int
main(int argc,char *argv[])
{
	FILE *fp;
	STR *str;
	pthread_t pid;
	fp = fopen("Dowm.txt","w");
	int number;
	char Ustr;
	str->str = malloc(sizeof(char));
	if(fp == NULL)
	{
		printf("errno");
		return -1;
	}
	str->fp = fp;
	if(!strcmp(argv[1],"-s"))
	{
		printf("if");
		//翻译命令报错信息
		str->str = argv[2];
		number = pthread_create(&pid,NULL,(void *)paraStr,str);
//		UserLog(str->str);
		if(number != 0)
		{
			UserError("create");
			return 0;
		}
	pthread_join(pid,NULL);
	exit(0);
	}

	if(!strcmp(argv[1],"-l"))
	{
		
	}
	if(strcmp(argv[1] > 65,)
	{
		str->str = argv[1];
		UserStr(str);
	}
	fclose(fp);
	return 0;
} 
void *
UserStr(STR *str)
	//stdin translation
{
	puts(str->str);
	UserLog(str->str);
	fputs(str->str,str->fp);
	//fputc(' ',str->fp);
		return NULL;
}
void *
paraStr(STR *str)
	//paraStr translation
{
	puts(str->str);
	UserLog(str->str);
	//strcat(str->str,"> /usr/local/src/fanyi/.fanyi.txt");
	strcat(str->str,"> men.txt");
	system(str->str);
	return NULL;
}
void *
UserLog(char *str)
	//用户日志
{
	FILE *fp;
	fp = fopen("log.txt","a+");
	if(fp == NULL)
		UserError("opne file for log");
	fputs(str,fp);
	fputc('\n',fp);
	puts("wire");
	fclose(fp);
	return NULL;
}
void 
UserError(char *str)
	//errno printf
{
	perror(str);
	exit(1);
}
