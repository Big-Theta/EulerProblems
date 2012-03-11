$layers = []

def layer_list my_list
    if my_list.inject(:+) == 32
        puts 'here'
        $layers.push(my_list.clone)
    end

    if my_list.inject(:+) + 2 <= 32
        puts 'here'
        puts my_list.length
        puts my_list.join(', ')
        for_recurse = my_list.clone.push(2)
        layer_list for_recurse
    end

    if my_list.inject(:+) + 3 <= 32
        puts 'there'
        puts my_list.length
        puts my_list.join(', ')
        layer_list my_list.clone.push(3)
    end
end

if __FILE__ == $0
    layer_list list()
    puts layers.length
end
