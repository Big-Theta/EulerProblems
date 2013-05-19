#!/usr/bin/python3

def gen_digits():
   num = 1234
   while num < 10000:
      num_str = str(num)
      digits = [int(num_str[0]),
                int(num_str[1]),
                int(num_str[2]),
                int(num_str[3])
      ]

      if ((sorted(digits) == digits)
          and (len(set(digits)) == 4)):
         yield digits
      num += 1


def max_obtainable(digit_list):
   answers = []
   if len(digit_list) < 2:
      answers = digit_list
   else:
      for idx, val in enumerate(digit_list):
         for retval in max_obtainable(digit_list[:idx] + digit_list[idx + 1:]):
            potentials = []
            potentials += [val + retval]
            potentials += [val - retval]
            potentials += [val * retval]
            potentials += [int(val / retval)]
            for p in potentials:
               if p > 0:
                  answers += [p]
      answers = sorted(list(set(answers)))
   return answers


def p93():
   answer = 0
   best_list = []
   a = gen_digits()
   for digit_list in gen_digits():
      curr_max = 0
      for a_i, a_v in enumerate(max_obtainable(digit_list)):
         if a_v == a_i + 1:
            #print("%i, %i" % (answer, a_i + 1))
            curr_max = a_i
      if curr_max > answer:
         print(max_obtainable(digit_list))
         answer = curr_max
         best_list = digit_list
   print(answer)
   print(best_list)

if __name__ == "__main__":
   p93()

