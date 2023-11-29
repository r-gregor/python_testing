import java.util.*;

public class BankovciKovanci {
    private Map<String, Integer> bc = new LinkedHashMap<String, Integer>();

    {   // initialization block
        bc.put("Bankovec 500 EUR", 0);
        bc.put("Bankovec 200 EUR", 0);
        bc.put("Bankovec 100 EUR", 0);
        bc.put("Bankovec 50 EUR", 0);
        bc.put("Bankovec 20 EUR", 0);
        bc.put("Bankovec 10 EUR", 0);
        bc.put("Bankovec 5 EUR", 0);
        bc.put("Kovanec 2 EUR", 0);
        bc.put("Kovanec 1 EUR", 0);
        bc.put("Kovanec 50 centov", 0);
        bc.put("Kovanec 20 centov", 0);
        bc.put("Kovanec 10 centov", 0);
        bc.put("Kovanec 5 centov", 0);
        bc.put("Kovanec 2 centa", 0);
        bc.put("Kovanec 1 cent", 0);
    }
    public static void main(String[] args) {
   

        List<Double> eurs = new ArrayList<Double>();
        for (String euro: args) {
            Double newEuro = Double.valueOf(euro);
            eurs.add(newEuro);
        }

        BankovciKovanci BC = new BankovciKovanci();

        for (Double znesek: eurs) {
            BC.getBaknkovciInKovanci(znesek);
        }
        
    } // end main


    public void getBaknkovciInKovanci(Double znesek) {
        System.out.println("===================================");
        System.out.printf("*** Znesek: %.2f EUR ***%n", znesek);

        double novirest1 = 0;
        bc.put("Bankovec 500 EUR", (int) (znesek / 500));
        novirest1 += (znesek % 500);
        
        double novirest2 = 0;
        bc.put("Bankovec 200 EUR", (int) (novirest1 / 200));
        novirest2 += (novirest1 % 200);
        
        double rest1 = 0;
        bc.put("Bankovec 100 EUR", (int) (novirest2 / 100));
        rest1 += (novirest2 % 100);
        
        double rest2 = 0;
        bc.put("Bankovec 50 EUR", (int) (rest1 / 50));
        rest2 += (rest1 % 50);

        double rest3 = 0;
        this.bc.put("Bankovec 20 EUR", (int) (rest2 / 20));
        rest3 += (rest2 % 20);

        double rest4 = 0;
        this.bc.put("Bankovec 10 EUR", (int) (rest3 / 10));
        rest4 += (rest3 % 10);

        double rest5 = 0;
        this.bc.put("Bankovec 5 EUR", (int) (rest4 / 5));
        rest5 += (rest4 % 5);

        double rest6 = 0; 
        this.bc.put("Kovanec 2 EUR", (int) (rest5 / 2));
        rest6 += (rest5 % 2);

        double rest7 = 0; 
        this.bc.put("Kovanec 1 EUR", (int) (rest6 / 1));
        rest7 += (rest6 % 1);

        rest7 = rest7 * 100;
       
        double rest8 = 0; 
        this.bc.put("Kovanec 50 centov", (int) (rest7 / 50));
        rest8 += (rest7 % 50);
      
        double rest9 = 0; 
        this.bc.put("Kovanec 20 centov", (int) (rest8 / 20));
        rest9 += (rest8 % 20);
        
        double rest10 = 0; 
        this.bc.put("Kovanec 10 centov", (int) (rest9 / 10));
        rest10 += (rest9 % 10);
       
        double rest11 = 0;   
        this.bc.put("Kovanec 5 centov", (int) (rest10  / 5));
        rest11 += (rest10 % 5);
       
        double rest12 = 0;
        this.bc.put("Kovanec 2 centa", (int) (rest11 / 2));
        rest12 += (rest11 % 2);
       
        double rest13 = 0;
        this.bc.put("Kovanec 1 cent", (int) (rest12 / 1));
        rest13 += (rest12 % 1);

        for(Map.Entry<String, Integer> entry: bc.entrySet()) {
            if (entry.getValue() != 0) {
                System.out.printf("%s = %dx%n",entry.getKey(), entry.getValue());
            }
        }

    }

} // end class