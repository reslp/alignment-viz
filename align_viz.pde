// written by Philipp Resl
// last changed: 16 April 2015

void setup() {
  
  size(1100, 400);  // Size should be the first statement
  stroke(0);     // Set stroke color to white
  background(255); 
  //println(nex);
  String[] map = loadStrings("../out.txt"); // input file created with calcmiss.py
  String[] nex = new String[map.length];
  int[] y_wert = new int[map.length];
  
  for (int i=1;i<map.length; i++) {
     y_wert[i] = int(Math.round(Float.parseFloat(map[i])));
  }
  //println(y_wert);
  float x = 0;
  float y = 350;
  fill(0);
  for (int i=1;i<map.length;i++){
  // specify which alignmemt position
  if (i == 610){stroke(#FF0000);}
  if (i == 1380){stroke(#00FF00);}
  if (i == 2660){stroke(#0000FF);}
  if (i == 3500){stroke(#CCEEFF);}
  if (i == 3760){stroke(#8ba752);}
  if (i == 4480){stroke(#83584f);}
  if (i == 5450){stroke(#ffb6ad);}
  
  x = map(i,1,y_wert.length,50,1000);
  //point((int) x,(y-y_wert[i]));
  print ((int)x,i, (int) x, (y-y_wert[i]*3), "\n");
  line ((int)x,350,(int)x,(y-y_wert[i]*3));
  //ellipse((int) x,(y-y_wert[i]*3),2,2);
  }
  stroke(0);
  line (49,50,49,350); //y axis
  line (49,350,1010,350); //x axis
  //stroke(#CCFFAA);
  //fill(#CCFFAA);
  for (int i=1;i<map.length;i+=1000){ // x axis label
    x = map(i,1,(y_wert.length),50,1000);   
    line((int)x, 350, (int)x, 355);
    ellipse((int)x, 355, 2, 2);
  }
  save("output.png");
}


