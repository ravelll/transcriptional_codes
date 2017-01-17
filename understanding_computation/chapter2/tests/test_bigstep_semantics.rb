require './chapter2/bigstep_semantics.rb'
require 'pp'

statement = While.new(
  LessThan.new(Variable.new(:x), Number.new(5)),
  Assign.new(:x, Multiply.new(Variable.new(:x), Number.new(3)))
)

pp statement

pp statement.evaluate({ x: Number.new(1) })
