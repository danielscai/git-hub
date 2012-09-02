#import <Foundation/Foundation.h>

@interface Triangle:NSObject 
{
  ShapeColor  fillColor;
  ShapeReact  bounds;
}


-(void) setFillColor:(ShapeColor) fillColor;
-(void) setBounds:(ShapeRect) bounds;

-(void) draw;

@end 

@implementatin Trigangle
-(void) setFillColor:(ShapeColor)c
{
  fillColor=c;
}

-(void) setBounds:(ShapeRect) b
{
  bounds=b;
}

-(void) draw
{
  NSLog(@"drawing a triangle at (%d %d %d %d) in %@",
    bounds.x, bounds,y,
    bounds.width, bounds height,
    colorName(fillcolor));
}

@end 





