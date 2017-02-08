class RoadBike < Bicycle
  attr_reader :tape_color

  def initialize(args)
    @tape_color  = args[:tape_color]
    super(args)
  end

  def spares
    {
      chain: '10-speed',
      tire_size: '23',
      tape_color: tape_color,
    }
  end

  def default_tire_size
    '23'
  end
end
