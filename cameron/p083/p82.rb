require "faceted.rb"

def problem82
  m, m_dim = gimme_matrix
  prev_col = []
  (0..m_dim[1]).each do |y|
    prev_col[y] = m[[0, y]]
  end
  (1..m_dim[0]).each do |x|
    curr_col = []
    (0..m_dim[1]).each do |y|
      curr_col.push(m[[x, y]])
    end
    prev_col = min_vertical(prev_col, curr_col)
  end
  prev_col.min
end

def min_vertical(prev_col, curr_col)
  dim = prev_col.size - 1
  down = []
  answer = []
  down[0] = prev_col[0] + curr_col[0]
  (1..dim).each do |y|
    down[y] = curr_col[y] + [prev_col[y], down[y - 1]].min
  end
  answer[dim] = [prev_col[dim] + curr_col[dim], down[dim - 1] + curr_col[dim]].min
  (1..dim).each do |y|
    y = dim - y
    answer[y] = [curr_col[y] + [prev_col[y], answer[y + 1]].min, down[y]].min
  end
  answer
end
