#import <Foundation/Foundation.h>

@interface TTtest:NSObject
{
  int a;
  char b;
}
-(void) show;
@end

@implementation TTtest
-(void)init 
{
  NSLog(@"In initialize function %s","hello,world!");
}
-(void)show
{
  NSLog(@"a is %s","hello");
}

@end

int main(int argc,const char *argv[])
{
  TTtest *hi=[TTtest new];
  [hi show];
}
