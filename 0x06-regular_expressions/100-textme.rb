#!/usr/bin/env ruby
puts ARGV[0].scan(/\[\w*:(\w*)\] \[\w*:(\+\d*)\] \[\w*:(-1:0:-1:0:-1)\]/).join(',')
