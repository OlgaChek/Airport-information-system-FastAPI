from sqlmodel import SQLModel, Field, Session, create_engine
from datetime import datetime
from typing import Optional

class Airport(SQLModel, table=True):
    id_airport: Optional[str] = Field(primary_key=True)
    airport_name: str
    legal_address: str
    code_IATA_ICAO: str

class Airplane(SQLModel, table=True):
    id_airplane: Optional[str] = Field(primary_key=True)
    airplane_type: str
    model: str
    capacity: int
    technical_condition: str

class Flight(SQLModel, table=True):
    id_flight: Optional[str] = Field(primary_key=True)
    departure_date: datetime
    arrival_date: datetime
    departure_airport: Optional[str] = Field(foreign_key="airport.id_airport")
    arrival_airport: Optional[str] = Field(foreign_key="airport.id_airport")
    id_airplane: Optional[str] = Field(foreign_key="airplane.id_airplane")
    num_of_avail_seats: int

class Passenger(SQLModel, table=True):
    id_passenger: Optional[str] = Field(primary_key=True)
    full_name: str
    series_number_passport: str
    contacts: str

class LoyaltyProgram(SQLModel, table=True):
    id_client: Optional[str] = Field(primary_key=True)
    id_passenger: Optional[str] = Field(foreign_key="passenger.id_passenger")
    loyalty_program: str
    discounts_bonuses: float

class Reservation(SQLModel, table=True):
    id_reservation: Optional[str] = Field(primary_key=True, unique=True)
    id_flight: Optional[str] = Field(foreign_key="flight.id_flight")
    booking_status: str

class Employee(SQLModel, table=True):
    id_employee: Optional[str] = Field(primary_key=True)
    full_name: str
    job: str
    certification_license: str
    id_airplane: Optional[str] = Field(foreign_key="airplane.id_airplane")

class AirTicket(SQLModel, table=True):
    id_airticket: Optional[str] = Field(primary_key=True)
    id_reservation: Optional[str] = Field(foreign_key="reservation.id_reservation")
    departure_date: datetime
    arrival_date: datetime
    service_class: str
    id_passenger: Optional[str] = Field(foreign_key="passenger.id_passenger")
    ticket_price: float

class Payment(SQLModel, table=True):
    id_reservation: Optional[str] = Field(primary_key=True, foreign_key="reservation.id_reservation")
    payment_state: str 

#engine = create_engine("sqlite:///database.db")
#SQLModel.metadata.create_all(engine) 

