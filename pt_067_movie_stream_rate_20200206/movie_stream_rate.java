// movie_stream_rate.java



public class movie_stream_rate {

static String usage = "Usage ...";
    public static void main(String[] args) {
        double myMS = 1.0;
        double mytimem = 1.0;
        
        if (args.length == 0) {
            showAll();
        
        } else if (args[0] == "h") {
            System.out.print(usage);
            System.exit(0);

        } else if (args.length == 2) {

            String arg1 = args[0];
            String arg2 = args[1];

            myMS = Double.valueOf(arg1);
            mytimem = Double.valueOf(arg2);
            System.out.println("Custom parameters calculation:");
            rate(myMS, mytimem);

        } else {
            System.out.println("Wrong number of parameters!");
            System.out.print(usage);
            System.exit(0);
        }

    } // end main

    public static void rate(double size, double minutes) {
        double rate = (size * 1024 * 8) / (minutes * 60);
        String line = String.format("Movie size: %.0f GB\n" +
            "Dration:    %.0f min.\n" +
            "Rate:       %.3f Mbit/s\n", size, minutes, rate);
        System.out.print(line);
    }

    public static void showAll() {
        System.out.println("Show All!");
    }




} // end class