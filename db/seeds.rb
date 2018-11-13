require "json"

Dir.glob('activities_data/events/*.json').each do |events_json|	
	events = JSON.parse(File.read(events_json))
	events.each do |event|
		Event.create!(event)
	end
end

Dir.glob('activities_data/venues/*.json').each do |venues_json|	
	venues = JSON.parse(File.read(venues_json))
	venues.each do |venue|
		Venue.create!(venue)
	end
end