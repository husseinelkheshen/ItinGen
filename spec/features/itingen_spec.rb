require 'rails_helper'

class Home
  include Capybara::DSL
  def visit_homepage
    visit('/')
  end
end

feature "Visit homepage" do
  let(:home) {Home.new}
  scenario "Able to see text, Word Nerds", :js => true do
    sleep(10)
    home.visit_homepage
    binding.pry
    expect(page).to have_content("Word Nerds")
  end
end

#describe 'content' do
  #before do
    #visit root_path
    #sleep(10)
  #end

  #describe 'homepage' do
    #it 'should be reached successfully' do
      #binding.pry
      #expect(page.status_code).to eq(200)
    #end
  #end
#end

    #describe 'maps' do
      #it 'should display google maps' do
        #page.should have_css('div', :id => 'map')
      #end

       #Checking to see if View propogated venues that map is using
      #it 'should display a location' do
        #page.should have_css('h5', :class => 'card-title')
      #end
    #end

    #describe 'sidebar' do
      #describe 'menu' do
        #it 'should have a menu' do
          #page.should have_css('div', :id => 'mySidebar')
        #end

        #it 'should have an option to login' do
          #page.should have_css('button', :text => 'Log in/out')
        #end

        #it 'should have an option to sign up' do
          #page.should have_css('button', :text => 'Create Account')
        #end
      #end

      #it 'should have an itinerary' do
        #page.should have_css('div', :class => 'card-header')
      #end

      #it 'should have a generate button' do
        #page.should have_css('button', :id => 'Generate')
      #end

      #it 'should have a like button' do
        #page.should have_css('a', :id => 'like')
      #end

      #it 'should have a dislike button' do
        #page.should have_css('a', :id => 'dislike')
      #end

      #it 'should have a save current itinerary button' do
        #page.should have_css('button', :text => 'Save Itinerary')
      #end

      #it 'should have a link to saved itineraries' do
        #page.should have_css('button', :text => 'View Saved Itineraries')
      #end

    #end
  #end
#end
