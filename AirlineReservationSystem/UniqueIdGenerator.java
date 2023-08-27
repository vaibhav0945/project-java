package AirlineReservationSystem;

public class UniqueIdGenerator {

//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        System.out.println("Enter choice");
//        int ch = Integer.parseInt(scanner.nextLine());
//        while(ch != -1){
//            System.out.print("Enter passenger name: ");
//            String passengerName = scanner.nextLine();
//
//            String uniqueId = generateUniqueId(passengerName);
//            System.out.println("Unique ID for " + passengerName + ": " + uniqueId);
//        }
//    }

    public static String generateUniqueId(String name) {
        String modifiedName = name.toLowerCase().replaceAll(" ", "").replaceAll("-", "");
        int nameSum = 0;
        for (char c : modifiedName.toCharArray()) {
            nameSum += (int) c;
        }
        long timestamp = System.currentTimeMillis();  // Current timestamp in milliseconds
        String uniqueId = nameSum + "" + timestamp;
        return uniqueId;
    }
}
