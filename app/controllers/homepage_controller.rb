class HomepageController < ApplicationController
  def index
    @locs = [
      {:lat => 41.7886, :lng => -87.5987},
      {:lat => 41.8001, :lng => -87.5961},
      {:lat => 41.7913, :lng => -87.5938},
      {:lat => 41.7906, :lng => -87.5831}
    ]
  end
end
