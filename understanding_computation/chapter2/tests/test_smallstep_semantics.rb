require './chapter2/smallstep_semantics.rb'

statement = Sequence.new(
  Assign.new(:x, Boolean.new(true)),
  Assign.new(:x, Add.new(Variable.new(:x), Number.new(1)))
)
environment = {}
Machine.new(statement, environment).run
