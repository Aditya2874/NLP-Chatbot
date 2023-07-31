import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = ("If I were you, I would go to the internet and type exactly what you wrote there!")
R_CANCEL = "Visit the View/Change bookings option on the homepage of our website. "
R_VIEW = """The View/ Change bookings sections is a self-service online tool on the website specially designed to 
eliminate the need to check booking details and request booking services via our call centre.  """
R_ChangeDestination = """You will not be be able to change your origin and destination through the View/ Change Booking facility
but passengers can opt to cancel their reservation and create a new reservation through the regular booking procedure. """
R_REFUND = """On domestic flights you can cancel/ refund till 2 hours prior to flight departure On international flights you can cancel/ refund till 4 hours prior to flight departure"""
R_LUGGAGE = "Maximum Luugage :One hand bag up to 7 kgs and 115 cms (L+W+H), shall be allowed per customer.\n For further query: Click on this link: https://www.goindigo.in/travel-information/en/baggage-allowance.html"
R_LOST = "Customers are solely responsible for carriage of their hand bag / personal belongings. airline company is not liable for any loss / damage  caused to customer's hand baggage / personal belongings"
R_INFANT = """For safety reasons, children above the age of 3 days and under the age of 2 years, as on the date of travel, can travel as Infants. Age proof needs to be provided at the time of check-in.
Valid ID proof for Infants:
Birth Certificate
Mother's hospital discharge summary
Vaccination certificate
Passport"""
R_CHECKIN = """Passengers can check-in at airline counters located at airports. Passengers must keep in mind the following rules related to airport check-ins:
Complete your government-mandated web check-in for free 48 hours and 60 min before flight.
for further info visit: https://www.goindigo.in/travel-information/en/airport-check-in-requirements.html"""
R_FARERULES = """The rules and conditions of any reservation depend upon the fare type that the reservation has been made under. These rules and applicable conditions for a particular fare type are called Fare Rules.
for more info visit : https://www.goindigo.in/travel-information/en/fare-rules.html"""
R_MEDICAL = """Customers who are ailing from any particular medical condition can travel on airplane after giving prior medical information as per the medical form provided on the airline Website, in order for airline to provide complete assistance.
Medical Information must be provided to IndiGo at least 72 hours prior to the scheduled departure of the flight.
The customer must also inform airline regarding any hospitalisation requirement upon arrival."""


def unknown():
    response = [
        "Could you please re-phrase that? ",
        "...",
        "Sounds about right.",
        "What does that mean?",
    ][random.randrange(4)]
    return response
