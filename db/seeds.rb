require "json"
venues = JSON.parse(File.read('activities_data/venues_11122018.json'))
venues.each do |venue|
	Venue.create!(venue)
end
