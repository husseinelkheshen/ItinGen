class Tevent < ApplicationRecord
	validate :venue_id, presence: true
	validate :event_name, presence: true
	validate :event_id, presence: true
	validate :start, presence: true
	validate :end, presence: true
	validate :date, presence: true
	validate :tags, array: true, presence: true
	validate :price, presence: true
end
