require "json"

Dir.glob('activities_data/venues/*.json').each do |venues_json|
	venues = JSON.parse(File.read(venues_json))
	venues.each do |venue|
		Venue.create!(venue)
	end
end

Dir.glob('activities_data/tmp_events/*.json').each do |events_json|
	tevents = JSON.parse(File.read(tevents_json))
	tevents.each do |tevent|
		Tevent.create!(tevent)
	end
end