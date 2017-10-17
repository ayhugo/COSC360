import java.util.*;

public class RedGreen{
  //0 = green
  //1 = red
  public static int intInput = 0;
  public static HashMap<Integer, Integer> numColor = new HashMap<Integer, Integer>();
  public static StringBuilder sb;
  public static String sbString = "";
  public static int a = 0;
  public static List<String> colors;
  public static List<Integer> indexes;
  
  
  public static void main(String []args){
    Scanner scan = new Scanner(System.in);
    Scanner sc;
    int[] input = new int[2];
    String line;
    
    while(scan.hasNextLine()){
      line = scan.nextLine();
      sc = new Scanner(line);
      
      if (!line.isEmpty() && !line.startsWith("#")){
        for (int i = 0; i < 2; i++){
          input[i] = sc.nextInt();
        } 
        getFactors(input);
      }
    } 
  }
  public static void getFactors(int[] numbers){
    colors = new ArrayList<String>();

    sb = new StringBuilder();
    sb.append("#");
    
    colors.add("G");
    colors.add("G");

    for (int i = 2; i < (numbers[0]+numbers[1]); i++){
      indexes = new ArrayList<Integer>();
      int greens = 0;
      int reds = 0;
      for (int j = i/2; j >1; j--){
         Integer index = i/j;
        indexes.add(index);
      }
      greens++;
      
      for (int j = 0; j < indexes.size(); j++){
        if (indexes.size() ==1){
          reds++;
        } else if ( j == 0){
          if (colors.get(indexes.get(j)).equals("G")){
            greens++;
          }else{
            reds++;
          }
        } else if (indexes.get(j-1) < indexes.get(j)){
          if (colors.get(indexes.get(j)).equals("G")){
            greens++;
          } else {
            reds ++;
          }
        }
      }

      if (greens>reds){
        colors.add(i, "R");
        //sb.append("R");
      } else {
        colors.add(i, "G");
        //sb.append("G");
      }
      
    }//end i forloop
    for (int i = numbers[0]; i < colors.size(); i++){
      sb.append(colors.get(i));
    }
    
    System.out.println(sb);
  }//end getFactors
}