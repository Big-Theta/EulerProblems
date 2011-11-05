require 'open-uri'

$strange = []
$count = 0

def next_nothing nothing=12345
    page = open("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing.to_s)
    page = page.readlines.inject('') {|memo, line| memo += line}

    puts "Page #{$count}: " + page.to_s
    $count += 1

    case page
    when /nothing is ((\d)+)/
        next_n = $1
        puts "found " + next_n.to_s
    when /Divide by two/
        next_n = nothing.to_i / 2
        puts "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        puts "Divided #{nothing} by two: next_n == #{next_n}"
    else
        puts "why am I here?"
        $strange.push page.clone
        puts 'Page is: ' + page.to_s
        exit
    end

    next_nothing next_n
end

next_nothing
puts $strange.to_s
