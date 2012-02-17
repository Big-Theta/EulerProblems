require "faceted"

def problem83
  m, m_dim = gimme_matrix
  path_sum = Hash.new(2**32)
  path_sum[[0, 0]] = m[[0, 0]]
  current_column = 0
  while current_column < m_dim[0] + 1
    current_column = update_column(current_column, path_sum, m, m_dim[0], m_dim[1])
  end
  path_sum[[m_dim[0], m_dim[1]]]
end

def update_column(x, path_sum, m, dim_x, dim_y)
  modified = false
  0.upto(dim_y) do |y|
    possible = m[[x, y]] + min_adjacent(x, y, path_sum)
    if possible < path_sum[[x, y]]
      modified = true
      path_sum[[x, y]] = possible
    end
  end
  if modified and x > 0
    update_column(x - 1, path_sum, m, dim_x, dim_y)
  else
    x + 1
  end
end

def min_adjacent(x, y, ps)
  [ps[[x - 1, y]], ps[[x + 1, y]], ps[[x, y - 1]], ps[[x, y + 1]]].min
end

if __FILE__ == $0
    require 'time'
    start = Time.now
    puts problem83
    puts Time.now - start
end
