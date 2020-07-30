boolean first = false;
float firsty, firstx= 0;
ArrayList<Circle> set = new ArrayList<Circle>();
int amp = 63;
float damp = 0.005f;
float wavelen = 15;
float move = 0;
float moverate = 3;
float size = 150;
int count = 0;
int freq = 5;
int red = 240;
int green = 240;
int blue = 240;
boolean colorOn = false;
boolean waveDetails = true;
boolean waveDetailOn = false;
boolean backgroundColor = true;
boolean editmode = false;
boolean pointGraph = false;
int oscillatRGB = 0;
//0 = 000
//1 = 001
//2 = 010
//3 = 011
//4 = 100
//5 = 101
//6 = 110
//7 = 111
int hue  = 255;
//Wave Detail Location
int[] WDL = {1450,1495,60,85};
int[] denL = {110, 40, 50 , 25};
int[] AL =  {185, 40, 50 , 25};
int[] DL = {265, 40, 50 , 25};
int[] WLL = {360, 40, 50 , 25};
int[] SL = {465, 40, 50 , 25};
int[] SiL = {40, 40, 50, 25};
int[] backgroundColors = {240, 240, 240};
int[] waveColors = {0, 115, 0};
boolean[] DADWSS = {false,false,false,false,false,false};
int[][] detailLoc = {denL, AL, DL, WLL, SL, SiL};
int detailSlider = 0;
boolean[] RGB = {false, true, false};
boolean start = true;
int[] lineloc = {0,0,0,0}; 

public void setup() {
  size(1600,1000);
  frameRate(30);
}

