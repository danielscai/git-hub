#!/usr/bin/ruby 

require 'rubygems'
require 'eventmachine'

class Pass < EM::Connection 
  attr_accessor :a,:b
  
  def receive_data(data)
    send_data "#{@a} #{data.chomp} #{b}"
  end 
end 


EM.run do 
  EM.start_server("0.0.0.0",10000,Pass) do |conn|
    conn.a="Goodby"
    conn.b="world"
  end 

end
