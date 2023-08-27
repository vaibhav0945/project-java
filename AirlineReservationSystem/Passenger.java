package AirlineReservationSystem;

public class Passenger {
    private String name;
    private String contactNumber;
    private String address;
    private String pId;

    public Passenger(String name, String contactInfo, String address) {
        this.name = name;
        this.contactNumber = contactInfo;
        this.address = address;
        this.pId = getPid();
    }

    public String getName() {
        return name;
    }

    public String getContactNumber() {
        return contactNumber;
    }

    public String getAddress() {
        return address;
    }

    private String getPid(){
        return UniqueIdGenerator.generateUniqueId(name);
    }

    // also add the functionality to ask the repeating user for the reference id (pid). if the user is the first time user
//    then call the get pid function to create a new pid for that particular user and then store the data.

}

