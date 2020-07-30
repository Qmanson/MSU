int NegitiveSwitch = 1;
float Rotate = PI/4;
boolean Once=true;
float x = 1;
float N = 2;
float M = 2;
float dis=8;
int a=8;
int var = 0;
boolean R= true;
boolean G= false;
boolean B= false;
boolean Robot=false;
boolean RandomON = false;
float sim = 8;

int r =0;
int g=0;
int b=0;

float Distance =0;
void setup() {
  size(1600, 1000);
}
boolean Start= true;


void mouseClicked() 
  {
     if(NegitiveSwitch >0)
    {
      Start = false;
      NegitiveSwitch*=-1;
    }else
    {
      Start = true;
      NegitiveSwitch*=-1;
    }
  }
void keyPressed()
{
  if(key == 'r')
  {
        R=true;
        G=false;
        B=false;
  }
  if(key == 'g')
  {
        G=true;
        R=false;
        B=false;
  }
  if(key == 'b')
  {
        G=false;
        R=false;
        B=true;
  }
  if(keyCode == SHIFT)
  {
        if(RandomON){
          var+=50;
          RandomON= false;
        }else{
           var-=50;
          RandomON=true;
        }
  }
  if(keyCode == UP )
  {
      dis+=5;
      
  }
  if(keyCode == DOWN)
  {
      dis-=5;
    
  }
  if(keyCode == LEFT )
  {
      dis+=0.05;
      
  }
  if(keyCode == RIGHT)
  {
      dis-=0.05;
    
  }
  
  if(key == '0')
  {
      a+=5;
  }
   if(key == 'q')
  {
      N=30;
      M=40;
  }
  if(key == '9')
  {
      a-=5;
  }
   if(key == '-')
  {
      if(Robot){
        Robot = false;
      }else{
        Robot = true;
      }
  }
  
  if(key == ' '){
    if(NegitiveSwitch >0)
    {
      Start = false;
      NegitiveSwitch*=-1;
    }else
    {
      Start = true;
      NegitiveSwitch*=-1;
    }
  }
}
  

void draw() 
{
  if(Start) 
  {     
    
    rect(1500,10,20,abs(a));
    float NUM = random(a)+(a/2);
        for(int i =0;i<NUM;i++){
             fill(255,255,255);
             circle(random(width),random(height),random(5));
        }
        String s = "ANGLE: " + (int)Rotate + " R: " +r + " G: " +g + " B: " +b + " N: " + N;
         fill(3*abs(var));
         rect(100,25,200,30);
         fill(255);
         text(s,100,50);
         if(R){
             fill(r,g,b);
             r++;
             if(r>=255){
               r=50;
             }  
         }
         if(G){
             fill(r,g,b);
             g++;
             if(g>=255){
               g=50;
             } 
         }
         if(B){
             fill(r,g,b);
             b++;
             if(b>=255){
               b=50;
             } 
         }
         
                 
         if(abs(Rotate) >2*PI){
           Rotate = 0;
         }
         Distance = sqrt(N*N+M*M);
         circle(N*cos(Rotate)+width/2,M*sin(Rotate)+height/2, 60*(Distance/100));
         if(Robot){
           sim+=0.01;
           if(sim ==0){
               sim=1;
           }
           
           print(sim,"_____");
           rect(10,10,20,abs(sim));
          
           Rotate += (PI/(sim));
           //was random(10) for N&M 
           if(RandomON)
           {
             N+=random(100)/sim;
             M+=random(100)/sim;
           }else
           {
             N+=10/sim;
             M+=10/sim;
           }
           float Rand1 = random(500);
           if(abs(N)>1000 || abs(sim) > 100){
              N=30;
              M=40;
             sim=3;
           }
           if(Rand1<(2-(sim)))
           {
             sim+=(sim+3);
           }
           else if(Rand1<(2+sim))
           {
               sim-=(sim+2);
           }else if(Rand1<3){
               sim*=-1;
           }
         }
         print(dis,"_____");
         if(dis == 0){dis=0;}
         else{
           //was random(10) for N&M 
           rect(10,10,20,abs(3-dis));
           Rotate += (PI/(dis));
           //was random(10) for N&M 
           if(RandomON){
             N+=random(10)/dis;
             M+=random(10)/dis;
           }else{
             N+=10/dis;
             M+=10/dis;
           }
           
         }
         
        
   }
}
