FactoryBot.define do
  factory :pevent do
    venue_id "test_venue"
    event_name "test_event"
    event_alias "test_alias"
    event_id "test_id"
    mon_start 0
    mon_end 0
    tues_start 0
    tues_end 0
    wed_start 0
    wed_end 0
    thurs_start 0
    thurs_end 0
    fri_start 0
    fri_end 0
    sat_start 0
    sat_end 0
    sun_start 0
    sun_end 0
    tags ["test_tags"]
    price 0
  end
end
