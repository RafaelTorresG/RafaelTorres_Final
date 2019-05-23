#include <iostream>
#include <math.h>

int main()
{
 float q=2;
 float m=7294.29;
 float dt=0.1;
 float k=q*dt/m;
 
 float X[100];
 float X_old[100];   
 float X_new[100];
 X[0]=1;
 
 float Vx[100];
 Vx[0]=0;
    
 float Y[100];
 float Y_old[100];   
 float Y_new[100];
 Y[0]=0;
  
 float Vy[100];
 Vy[0]=1;   
    
 float Ex[100];
 float Ey[100];
 
 for(int t=0; t<100; t++)
 {
  if(t<30||t>70)
  {
   Ex[t]=0;
   Ey[t]=0;
  }
  else
  {
   Ex[t]=0;
   Ey[t]=3;
  }
 }

     
 for(int t=1; t<100; t++)
 {
  Vx[t]=k*Ex[t];
  Vy[t]=k*Ey[t];
     
  X[t]=k*Vx[t]+X[t-1];
  Y[t]=k*Vy[t]+Y[t-1];
 }
 
 for(int i=0; i<100; i++)
 {
  float t=i*0.1;
  std::cout<<t<<","<<X[i]<<","<<Y[i]<<std::endl;
 }

 return 0;
}
