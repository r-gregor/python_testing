// filename Test.java

import java.util.*;

public class Test {
    //** Main function */
    public static void main(String[] args) {
        

        Map<Integer, Double> f_st = new HashMap<Integer, Double>();
        f_st.put(1, 0.621); f_st.put(2, 0.448); f_st.put(3, 0.371); f_st.put(4, 0.325); f_st.put(5, 0.294);
        f_st.put(6, 0.271); f_st.put(7, 0.253); f_st.put(8, 0.239); f_st.put(9, 0.227); f_st.put(10, 0.217);
        f_st.put(11, 0.208); f_st.put(12, 0.201); f_st.put(13, 0.194); f_st.put(14, 0.188); f_st.put(15, 0.183);
        f_st.put(16, 0.178); f_st.put(17, 0.173); f_st.put(18, 0.169); f_st.put(19, 0.166); f_st.put(20, 0.162);
        f_st.put(21, 0.159); f_st.put(22, 0.156); f_st.put(23, 0.153); f_st.put(24, 0.151); f_st.put(25, 0.148);
        f_st.put(26, 0.146); f_st.put(27, 0.144); f_st.put(28, 0.142); f_st.put(29, 0.140); f_st.put(30, 0.138);
        f_st.put(31, 0.136); f_st.put(32, 0.134); f_st.put(33, 0.133); f_st.put(34, 0.131); f_st.put(35, 0.130);
        f_st.put(36, 0.128); f_st.put(37, 0.127); f_st.put(38, 0.126); f_st.put(39, 0.125); f_st.put(40, 0.123);
        f_st.put(41, 0.122); f_st.put(42, 0.121); f_st.put(43, 0.120); f_st.put(44, 0.119); f_st.put(45, 0.118);
        f_st.put(46, 0.117); f_st.put(47, 0.116); f_st.put(48, 0.115); f_st.put(49, 0.114); f_st.put(50, 0.114);

        // test
        int st = 44;
        System.out.printf("Faktor istočasnosti za %d trošil znaša: %.3f%n.",  st, f_st.get(st));

    
    } // end Main
        
} // end class
