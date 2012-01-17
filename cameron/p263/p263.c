#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "integer.h"
#include "miller-rabin.c"

int problem263(void);

int main(int argc, char** argv) {
  problem263();
  return 0;
}

int problem263()
{
  integer testnum = string_to_integer("5");
  integer testnum_helper = string_to_integer("5");
  integer two = string_to_integer("2");
  integer total_src = string_to_integer("0");
  integer total_tar = string_to_integer("0");
  integer target_dif = string_to_integer("6");
  integer dif = string_to_integer("0");

  int found = 0;
  integer lastprime = string_to_integer("5");
  //int sexy_count = 0;
  printf("text here\n");
  while (found < 4) {
    //printf("gets 1\n");
    if (miller_rabin(testnum) == PRIME) {
      subtract_integer(testnum, lastprime, dif);
      if (compare_integers(dif, target_dif) == 0) {
        printf("difference between %s and %s is six\n", 
                integer_to_string(testnum), integer_to_string(lastprime));
        found++;
      }else {
        found = 1;
      }
      copy_integer(testnum, lastprime);
      add_integer(total_src, testnum, total_tar);
      copy_integer(total_tar, total_src);
      printf("Total is %s\n", integer_to_string(total_tar));
    }
    add_integer(testnum_helper, two, testnum);
    copy_integer(testnum, testnum_helper);
    printf("Tested %s\n", integer_to_string(testnum));
  }
  return 0;
}


/*
int main(int argc, char* argv[]) {
  srand(time(NULL));
    if (strcmp(argv[1], "test") == 0) {
      integer n = string_to_integer(argv[2]);
        puts(miller_rabin(n) == PRIME ? "PRIME" : "COMPOSITE");
    } else if (strcmp(argv[1], "genprime") == 0) {
        integer max = create_integer(atoi(argv[2])/COMPONENT_BITS);
        integer p   = create_integer(max.num_components);
        set_zero_integer(max);
        max.c[max.num_components-1] = MAX_COMPONENT;
      do {
        random_integer(max, p);
        if ((p.c[0] % 2) == 0) continue;
        //if (mod_small_integer(p, 3) == 0) continue;
        //if (mod_small_integer(p, 5) == 0) continue;
        if (mod_small_integer(p, 7) == 0) continue;
        if (mod_small_integer(p, 61) == 0) continue;

      } while (miller_rabin(p) == COMPOSITE);
      puts(integer_to_string(p));
    }
    return 0;
}

*/
