require 'rails_helper'

RSpec.describe Venue, type: :model do
	describe "Creation" do
		before do
			@venue = FactoryGirl.create(:venue)
		end

		it 'can be created' do
			expect(@venue).to be_valid
		end

		it 'cannot be created without a venue_id' do
			@venue.venue_id = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a venue_name' do
			@venue.venue_name = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a venue_alias' do
			@venue.venue_alias = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a latitude' do
			@venue.latitude = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a longitude' do
			@venue.longitude = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a address1' do
			@venue.address1 = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a address2' do
			@venue.address2 = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a address3' do
			@venue.address3 = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a city' do
			@venue.city = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a state' do
			@venue.state = nil
			expect(@venue).to_not be_valid
		end

		it 'cannot be created without a zip_code' do
			@venue.zip_code = nil
			expect(@venue).to_not be_valid
		end
	end
end
