=begin
How To Write Port Scanner With Ruby

=end

require 'socket' # import socket Ruby Library

print "Enter Host: "
host = gets.chomp
puts "\n"

ports = [21,22,23,80,443] # Ports

for port in ports do
    HOST = ARGV[1] || host # Host
    PORT = ARGV[0] || port # Port
    begin
        socket = TCPSocket.new(HOST,PORT)
        status = "Open" # If Host & Port Connected status = "Open"
    rescue
        status = "Filter" # Else: status = "Filter"
    end
    puts "Port: #{PORT} #{status}"
end
puts "\n"

# Mr.Programmer2938: Ok Thanks For Waching ;)
