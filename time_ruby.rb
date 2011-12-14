require 'time'
require 'mr'

$dur = 2

def timeit #func
    start = Time.new
    i = 0

    while i < 1_000_000 do
        i += 1
    end

    Time.new - start
end

if __FILE__ == $0 then
    puts timeit
end
