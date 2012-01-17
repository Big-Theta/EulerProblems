

def problem19
    total = 0
    today = 2
    cur_month = 0
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1901
    while year < 2001
        while cur_month < 12
            print "day #{today}, month #{cur_month}, year #{year}\n"
            if cur_month == 1 and year % 4 == 0
                days_left_in_month = 29
            else
                days_left_in_month = month_length[cur_month]
            end

            if today % 7 == 0
                total += 1
            end

            while days_left_in_month > 0
                today += 1
                days_left_in_month -= 1
            end
            cur_month += 1
        end
        cur_month = 0
        year += 1
    end
    total
end
