#include <stdio.h>
int
increment_counter ()
{
  static int counter = 0;
  return ++counter;
}
int main()
{
  int x = 20, y = 35;
  x = y++ + x++;
  y = ++y + ++x;
  double d = 5; float f = 8 / 6; int i = 12; unsigned int ui = 2;
  unsigned int z = -10;
  /*
  printf("%d,%d", x, y);
  int a = 3, b = 4, c, i, d;  c = ++a; d = b++;  
  i = 1;
  c = a * b + ++a + 4;
  i = ++i +1;
  printf("i: %d\n", i);
  
  
  printf("a: %d\n", a);
  printf("b: %d\n", b);
  printf("c: %d\n", c);
  
  for(i = 0; i < 1; i++) {
     b =b++ + ++b;
    printf("updated b: %d\n", b);
  }
  
    for(i = 0; i < 10; i++) {
    printf("increment: %d\n", increment_counter ());
  } */
  printf("%u\n", (int)(d / f) + i * (ui - i));
  i = d / f + i * (ui - i);
  
  
  return 0;
}

