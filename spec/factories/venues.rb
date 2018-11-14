FactoryBot.define do
  factory :venue do
    venue_id "test_id"
    venue_name "test_name"
    venue_alias "test_alias"
    latitude 1.0
   	longitude 1.0
   	address1 "address1"
   	address2 "address2"
   	address3 "address3"
   	city "test_city"
   	state "test_state"
   	zip_code "test_zip"
  end
end
