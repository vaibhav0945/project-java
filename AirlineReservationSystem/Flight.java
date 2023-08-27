package AirlineReservationSystem;

import java.util.Date;

public class Flight {
    private String flightNumber;
    private String departureLocation;
    private String arrivalLocation;
    private Date departureTime;
    private int totalSeats;
    private int availableSeats;

    public Flight(String flightNumber, String departureLocation, String arrivalLocation, Date departureTime, int totalSeats) {
        this.flightNumber = flightNumber;
        this.departureLocation = departureLocation;
        this.arrivalLocation = arrivalLocation;
        this.departureTime = departureTime;
        this.totalSeats = totalSeats;
        this.availableSeats = totalSeats;
    }

    public String getFlightNumber() {
        return flightNumber;
    }

    public String getDepartureLocation() {
        return departureLocation;
    }

    public String getArrivalLocation() {
        return arrivalLocation;
    }

    public Date getDepartureTime() {
        return departureTime;
    }

    public int getTotalSeats() {
        return totalSeats;
    }

    public int getAvailableSeats() {
        return availableSeats;
    }

    public boolean reserveSeat() {
        if (availableSeats > 0) {
            availableSeats--;
            return true;
        }
        return false;
    }
}