public void mouseMovement(){
  if(backgroundColor)
  {
    backgroundColors[0] = red;
    backgroundColors[1] = green;
    backgroundColors[2] = blue;
    
  }
  else
  {
    waveColors[0] = red;
    waveColors[1] = green;
    waveColors[2] = blue; 
  }
  if(mouseX >1500 && mouseX< 1575 && mouseY > 25 && mouseY <255+52)
  {
    if(mouseY > 49)
    {
      if(colorOn)
      {
        if(mouseX< 1525)
        {
          red = mouseY-49;
        }
        else if(mouseX >1525 && mouseX< 1550)
        {
          green = mouseY-49;
        }
        else if(mouseX >1550)
        {
          blue = mouseY-49;
        }
      }
      else
      {
        if(mouseX>1505 && mouseX<1525)
        {
          backgroundColor = false;
          red = waveColors[0];
          green = waveColors[1];
          blue = waveColors[2];
        }
        if(mouseX>1540 && mouseX<1560)
        {
          backgroundColor = true;
          red = backgroundColors[0];
          green = backgroundColors[1];
          blue = backgroundColors[2];
        }
      }
    }
    else{
      if(!colorOn)
      {
        if(mouseX<1525)
        {
          oscillatRGB = colorSwitch(0);
        }
        else if(mouseX<1550)
        {
          oscillatRGB = colorSwitch(1);
        }
        else
        {
          oscillatRGB = colorSwitch(2);
        }
      }
    }
  }
  else if(mouseX >1450 && mouseX< 1450+45 && mouseY > 25 && mouseY < 50)
  {
    colorOn = !(colorOn);
  }
  else if(mouseX>1412 && mouseX < 1437 && mouseY > 60 && mouseY<90)
  {
    editmode = !(editmode);
  }
  else if(mouseX > WDL[0] && mouseX< WDL[1] && mouseY > WDL[2] && mouseY < WDL[3])
  {
    waveDetails = !(waveDetails);
    DADWSS[0] = false;
    DADWSS[1] = false;
    DADWSS[2] = false;
    DADWSS[3] = false;
    DADWSS[4] = false;
    DADWSS[5] = false;
    
  }
  else if(waveDetails)
  {
    if(waveDetailOn && mouseX > 560 && mouseX<760 && mouseY <60 && mouseY > 35)
    {
        detailSlider = mouseX-560; 
    }
    else if(mouseX>800 && mouseX<810 && mouseY<15)
    {
      pointGraph = !(pointGraph);
    }
    
    else if(mouseX > denL[0] && mouseX< denL[0]+denL[2] && mouseY > denL[1] && mouseY < denL[1] + denL[3])
    {
        DADWSS[0] = !(DADWSS[0]);
        detailSlider = freq*10;
        DADWSS[1] = false;
        DADWSS[2] = false;
        DADWSS[3] = false;
        DADWSS[4] = false;
        DADWSS[5] = false;
    }
    else if(mouseX > AL[0] && mouseX< AL[0]+AL[2] && mouseY > AL[1] && mouseY < AL[1] + AL[3])
    {
        DADWSS[1] = !(DADWSS[1]);
        detailSlider = amp*2;
        DADWSS[0] = false;
        DADWSS[2] = false;
        DADWSS[3] = false;
        DADWSS[4] = false;
        DADWSS[5] = false;
    }
    else if(mouseX > DL[0] && mouseX< DL[0]+DL[2] && mouseY > DL[1] && mouseY < DL[1] + DL[3])
    {
        DADWSS[2] = !(DADWSS[2]);
        detailSlider = floor(damp*10000.0f);
        DADWSS[1] = false;
        DADWSS[0] = false;
        DADWSS[3] = false;
        DADWSS[4] = false;  
        DADWSS[5] = false;
    }
    else if(mouseX > WLL[0] && mouseX< WLL[0]+WLL[2] && mouseY > WLL[1] && mouseY < WLL[1] + WLL[3])
    {
        DADWSS[3] = !(DADWSS[3]);
        detailSlider = floor(wavelen*4.0f);
        DADWSS[1] = false;
        DADWSS[2] = false;
        DADWSS[0] = false;
        DADWSS[4] = false;
        DADWSS[5] = false;
    }
    else if(mouseX > SL[0] && mouseX< SL[0]+SL[2] && mouseY > SL[1] && mouseY < SL[1] + SL[3]){
        DADWSS[4] = !(DADWSS[4]);
        detailSlider = floor(moverate*5);
        DADWSS[1] = false;
        DADWSS[2] = false;
        DADWSS[3] = false;
        DADWSS[0] = false;
        DADWSS[5] = false;
    }
    else if(mouseX > SiL[0] && mouseX< SiL[0]+SiL[2] && mouseY > SiL[1] && mouseY < SiL[1] + SiL[3]){
        DADWSS[5] = !(DADWSS[4]);
        detailSlider = floor(size/2);
        DADWSS[1] = false;
        DADWSS[2] = false;
        DADWSS[3] = false;
        DADWSS[4] = false;
        DADWSS[0] = false;
    }
    else if(mouseY>90){
      if(!editmode)
      {
        if(!first){
            firstx = mouseX;
            firsty = mouseY;
            first = true;
            if(count > freq){
              set.add(new Circle(firstx, firsty));
              count = 0;
            }
        }
        else{
          first= false;
        }
      }
      else
      {
        if(start)
        {
          fill(255-hue);
          circle(1425,72,12);
          noFill();
          lineloc[2] = mouseX;
          lineloc[3] = mouseY;
          start = false;
        }
        else{
          lineloc[0] = mouseX;
          lineloc[1] = mouseY;
          start = true;
        }
      }
    }
  }
  else if(mouseY>90){
    if(!editmode)
    {
      if(!first){
          firstx = mouseX;
          firsty = mouseY;
          first = true;
          if(count > freq){
            set.add(new Circle(firstx, firsty));
            count = 0;
          }
      }
      else{
        first= false;
      }
    }
    else
    {
      if(start)
      {
          noFill();
          lineloc[2] = mouseX;
          lineloc[3] = mouseY;
          start = false;
      }
      else{
        lineloc[0] = mouseX;
        lineloc[1] = mouseY;
        start = true;
      }
    }
  }
}

public void mouseClicked()
{
  mouseMovement();
}
public void mouseDragged()
{
  mouseMovement();
}

