class PagesController < ApplicationController
    def index
      @pts = [
        {:lat => 41.7886, :lng => -87.5987},
        {:lat => 41.7906, :lng => -87.5831}
      ]

      @locs = [
        {:lat => 41.8001, :lng => -87.5961},
        {:lat => 41.7913, :lng => -87.5938}
      ]
      @i = 2
    end
  end
