#!/usr/bin/env ruby
# By Mkweb
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
