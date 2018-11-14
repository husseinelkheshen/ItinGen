class Venue < ApplicationRecord
    validates :venue_id, presence: true
    validates :venue_name, presence: true
    validates :venue_alias, presence: true
    validates :latitude, presence: true
    validates :longitude, presence: true
    validates :address1, presence: true
    validates :address2, presence: true
    validates :address3, presence: true
    validates :city, presence: true
    validates :state, presence: true
    validates :zip_code, presence: true
end
