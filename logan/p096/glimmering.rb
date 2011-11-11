class Spot
    attr_accessor :x, :y, :maybe
end

class Puzzle
    attr_accessor :board
    def initialize puzzle_hash
        @board = {}
        puzzle_hash.each_pair {|index, val| self[index] = val}
    end

    def [] index
        @board[index]
    end

    def []= index, val
        @board[index] = val
    end

    def to_s
        (1..9).each do |i|
            (1..9).each do |j|
                print "(#{i}, #{j}): " + self[[i, j]].to_s
            end
            puts
        end
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
        puts 'r: ' + row.to_s
        row += 1
    end

    return all_puzzles
end

all_puzzles = parse_file
a = Puzzle.new all_puzzles[1]

all_puzzles[1].each_pair do |a, b|
    puts "a: (#{a}) b: (#{b})"
end

puts a
puts all_puzzles[3][[1,7]]
