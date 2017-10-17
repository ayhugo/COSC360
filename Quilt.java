import javax.swing.*;
import java.awt.*;
import java.util.*;

public class Quilt extends JFrame{
  
  public static Scanner input = new Scanner(System.in);
  
  public static ArrayList<Double> scaleList = new ArrayList<Double>();
  public static ArrayList<Color> colorList = new ArrayList<Color>();
  public static double totalScale = 0.0;
  public static int windowSize = 400;
  public static int initalScale = 0;
  
  public static void main(String[]args){
    while (input.hasNextLine()) {
      sortLines(input.nextLine());
    } 
    double tempScale = scaleList.get(0);
    double tempTotalScale = totalScale;
    double result = windowSize * (tempScale/tempTotalScale);
    
    initalScale = (int) result;
    
    Quilt window = new Quilt();
    window.setVisible(true);
    window.setSize(windowSize, windowSize+22);
    /*
1.0 255 0 0
0.8 0 255 0
0.1 0 0 255
     scaleList.add(1.0);
     scaleList.add(0.8);
     scaleList.add(0.1);
     
     colorList.add(new Color(255,0,0));
     colorList.add(new Color(0,255,0));
     colorList.add(new Color(0,0,255));
     */
    
    
  }
  public static void sortLines (String sc) {
    if (!sc.trim().isEmpty()) {
      if (!sc.startsWith("#")) {
        String[] input = sc.split(" ");
        totalScale = totalScale += Double.parseDouble(input[0]);
        scaleList.add(Double.parseDouble((input[0])));
        colorList.add(new Color(Integer.parseInt((input[1])),Integer.parseInt((input[2])),Integer.parseInt((input[3]))));
      }
    }
  }
     
  public static class Square{
    int x;
    int y;
    int size;
    int depth;
    Color c;
    public Square(int x, int y, int size, int depth, Color c){
      this.x = x;
      this.y = y;
      this.size = size;
      this.depth = depth;
      this.c = c;
    }
  }
  
  public static class XY {
    int x;
    int y;
    int length;
    int size;
    
    public XY(int x, int y, int length, int size){
      this.x = x;
      this.y = y;
      this.length = length;
      this.size = size;
    }
    
  }
  
  public void paint(final Graphics g){
    ArrayList<XY> coordinates = new ArrayList<XY>();
    ArrayList<Square> s = new ArrayList<Square>();
    //scales = window/totalScale
    //System.out.println(windowSize/totalScale);
    boolean change = true;
    Double tempScaleDo = scaleList.get(0) * windowSize/totalScale;
    int tempScaleInt = tempScaleDo.intValue();
    int xy = windowSize / 2 - tempScaleInt / 2;
    
    for(int i = 0; i < scaleList.size(); i ++){
      Color c = colorList.get(i);
      Double d = scaleList.get(i) * windowSize/totalScale;
      int size = d.intValue();
      //System.out.println(size);
      int prevX = -1;
      
      for(Square square : s){
        prevX = square.x;
        coordinates.add(new XY(square.x, square.y, square.depth, square.size));
      }
      if(change) {
        s.add(new Square(xy,xy,size,1,c));
        change = false;     
      }
      if(prevX!=-1){
        for (XY cord: coordinates){
          if (cord.length == i){
            s.add(new Square(cord.x - (size / 2), (cord.y - (size / 2)), size, cord.length + 1, c));
            s.add(new Square(cord.x - (size / 2), cord.y - (size / 2) + cord.size, size, cord.length + 1, c));
            s.add(new Square(cord.x - (size / 2) + cord.size, cord.y - (size / 2), size, cord.length + 1, c));
            s.add(new Square(cord.x - (size / 2) + cord.size, cord.y - (size / 2) + cord.size, size, cord.length + 1, c));
          }
        }
      }
    }//end i loop
    
    for (Square square : s){
      g.setColor(square.c);
      g.fillRect(square.x,square.y+20,square.size,square.size);
    }
  }
}