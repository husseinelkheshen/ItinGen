require 'rails_helper'

RSpec.describe Pevent, type: :model do
	describe "Creation" do
		before do
			@pevent = FactoryGirl.create(:pevent)
		end

		it 'can be created' do
			expect(@pevent).to be_valid
		end

		# it 'cannot be created without a venue_id' do
		# 	@pevent.venue_id = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a event_name' do
		# 	@pevent.event_name = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a event_alias' do
		# 	@pevent.event_alias = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a event_id' do
		# 	@pevent.event_id = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a mon_start' do
		# 	@pevent.mon_start = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a mon_end' do
		# 	@pevent.mon_end = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a tues_start' do
		# 	@pevent.tues_start = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a tues_end' do
		# 	@pevent.tues_end = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a wed_start' do
		# 	@pevent.wed_start = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a wed_end' do
		# 	@pevent.wed_end = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a thurs_start' do
		# 	@pevent.thurs_start = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a thurs_end' do
		# 	@pevent.thurs_end = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a fri_start' do
		# 	@pevent.fri_start = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a fri_end' do
		# 	@pevent.fri_end = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a sat_start' do
		# 	@pevent.sat_start = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a sat_end' do
		# 	@pevent.sat_end = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a sun_start' do
		# 	@pevent.sun_start = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a sun_end' do
		# 	@pevent.sun_end = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a tags' do
		# 	@pevent.tags = nil
		# 	expect(@pevent).to_not be_valid
		# end

		# it 'cannot be created without a price' do
		# 	@pevent.price = nil
		# 	expect(@pevent).to_not be_valid
		# end
	end
end
