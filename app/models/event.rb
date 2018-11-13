class Event
  include Mongoid::Document
  field :venue_id, type: String
  field :event_name, type: String
  field :event_alias, type: String
  field :event_id, type: String
  field :mon_start, type: Integer
  field :mon_end, type: Integer
  field :tues_start, type: Integer
  field :tues_end, type: Integer
  field :wed_start, type: Integer
  field :wed_end, type: Integer
  field :thurs_start, type: Integer
  field :thurs_end, type: Integer
  field :fri_start, type: Integer
  field :fri_end, type: Integer
  field :sat_start, type: Integer
  field :sat_end, type: Integer
  field :sun_start, type: Integer
  field :sun_end, type: Integer
  field :tags, type: Array
  field :price, type: Integer
end
