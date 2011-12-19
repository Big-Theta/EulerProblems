def gimme_matrix_dummy
    m = "131 673 234 103 18
         201 96  342 965 150
         630 803 746 422 111
         537 699 497 121 956
         805 732 524 37  331"

    matrix = {}
    x_, y_ = 0, 0

    m.split("\n").each_with_index do |line, y|
        line.split.each_with_index do |val, x|
            val.strip!
            matrix[[x, y]] = val

            x_ = x if x > x_
            y_ = y if y > y_
        end
    end

    return matrix, [x_, y_]
end

# Parses the matrix file into a hash. Thus, matrix[[79, 79]] == bottom_right_val
def gimme_matrix
    matrix = {}
    x_, y_ = 0, 0

    open('matrix.txt', 'r').readlines.each_with_index do |line, y|
        line.strip.split(',').each_with_index do |val, x|
            val.strip!
            matrix[[x, y]] = val

            x_ = x if x > x_
            y_ = y if y > y_
        end
    end

    return matrix, [x_, y_]
end



if __FILE__ == $0
    #matrix = gimme_matrix
    #matrix = gimme_matrix_dummy
    #puts matrix
    #matrix.each {|v| puts v}
end
