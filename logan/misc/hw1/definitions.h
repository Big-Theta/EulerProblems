#ifndef HW1_DEFINITIONS_H_
#define HW1_DEFINITIONS_H_

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <fstream>  // NOLINT
#include <iomanip>
#include <iostream>  // NOLINT
#include <sstream>
#include <string>

using ::std::cout;
using ::std::endl;
using ::std::string;
using ::std::stringstream;
using ::std::setw;
using ::std::ifstream;
using ::std::ofstream;

/* ENHANCEMENT:
 * This really would be an obvious candidate for a class.
 * This is currently coded in C style using streams. A class
 * with the index operator overloaded and flippable based on some
 * instance variable would be kinda slick.
 */

int** create(int rows, int cols);
void destroy(int **arr_2d, int rows);
int** clone(int **arr_2d, int rows, int cols);
int** rotate_left(int **arr_2d, int rows, int cols);
int** rotate_right(int **arr_2d, int rows, int cols);
string to_str(int **arr_2d, int rows, int cols);
int** read_from_file(string fname, int* rows, int* cols);
void save_to_file(string fname, int** arr_to_save, int rows, int cols);

#endif  // HW1_DEFINITIONS_H_

