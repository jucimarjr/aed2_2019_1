#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int t[8][8],a[8],b[8];
void imprime(){
 int i,j;
 for(i=0;i<8;i++){ 

   for(j=0;j<8;j++){ 

     printf("%3d",t[i][j]);} 

    printf("\n"); 

   }
}
int cavalo(int i, int x, int y){
 int u,v,k,q; 
 if(i==65){ imprime(); return 1;}
 //executa movimentos
 for(k=0;k<8;k++){
  u = x + a[k];  v = y + b[k];
  //testa limites do tabuleiro
  if( (u>=0 && u<=7) && (v>=0 && v<=7)){
   if(t[u][v]==0){ //posicao livre
    t[u][v]=i; //registre o movimento
    q = cavalo(i+1,u,v);
    if(q==0) t[u][v]=0; //se não alcançou todos, desfaça 

    else return 1; // se alcançou todos, retorne 1
   }
  }
 }
 return 0;
}
int main(){
 int cont;
 //inicializa os deslocamentos dos movimentos
 a[0]=2;a[1]=1;a[2]=-1;a[3]=-2; 
 b[0]=1;b[1]=2;b[2]=2;b[3]=1;
 
 a[4]=-2;a[5]=-1;a[6]=1;a[7]=2;
 b[4]=-1;b[5]=-2;b[6]=-2;b[7]=-1; 
 memset(t,0,sizeof(t));
 cont =1;
 t[0][0]=1;
 cavalo(2,0,0);
 