class HomepageController < ApplicationController
  def index
    @locs = Venue.all.shuffle[0..4]
  end
end
