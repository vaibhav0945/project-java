package AirlineReservationSystem;

import java.util.ArrayList;
import java.util.List;

public class ReservationSystem {
    private List<Airline> airlines;

    private static ReservationSystem instance;

    private ReservationSystem() {
        airlines = new ArrayList<>();
    }

    public static ReservationSystem getInstance() {
        if (instance == null) {
            instance = new ReservationSystem();
        }
        return instance;
    }

    public void addAirline(Airline airline) {
        airlines.add(airline);
    }

//    public List<Flight> searchFlights(String departure, String arrival, Date date) {
//        // Implement flight search logic
//    }

//    public Reservation makeReservation(Passenger passenger, Flight flight) {
//        // Implement reservation creation logic
//    }
}
