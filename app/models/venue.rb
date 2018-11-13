class Venue
  include Mongoid::Document
  field :venue_id, type: String
  field :venue_name, type: String
  field :venue_alia, type: String
  field :latitude, type: Float
  field :longitude, type: Float
  field :address1, type: String
  field :address2, type: String
  field :address3, type: String
  field :city, type: String
  field :state, type: String
  field :zip_code, type: String
end
