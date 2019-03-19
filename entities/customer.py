from dataclasses import dataclass


@dataclass
class Customer:

    customer_id: str
    auth_token: str

    email: str
    password: str
    username: str

    full_name: str
    first_name: str
    last_name: str
    phone_number: str
    mailing_address_display: str
    preferred_language: str

    driver_license_number: str
    is_license_verified: bool

    number_of_paid_drives: int
    external_membership_number: str
    has_valid_payment_card: bool

    blocked: bool
    can_reserve_car: bool
    phone_number_verified: bool
    blocked_until_datetime: str
    pin_number: str
    last_signed_tos_version: int
    rfid: str

    is_jumio_verified: bool
    jumio_in_progress: bool
