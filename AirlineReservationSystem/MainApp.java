package AirlineReservationSystem;

import java.util.Scanner;

public class MainApp {

    public static void printSequence() throws InterruptedException {
        String writerSystem = "Airline Reservation System";

        for(int i=0;i<20;i++){
            System.out.print("-");
            Thread.sleep(10);
        }

        System.out.print(" | ");

        for(char ch : writerSystem.toCharArray()){
            System.out.print(ch);
            Thread.sleep(10);
        }

        System.out.print(" | ");

        for(int i=0;i<20;i++){
            System.out.print("-");
            Thread.sleep(10);
        }

        System.out.println();
    }

    public static void main(String[] args) throws InterruptedException {
        //user interface
        printSequence();
        Scanner sc = new Scanner(System.in);
        int choice = 0;
        while(choice != -1){
            System.out.println("Enter your choice : ");
            System.out.println("1 :  Book a Flight");
            System.out.println("2 :  Check Flight Status");
            System.out.println("3 :  Cancel Flight");
            System.out.println("-1 : EXIT from Airline Reserveration System\n");
            printSequence();

            choice = Integer.parseInt(sc.nextLine());
            
            switch (choice){
                case 1 :
                    System.out.println("HELLO 1");
                    break;
                case 2 :
                    System.out.println("2");
                    break;
                case 3 :
                    System.out.println("3");
                    break;
                case -1 :
                    System.out.println("EXITING THE AIRLINE RESERVATION SYSTEM");
                    System.exit(1);
                    break;
            }
        }
    }
}
