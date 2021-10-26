#include <stdio.h>
#include <math.h>


void main()
{
  float x = 2;
  if (x >= 2 && x <3){
      while (x < 3){
          float variable_1 = cos(x + 1 / cos(pow(x,-2))) / sin(x + 1 / cos(pow(x,-2)));
          printf("Результат першого прикладу (при x = %.1f) є %.2f \n",x,variable_1);
          x+=0.2;
         
      }
      printf("\n");
  }
 
  if (x >= 3 && x <4){
       while (x < 4){
          float variable_2 = log10(log10(x) + log(x)/log(3));
          printf("Результат другого прикладу (при x = %.1f) є %.2f \n",x,variable_2);
          x+=0.2;
         
      }
      printf("\n");
  }
  
  if (x >= 4 && x<=5){
       while (x <= 5){
          float variable_3 = cos(5*pow(x,2));
          printf("Результат третього прикладу (при x = %.1f) є %.2f \n",x,variable_3);
          x+=0.2;
          
      }
  }

}
