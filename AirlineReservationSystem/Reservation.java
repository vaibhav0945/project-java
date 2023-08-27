package AirlineReservationSystem;

public class Reservation {
    private String reservationNumber;
    private Flight flight;
    private Passenger passenger;

    public Reservation(String reservationNumber, Flight flight, Passenger passenger) {
        this.reservationNumber = reservationNumber;
        this.flight = flight;
        this.passenger = passenger;
    }

    public String getReservationNumber() {
        return reservationNumber;
    }

    public Flight getFlight() {
        return flight;
    }

    public Passenger getPassenger() {
        return passenger;
    }
}

