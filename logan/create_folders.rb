#!/usr/bin/ruby -w

def create_problem_folders(problems)
    %x/mkdir project_euler/

    problems.each do |problem|
        %x/mkdir #{"project_euler/p" +
            problem.to_s.rjust(3, '0')}/
    end
end

def remove_problem_folders()
    %x/ls/.each do |folder|
        %x/rmdir #{folder}/
    end
end

#remove_problem_folders()
problems = [1, 2, 4, 6, 16, 20]
create_problem_folders(problems)