public void draw()
{
  waveDetailOn = false;
  for(boolean i : DADWSS){
      if(i){
        waveDetailOn = true;
      }
  }
  if((255-backgroundColors[0] + 255-backgroundColors[1] + 255-backgroundColors[2])/3 < 125){
    hue = 0;
  }
  else{
    hue = 255;
  }
  move-=PI*(moverate/100);
  count+=1;
  if(first){
    if(count > freq){
      set.add(new Circle(firstx, firsty));
      count = 0;
    }
  }
  for(int i = 0; i < set.size(); i++){
    set.get(i).update();
    if(set.get(i).t > size){
      set.remove(i);
    }
  }
  background(backgroundColors[0], backgroundColors[1] ,backgroundColors[2]);
  noFill();
  for(Circle circle : set){
    float a0 = sq(lineloc[0]-lineloc[2])+sq(lineloc[1]-lineloc[3]);
    float b0 = sq(lineloc[0]-circle.fx_)+sq(lineloc[1]-circle.fy_);
    float c0 = sq(lineloc[2]-circle.fx_)+sq(lineloc[3]-circle.fy_);
    float x = sqrt(b0)*sin(acos((a0+b0-c0)/(2*sqrt(a0)*sqrt(b0))));
    noFill();
    stroke(hue); 
    if(waveDetails)
    {
      if((circle.t+200)*4<1450)
      {
        if(!pointGraph)
        {
          line((circle.t+200)*4, 45, (circle.t+200)*4,(amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move/4)))/5+45);
        }
        else
        {
          point((circle.t+200)*4,(amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move/4)))/5+45);
        }
      }
    }
    switch(oscillatRGB)
    {
      case 0:
        stroke(waveColors[0], waveColors[1], waveColors[2]);
        break;
      case 1:
        stroke(waveColors[0], waveColors[1], waveColors[2]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25);
        break;
      case 2:
        stroke(waveColors[0], waveColors[1]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25, waveColors[2]);
        break;
      case 3:
        stroke(waveColors[0], waveColors[1]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25, waveColors[2]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25);
        break;
      case 4:
        stroke(waveColors[0]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25, waveColors[1], waveColors[2]);
        break;
      case 5:
        stroke(waveColors[0]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25, waveColors[1], waveColors[2]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25);
        break;
      case 6:
        stroke(waveColors[0]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25, waveColors[1]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25, waveColors[2]);
        break;
      case 7:
        stroke(waveColors[0]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25, waveColors[1]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25, waveColors[2]*amp*(1/exp(circle.t*damp))*cos(circle.t*((2*PI)/wavelen)+(move))/25);
        break;
    }
    float angle_from1 = 0;
    float angle_from0 = 0;
     if(editmode && (start))
     {
       if((lineloc[1]-lineloc[3]) !=0)
       {
         float m = PApplet.parseFloat(lineloc[0]-lineloc[2])/PApplet.parseFloat(lineloc[1]-lineloc[3]);
         float a1 = (sq(m))+1;
         float b1 = -(2.0f*circle.fy_)+ 2.0f*m*((-1.0f*m*lineloc[1])+lineloc[0]-circle.fx_);
         float c1 = (sq(circle.fy_))-sq(circle.wid/2.0f)+sq(-(m*lineloc[1])+lineloc[0]-circle.fx_);
         float r = circle.wid/2.0f;
         float interceptY1 = (-b1 + sqrt(sq(b1)-(4.0f*a1*c1)))/(2.0f*a1); 
         float interceptY2 = (-b1 - sqrt(sq(b1)-(4.0f*a1*c1)))/(2.0f*a1); 
         float interceptX1 = (m*interceptY1) - (m*lineloc[1]) + (lineloc[0]);
         float interceptX2 = (m*interceptY2) - (m*lineloc[1]) + (lineloc[0]);
         circle(interceptX1, interceptY1,10);
         circle(interceptX2, interceptY2,10);
         angle_from0 = cordToRad(interceptX1,interceptY1,circle.fx_,circle.fy_);
         angle_from1 = cordToRad(interceptX2,interceptY2,circle.fx_,circle.fy_);

         //print("\n" + "\n" + (2*sq(r)-sq(interceptX1-interceptX2)-sq(interceptY1-interceptY2))/(2*sq(r)));
       }
       if((degrees(acos((a0+b0-c0)/(2*sqrt(a0)*sqrt(b0)))) > 90 || degrees(acos((a0+c0-b0)/(2*sqrt(a0)*sqrt(c0)))) >90))
       {
         if(circle.wid/2 > min(sqrt(c0),sqrt(b0)))
         {
            //needs
           arc(circle.fx_, circle.fy_, circle.wid, circle.heig, angle_from0, angle_from1);

           print("\n" + "\n" + "From 0:" +angle_from0);
         }
         else
         {
           arc(circle.fx_, circle.fy_, circle.wid, circle.heig, 0, TWO_PI);
         }
       }
       else
       {
         if(circle.wid/2 > x)
         { 
           //needs
           arc(circle.fx_, circle.fy_, circle.wid, circle.heig, angle_from0, angle_from1);
           print("\n" + "\n" + "From 0:" +angle_from0);
         }
         else
         {
           arc(circle.fx_, circle.fy_, circle.wid, circle.heig, 0, TWO_PI);
         }
       }
     }
     else
     {
       arc(circle.fx_, circle.fy_, circle.wid, circle.heig, 0, TWO_PI);
     }
  }
  String s = "   Size: " + size + "   Density: "+ freq +"       Amp: " + amp + "          Damp: " +floor(damp*1000) + "        Wave-Length: " + wavelen + "       Speed: " + moverate;
  String rgb = "   R     G    B   ";
  float value = cordToRad(mouseX,mouseY,firstx,firsty);
  String currentMouse = mouseX + " , " + mouseY + " , " + floor(frameRate) + " , " + hue +" , " + waveDetails + waveDetailOn +value;  
  String colorTab = "Color";
  stroke(hue);
  //state with color dials
  if(colorOn)
  {
    rect(1500,25, 75, 255+24);
    line(1525, 25, 1525, 255+49);
    line(1550, 25, 1550, 255+49);
    line(1500,40,1575,40);
    fill(red, 0, 0 );
    circle(1513,red+49,12);
    fill(0,green,0);
    circle(1513+25,green+49,12);
    fill(0,0,blue);
    circle(1513+50,blue+49,12);
    //color edit button
    noFill();
    rect(1450,25,45,25);
    stroke(255-hue);
    fill(hue);
    text(rgb,1500,38);
    stroke(hue);
    if(waveDetails)
    {
      line(0,90,1500,90);
      line(1575,90,1600,90);
    }
  }
  else{
    //color edit button
    fill(hue);
    if(backgroundColor)
    {
      rect(1450,25,45,25);
      fill(backgroundColors[0],0,0);
      rect(1500,25,25,25);
      fill(0,backgroundColors[1],0);
      rect(1525,25,25,25);
      fill(0,0,backgroundColors[2]);
      rect(1550,25,25,25);
    }
    else
    {
      rect(1450,25,45,25);
      fill(waveColors[0],0,0);
      stroke(0);
      if(RGB[0]){
        stroke(255);
      }
      rect(1500,25,25,25);
      fill(0,waveColors[1],0);
      stroke(0);
      if(RGB[1]){
        stroke(255);
      }
      rect(1525,25,25,25);
      fill(0,0,waveColors[2]);
      stroke(0);
      if(RGB[2]){
        stroke(255);
      }
      rect(1550,25,25,25);
      stroke(hue);
    }
    fill(255-hue);
    textSize(15);
    text(colorTab, 1454, 42);
    textSize(11);
    if(waveDetails)
    {
      line(0,90,1600,90);
    }
    if(backgroundColor)
    {
      fill(hue);
      rect(1540,62,20,20);
      noFill();
      circle(1517,72,20);
    }
    else
    {
      noFill();
      rect(1540,62,20,20);
      fill(hue);    
      circle(1517,72,20); 
    }
  }
  if(editmode)
  {
    if(start)
    {
      line(lineloc[0],lineloc[1],lineloc[2],lineloc[3]);
      fill(hue);
      circle(lineloc[0], lineloc[1],5);
      circle(lineloc[2], lineloc[3],5);
      noFill();
    }
    else
    {
      fill(hue);
      circle(lineloc[2], lineloc[3],5);
      noFill();
    }
  }
  
  if(waveDetails){
    noFill();
    rect(30,25, 505, 50);
    rect(WDL[0], WDL[2], WDL[1]-WDL[0], WDL[3]-WDL[2]);
    fill(hue);
    text(s,30,36);
    noFill();
    rect(denL[0], denL[1], denL[2], denL[3]);
    rect(AL[0], AL[1],AL[2],AL[3]);
    rect(DL[0], DL[1], DL[2], DL[3]);
    rect(WLL[0], WLL[1], WLL[2], WLL[3]);
    rect(SL[0], SL[1], SL[2], SL[3]);
    rect(SiL[0], SiL[1], SiL[2], SiL[3]);
    line(800,0,800,90);
    if(pointGraph)
    {
      fill(hue);
      circle(805,10,5);
      noFill();
    }
    else
    {
      noFill();
      circle(805,10,5);  
    }
    
  }
  
  else{
    fill(hue);
    rect(WDL[0], WDL[2], WDL[1]-WDL[0], WDL[3]-WDL[2]);
    fill(255-hue);
    rect(WDL[0]-1, WDL[2]-1, WDL[1]-WDL[0]+2, WDL[3]-WDL[2]+2);
    fill(hue);
  }
  
  if(waveDetailOn)
  {
    fill(hue);
    circle(563+detailSlider,49,12);
    line(560, 50, 760,50);
    for(int i = 0; i<6; i++)
    {
      if(DADWSS[i])
      {
        fill(hue);
        rect(detailLoc[i][0],detailLoc[i][1],detailLoc[i][2],detailLoc[i][3]); 
        switch(i)
        {
          case 0:
            freq = floor(detailSlider/10);
            break;
          case 1:
            amp = floor(detailSlider/2);
            break;
          case 2:
            damp = detailSlider/10000.0f;
            break;
          case 3:
            wavelen = floor(detailSlider/4);
            break;
          case 4:
            moverate = floor(detailSlider/5);
            break;
           case 5:
             size = floor(detailSlider*2);
             break;
        }
      }
    }
    //color edit button
    noFill(); 
  }
  if(editmode)
  {
    fill(hue);
    rect(1412,60,25,25);
    if(start)
    {
      fill(255-hue);
      circle(1425,72,12);
    }
  }
  else
  {
    noFill();
    rect(1412,60,25,25);
    fill(hue);
  }
  text(currentMouse, 1200,100);
}

