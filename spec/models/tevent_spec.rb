require 'rails_helper'

RSpec.describe Tevent, type: :model do
	describe "Creation" do
		before do
			@tevent = FactoryGirl.create(:tevent)
		end

		it 'can be created' do
			expect(@tevent).to be_valid
		end

		# it 'cannot be created without a venue_id' do
		# 	@tevent.venue_id = nil
		# 	expect(@tevent).to_not be_valid
		# end

		# it 'cannot be created without a event_name' do
		# 	@tevent.event_name = nil
		# 	expect(@tevent).to_not be_valid
		# end

		# it 'cannot be created without a event_id' do
		# 	@tevent.event_alias = nil
		# 	expect(@tevent).to_not be_valid
		# end

		# it 'cannot be created without a start' do
		# 	@tevent.start = nil
		# 	expect(@tevent).to_not be_valid
		# end

		# it 'cannot be created without a date' do
		# 	@tevent.date = nil
		# 	expect(@tevent).to_not be_valid
		# end

		# it 'cannot be created without a tags' do
		# 	@tevent.tags = nil
		# 	expect(@tevent).to_not be_valid
		# end

		# it 'cannot be created without a price' do
		# 	@tevent.price = nil
		# 	expect(@tevent).to_not be_valid
		# end

	end
end
