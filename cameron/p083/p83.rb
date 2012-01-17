require "faceted"

def problem83
  m, m_dim = gimme_matrix
  path_sum = Hash.new(0)
  path_sum[[0, 0]] = m[[0, 0]]
  (1..m_dim[1]).each do |y|
    path_sum[[0, y]] = m[[0, y]] + path_sum[[0, y - 1]]
  end
  (1..m_dim[0]).each do |x|
    update_min_to_column(x, path_sum, m, m_dim[0], m_dim[1])
  end
  path_sum[[m_dim[0], m_dim[1]]]
end

def update_min_to_column(x, path_sum, m, dim_x, dim_y)
  path_sum[[x, 0]] = path_sum[[x - 1, 0]] + m[[x, 0]]
  1.upto(dim_y) do |y|
    path_sum[[x, y]] = m[[x, y]] + [m[[x, y - 1]], path_sum[[x - 1, y]]].min
  end
  path_sum[[x, dim_y]] = path_sum[[x - 1, dim_y]] + m[[x, dim_y]]
  (dim_y - 1).downto(0) do |y|
    path_sum[[x, y]] = [m[[x, y]] + [path_sum[[x - 1, y]], path_sum[[x, y + 1]]].min, path_sum[[x, y - 1]]].min
  end
end

def update_prev_column(x, path_sum, m, dim_x, dim_y)
  
end