class Circle{
  float fx_, fy_, wid, heig, t;
  Circle(float fx, float fy){
    fx_ = fx;
    fy_ = fy;
    wid = 0;
    heig = 0;
    t=1;
  }
  public void update(){
    t+=1;
    wid +=2;
    heig +=2;
  }
}


public float cordToRad(float cordX, float cordY, float x, float y)
{
  float rad = atan((cordX-x)/(cordY-y));
  if(cordX>x)
  {
    //positive x
    if(cordY<y)
    {
      return (TWO_PI - (PI/2.0f + rad));
      //Quad 1
    }
    else
    {
      return ((PI/2.0f - rad));
      //Quad 4
    }
  }
  else
  {
    //negative x
    if(cordY<y)
    {
      return (PI + (PI/2.0f - rad));
      //Quad 2
    }
    else
    {
      return (PI/2 + (PI/2.0f + rad));
      //Quad 3
    }
  }
}

//imput R=0 G=1 B=3
public int colorSwitch(int colorin)
{
  switch(colorin)
  {
    case 0:
      RGB[0] = !(RGB[0]);
      switch(oscillatRGB)
      {
        case 0:
          return 4;
        case 1:
          return 5;
        case 2:
          return 6;
        case 3:
          return 7;
        case 4:
          return 0;
        case 5:
          return 1;
        case 6:
          return 2;
        case 7:
          return 3;
     }
     break;
   case 1:
      RGB[1] = !(RGB[1]);
      switch(oscillatRGB)
      {
        case 0:
          return 2;
        case 1:
          return 3;
        case 2:
          return 0;
        case 3:
          return 1;
        case 4:
          return 6;
        case 5:
          return 7;
        case 6:
          return 4;
        case 7:
          return 5;
      }
      break;
    case 2:
      RGB[2] = !(RGB[2]);
      switch(oscillatRGB)
      {
        case 0:
          return 1;
        case 1:
          return 0;
        case 2:
          return 3;
        case 3:
          return 2;
        case 4:
          return 5;
        case 5:
          return 4;
        case 6:
          return 7;
        case 7:
          return 6;
      }
      break;
  }
  return 0;
}
