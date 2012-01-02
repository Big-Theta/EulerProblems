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
            matrix[[x, y]] = val.to_i

            x_ = x if x > x_
            y_ = y if y > y_
        end
    end

    return [x_, y_], matrix
end

# Parses the matrix file into a hash. Thus, matrix[[79, 79]] == bottom_right_val
def gimme_matrix
    matrix = {}
    x_, y_ = 0, 0

    open('matrix.txt', 'r').readlines.each_with_index do |line, y|
        line.strip.split(',').each_with_index do |val, x|
            val.strip!
            matrix[[x, y]] = val.to_i

            x_ = x if x > x_
            y_ = y if y > y_
        end
    end

    return [x_, y_], matrix
end

class Is_in
    include Comparable

    attr_reader :my_val, :x, :y
    # Expect: weight to this path, (x, y), matrix
    def initialize obj
        @obj = obj
        @my_val = obj[0]
        @x, @y = obj[1][0], obj[1][1]
        @matrix = obj[2]
        @maxc = obj[3]  # maxc-oordinates
    end

    def done
        return @x == @maxc[0] ? true : false
    end

    def gen
        ret = []

        #[[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]].each do |x_, y_|
        [[@x + 1, @y], [@x, @y + 1], [@x, @y - 1]].each do |x_, y_|
            #puts "--- #{x_}, #{y_} -- #{@x}, #{@y}"
            yield Is_in.new([@my_val + @matrix[[x_, y_]], [x_, y_], @matrix, @maxc]) if @matrix[[x_, y_]]
            #ret.push tmp if @matrix[[x_, y_]]
            #puts "#{tmp.my_val}, #{x_}, #{y_}" if @matrix[[x_, y_]]
            #puts '---+'
        end
        #puts @my_val
    end

    def [] val
        return @obj[val]
    end

    def <=> other
        @my_val <=> other.my_val
    end
end

def m_sort tree
    tree.sort! {|x, y| x[0] <=> y[0]}
end

def conquor maxc, matrix
    seen = {}

    explore = []

    (0..maxc[1]).each do |num|
        seen[[0, num]] = true
        explore.unshift Is_in.new [matrix[[0, num]], [0, num], matrix, maxc]
    end

    while true
        explore.sort!
        tmp = explore.shift

        return tmp if tmp.done

        tmp.gen do |element|
            if not seen[[element.x, element.y]]
                seen[[element.x, element.y]] = true
                explore.unshift element
            end
        end

        explore.sort!
    end
end

if __FILE__ == $0
    puts conquor(*gimme_matrix).my_val
end
