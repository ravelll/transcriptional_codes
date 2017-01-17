require './chapter3/dfa.rb'

rulebook = DFARulebook.new([
  FARule.new(1, 'a', 2), FARule.new(1, 'b', 1),
  FARule.new(2, 'a', 2), FARule.new(2, 'b', 3),
  FARule.new(3, 'a', 3), FARule.new(3, 'b', 3),
])

puts "rulebook.next_state(1, 'a') should return 2"
puts rulebook.next_state(1, 'a') == 2 ? 'OK' : "Failed"

puts "rulebook.next_state(1, 'b') should return 1"
puts rulebook.next_state(1, 'b') == 1 ? 'OK' : "Failed"

puts "rulebook.next_state(2, 'b') should return 3"
puts rulebook.next_state(2, 'b') == 3 ? 'OK' : "Failed"
