#!/usr/bin/ruby 

require 'rubygems'
require 'eventmachine'

EM.run do 
  EM.add_timer(5) do 
    puts "BOOM"
    EM.stop_event_loop 
  end 

  EM.add_periodic_timer(1) do 
    puts "Tick .."
  end 
end 


