#!/usr/bin/ruby 

require 'rubygems'
require 'eventmachine'

class Connector < EM::Connection 
  def post_init
    puts "Getting /"
    send_data "GET / HTTP/1.1\r\nHost: MagicBob\r\n\r\n"
  end 

  def receive_data(data)
    puts "Received #{data.length} bytes"
    puts "Received #{data} "
  end 

end

EM.run do 
  EM.connect("localhost",10000,Connector)
end 

