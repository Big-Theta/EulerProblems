class Puzzle
    attr_accessor :board
    def initialize puzzle_hash
        @board = {}
        puzzle_hash.each_pair {|index, val| self[index] = val}
        filter 1, ???
    end

    def filter group, loc
        x, y = loc[0], loc[1]
        done = true

        self.each_spot(group) do |a_x, a_y|
            pos = self[a_x, a_y]
            print pos

            # each element in my_spot...
            self.each_spot(group) do |b_x, b_y|
                next if a_x == b_x and a_y == b_y
                end
            end
        end
    end

    def get_group group
        if (1..9).include? group  # Square
            x, y = (1..3), (1..3) if group == 1
            x, y = (4..6), (1..3) if group == 2
            x, y = (7..9), (1..3) if group == 3

            x, y = (1..3), (4..6) if group == 4
            x, y = (4..6), (4..6) if group == 5
            x, y = (7..9), (4..6) if group == 6

            x, y = (1..3), (7..9) if group == 7
            x, y = (4..6), (7..9) if group == 8
            x, y = (7..9), (7..9) if group == 9
        elsif (10..18).include? group  # Row
            x, y = [group - 9], (1..9)
        elsif (19..27).include? group  # Col
            x, y = (1..9), [group - 18]
        else
            puts "improper group value sent to get_group: #{group}"
        end
        return x, y
    end

    def each_spot group
        x, y = get_group group
        x.each do |my_x|
            y.each do |my_y|
                yield(my_x, my_y)
            end
        end
    end

    def [] index
        @board[index]
    end

    def []= index, val
        @board[index] = val
    end

    def to_s
        puts '> to_s'
        (1..9).each do |i|
            (1..9).each do |j|
                print "(#{i}, #{j}): " + self[[i, j]].to_s + " "
            end
        end
        puts '< to_s'
    end
end

def parse_file
    all_puzzles = {}
    puz = nil
    row = nil
    col = nil

    File.open('sudoku.txt').each do |line|
        if line =~ /Grid (\d+)/ then
            all_puzzles[$1.to_i] = {}
            puz = $1.to_i
            row = 1
            next
        end

        col = 1
        line.each_char do |c|
            if col > 9 then
                break
            elsif c.to_i == 0 then
                all_puzzles[puz][[row, col]] = (1..9).entries
            else
                all_puzzles[puz][[row, col]] = [c.to_i]
            end
            col += 1
        end
        row += 1
    end

    return all_puzzles
end

all_puzzles = parse_file
=begin
x = Puzzle.new all_puzzles[1]

all_puzzles[1].each_pair do |a, b|
    puts "a: (#{a}) b: (#{b})"
end

puts '--------------'

puts x.to_s
=end
a = Puzzle.new all_puzzles[1]

#puts a
#puts all_puzzles[3][[1,7]]
