require "faceted.rb"

# [up, left, down, right]
def problem81
  m, m_dim = gimme_matrix
  min_path = {}
  (0..m_dim[1]).each do |y|
    (0..m_dim[0]).each do |x|
      if x == 0 and y == 0
        min_path[[x, y]] = m[[x, y]]
      elsif x == 0
        min_path[[x, y]] = m[[x, y]] + min_path[[x, y - 1]]
      elsif y == 0
        min_path[[x, y]] = m[[x, y]] + min_path[[x - 1, y]]
      else
        min_path[[x, y]] = m[[x, y]] + [min_path[[x - 1, y]], min_path[[x, y - 1]]].min
      end
    end
  end
  min_path[[m_dim[0], m_dim[1]]]
end
