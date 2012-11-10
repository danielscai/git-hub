#!/usr/bin/ruby 

require 'rubygems'
require 'eventmachine'

EM.run do 
  p=EM::PeriodicTimer.new(1) do 
    puts "Tick .."
  end 

  EM::Timer.new(5) do 
    puts "BOOM" 
    p.cancel
  end 

  EM::Timer.new(8) do 
    puts "The googles, the do nothing"
    EM.stop
  end
end
