=begin
"a" → "aRbFR"
"b" → "LFaLb"
=end

$x = 0
$y = 0
$d = 0
$steps = 0

=begin
     0
   1 d 3
     2
=end

def left!
    $d = ($d + 1) % 4
end

def right!
    $d = ($d - 1) % 4
end

def forward!
    case $d
    when 0
        $y += 1
    when 1
        $x -= 1
    when 2
        $y -= 1
    when 3
        $x += 1
    else
        puts "why am I here?"
    end

    $steps += 1
end

$start = Time.new

def gen_str val
    seed = "Fa"
    val.times do |i|
        puts "Iteration: #{i}"
        seed.gsub! 'a', 'A'
        seed.gsub! 'b', 'B'
        seed.gsub! 'A', 'aRbFR'
        seed.gsub! 'B', 'LFaLb'
    end

    return seed
end


def foo n_steps
    x = 0
    while 2 ** x < n_steps do
        x += 1
    end

    puts "x: #{x}"

    seed = gen_str x

    seed.each_char do |c|
        case c
        when 'a'
        when 'b'
        when 'L'
            left!
        when 'R'
            right!
        when 'F'
            forward!
        else
            puts "C: #{c} Why wasn't this made clear?"
        end

        if $steps % 1024 == 0 or $steps == n_steps
            puts "Step #{$steps} Time: #{Time.new - $start} sec -- x: #{$x} y: #{$y}"
            if $steps == n_steps
                puts Time.new - $start
                puts "RESULT -- x: #{$x}, y: #{$y}"
                exit
            end
        end
    end

    puts "Reached the end of the string after #{$steps} steps."
end

foo 100000

puts Time.new - $start
