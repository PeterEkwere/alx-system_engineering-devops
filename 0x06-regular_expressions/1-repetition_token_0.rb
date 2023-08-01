#!/usr/bin/env ruby

name = ARGV[0]

regex = /hbt{2,}n/
if name =~ regex
  puts "#{name}"
else
  puts ""
end
