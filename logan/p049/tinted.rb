require 'prime'

def permute n
    my_list = []
    val = n.to_s
    val.each_char {|c| my_list.push c}
    my_list.permutation do |perm|
        yield perm.to_s.to_i
    end
end

def candidates n
    my_list = []
    permute(n) {|x| my_list.push(x) if x.prime?}
    my_list
end

def all_candidates
    (1000..9999).each do |x|
        cand = candidates x
        yield cand if cand.length >= 3
    end
end

def filter_arithmetic cand_list
    seq = []
    cand_list.each_with_index do |val, i|
        cand_list[(i + 1)..-1].each do |other|
            dif = (val - other).abs
            if seq.include? dif
                break if val == other
                if cand_list.include?([val, other].min - dif)
                    puts [val, other, [val, other].min - dif].sort.join
                end

                if cand_list.include?([val, other].max + dif)
                    puts [val, other, [val, other].max + dif].sort.join
                end
            end
            seq.push dif
        end
    end
end

if __FILE__ == $0
    #puts candidates 1234
    all_candidates do |cand|
        filter_arithmetic cand
    end
end
