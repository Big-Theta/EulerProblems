require 'open-uri'

def next_nothing nothing
    puts '> next_nothing ' + nothing.to_s
    page = open("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing.to_s).readlines[0]

    case page
    when /nothing is ((\d)+)/
        next_n = $1
        puts "found " + next_n.to_s
    #when
    else
        puts "why am I here?"
        puts 'Page is: ' + page.to_s
    end

    yield next_n
end

next_nothing(

1000.times {next_nothing 12345}
