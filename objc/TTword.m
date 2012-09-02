
#import <Foundation/Foundation.h>

int main( int argc, const char *argv[])
{
  if (argc==1){
    NSLog(@"you ned to provide a file name");
    return (1);
  }

  FILE *wordfile=fopen(argv[1],"r");
  char word[100];
  
  while(fgets(word,100,wordfile)){
    word[strlen(word)-1]='\0';
    NSLog(@"%s is %d character long",
      word,strlen(word));
  }

  fclose(wordfile);
  return (0);
}
