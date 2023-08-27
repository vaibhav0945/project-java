package AirlineReservationSystem;

import java.util.ArrayList;
import java.util.List;

public class Airline {
    private String name;
    private List<Flight> flights;

    public Airline(String name) {
        this.name = name;
        this.flights = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        flights.add(flight);
    }
}

