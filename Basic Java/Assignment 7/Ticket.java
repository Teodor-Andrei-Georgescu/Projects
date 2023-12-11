public class Ticket implements Comparable<Ticket>{

	private String eventName;
	private int ticketType;
	private int seatNumber;
	
	public Ticket(String eventName, int ticketType, int seatNumber) {
		this.eventName = eventName;
		this.ticketType = ticketType;
		this.seatNumber = seatNumber;
	}

	public String getEventName() {
		return eventName;
	}

	public int getTicketType() {
		return ticketType;
	}

	public int getSeatNumber() {
		return this.seatNumber;
	}

	public String toString() {
		return eventName + " (type:"+ticketType+")";
	}

	/*
	 * Purpose: returns the result of comparing this ticket's
	 *          ticketType with other ticket's ticketType
	 * Parameters: Ticket other
	 * Precondition: other is not null
	 * Returns: a value < 0 if this ticketType is higher priority than other
	 *          a value == 0 if this ticketTypes are the same
	 *          a value > 0 if this ticketType is lower priority than other
	 */
	public int compareTo(Ticket other) {
		return this.ticketType - other.ticketType;
	}

	/* 
	 * Purpose: determines whether this ticket's eventName, ticketType
	 *          and seatNumber are the same as the other ticket
	 * Parameters: Ticket other
	 * Precondition: other is not null
	 * Returns: true if this ticket is the same as other, false otherwise
	 */
	public boolean equals(Ticket other) {
		return this.eventName.equals(other.eventName)
			&& this.ticketType == other.ticketType
				&& this.seatNumber == other.seatNumber;
	}
}


