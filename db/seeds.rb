require "json"

file = File.read('./activities_data/venues/venues_11122018.json')
venues = JSON.parse(file)

vs = []
venues.each do |venue|
  vs << Venue.create(:venue_id => venue[:venue_id],
                :venue_name => venue[:venue_name],
                :latitude => venue[:latitude],
                :longitude => venue[:longitude],
                :address1 => venue[:address1],
                :address2 => venue[:address2],
                :address3 => venue[:address3],
                :city => venue[:city],
                :state=> venue[:state],
                :zip_code => venue[:zip_code])
end

puts vs

#Dir.glob('activities_data/venues/*.json').each do |venues_json|
	#venues = JSON.parse(File.read(venues_json))
	#venues.each do |venue|
		#Venue.create!(venue)
	#end
#end
