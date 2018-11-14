require 'rails_helper'

describe 'content' do
  before do
    visit root_path
  end

  describe 'homepage' do
    it 'should be reached successfully' do
      expect(page.status_code).to eq(200)
    end

    it 'should have a title' do
      page.should have_css('h1', :text => 'Itinerary Generator')
    end

    describe 'maps' do
      it 'should display google maps' do
        page.should have_css('div', :id => 'map')
      end

      it 'should display a location' do
        page.should have_css('div', :class => 'marker')
      end
    end

    describe 'sidebar' do
      describe 'menu' do
        it 'should have a menu' do
          page.should have_css('ul', :text => 'Menu')
        end

        it 'should have an option to login' do
          page.should have_css('button', :text => 'Login')
        end

        it 'should have an option to sign up' do
          page.should have_css('button', :text => 'Sign Up')
        end
      end

      it 'should have an itinerary' do
        page.should have_css('div', :class => 'itinerary')
      end

      it 'should have a generate button' do
        page.should have_css('button', :id => 'Generate')
      end

      it 'should have a dislike button' do
        page.should have_css('button', :text => 'Dislike')
      end

      it 'should have a save current itinerary button' do
        page.should have_css('button', :text => 'Save Itinerary')
      end

      it 'should have a link to saved itineraries' do
        page.should have_css('button', :text => 'View Saved Itineraries')
      end

    end
  end
end
