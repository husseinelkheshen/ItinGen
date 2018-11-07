require 'rails_helper'

RSpec.describe Event, type: :model do
  describe "Creation" do
    before do
      @event = FactoryGirl.create(:event)
    end

    it 'can be created' do
      expect(@event).to be_valid
    end

    it 'cannot be created without a name, lat, lng, and rating' do
      @event.name = nil
      @event.lat = nil
      @event.lng = nil
      @event.rating = nil
      expect(@event).to_not be_valid
    end
  end
end
