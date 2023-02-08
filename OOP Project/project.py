#Enum
class BookingStatus(Enum):
    PENDING, CONFIRMED, CANCELLED = 1, 2, 3

class RoomStatus(Enum):
    AVAILABLE, UNAVAILBLE = 1, 2

#บอก class ต่างๆ
class Stays:
    def __init__(self, name, room_num, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact):
        self.name = name
        self.room_num = room_num
        self.bed_type = bed_type
        self.size = size
        self.toilet_type = toilet_type
        self.complimentary = complimentary
        self.speaker = speaker
        self.coffee_machine = coffee_machine
        self.bathrobes = bathrobes
        self.details = details
        self.highlights = highlights
        self.description = description
        self.room_count = room_count
        self.contact = contact
    pass

class Rooms(Stays):
    def __init__(self, name, room_num, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact):
        Stays.__init__(self, name, room_num, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact)
    pass

class Suites(Stays):
    def __init__(self, name, room_num, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact, bedroom, connecting, powder_room):
        Stays.__init__(self, name, room_num, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact)
        self.bedroom = bedroom
        self.connecting = connecting
        self.powder_room = powder_room
    pass

class RoomCatalog:
    def __init__(self, name, room_num, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact, bedroom, connecting, powder_room):
        Stays.__init__(self, name, room_num, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact)
        self.room_dict = {}
    pass

class Contact:
    def __init__(self, header_info, general_enquires, reservation, sales_marketing, dining, weddings, events, spa):
        self.header_info = header_info
        self.general_enquires = general_enquires
        self.reservation = reservation
        self.sales_marketing = sales_marketing
        self.dining = dining
        self.weddings = weddings
        self.events = events
        self.spa = spa
    pass
class Payment:
    def __init__(self, first_name, last_name, email, email_confirmation, country, phone_number, street_address, city, state_provunce, postal_code,date_of_birth, additional_info, terms_conditions, unpaid):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.email_confirmation = email_confirmation
        self.country = country
        self.phone_number = phone_number
        self.street_address = street_address
        self.city = city
        self.street_province = street_province
        self.postal_code = postal_code
        self.date_of_birth = date_of_birth
        self.additional_info = additional_info
        self.terms_conditions = terms_conditions
        self.unpaid = unpaid
    pass
class Booking:
    def __init__(self, calendar, check_in, check_out, room_price, total_price, currency):
        self.calendar = calendar
        self.check_in = check_in
        self.check_out = check_out
        self.room_price = room_price
        self.total_price = total_price
        self.currency = currency
    pass
class CreditPayment:
    def __init__(self, card_number, cardholder_name, expiration_date):
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.expiration_date = expiration_date
    pass
class SpecialCode:
    def __init__(self, iata_number, promo_code, group_code):
        self.iata_number = iata_number
        self.promo_code = promo_code
        self.group_code = group_code
    pass
class Show:
    def __init__(self, stays, contact, member_info, booking):
        self.stays = stays
        self.contact = contact
        self.member_info = member_info
        self.booking = booking
    pass
class Member_info:
    def __init__(self, member_id):
        self.member_id = member_id
    pass
class User:
    def __init__(self, email, password, status):
        self.email = email
        self.password = password
        self.status = status
    pass
