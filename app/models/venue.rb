class Venue < ApplicationRecord
    validate :venue_id, presence: true
    validate :venue_name, presence: true
    validate :venue_alias, presence: true
    validate :latitude, presence: true
    validate :longitude, presence: true
    validate :address1, presence: true
    validate :address2, presence: true
    validate :address3, presence: true
    validate :city, presence: true
    validate :state, presence: true
    validate :zip_code, presence: true
end