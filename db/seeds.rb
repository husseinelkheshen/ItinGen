require "json"
events = JSON.parse(File.read('/path/to/events/json'))
events.each do |event|
	Events.create!(event)
end
