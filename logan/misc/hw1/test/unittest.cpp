#include <string>

#include "gtest/gtest.h"
#include "../definitions.h"

TEST(ArrayManipulationTest, create) {
  int** uut;
  for (int i = 0 ; i < 10 ; i++) {
    for (int j = 0 ; j < 10 ; j++) {
      ASSERT_NO_THROW({
        uut = create(i, j);
      });

      for (int a = 0 ; a < i ; a++) {
        for (int b = 0 ; b < j ; b++) {
          ASSERT_NO_THROW({
            uut[a][b] = a;
          }) << "a: " << a << " b: " << b << endl;
        }
      }
    }
  }
}

TEST(ArrayManipulationTest, destroy) {
  ASSERT_NO_THROW({
    int** uut;
    for (int i = 0 ; i < 10 ; i++) {
      for (int j = 0 ; j < 10 ; j++) {
        uut = create(i, j);
        destroy(uut, i);
      }
    }
  });
}

TEST(ArrayManipulationTest, clone) {
  for (int a = 3 ; a < 10; a++) {
    int** to_clone = create(a, a);
    int count = 0;
    for (int i = 0 ; i < a ; i++) {
      for (int j = 0 ; j < a ; j++) {
        to_clone[i][j] = count++;
      }
    }

    int** uut = clone(to_clone, a, a);

    for (int i = 0 ; i < a ; i++) {
      for (int j = 0 ; j < a ; j++) {
        ASSERT_EQ(to_clone[i][j], uut[i][j]);
      }
    }
  }
}

TEST(ArrayManipulationTest, rotate_left) {
  int a = 4, b = 3;
  int count = 0;
  int** to_rotate = create(a, b);
  for (int i = 0 ; i < a ; i++) {
    for (int j = 0 ; j < b ; j++) {
      to_rotate[i][j] = count++;
    }
  }
  // to_rotate == [0, 1, 2]
  //              [3, 4, 5]
  //              [6, 7, 8]
  //              [9, 10, 11]
  int** to_confirm = create(b, a);
  to_confirm[0][0] = 2;
  to_confirm[0][1] = 5;
  to_confirm[0][2] = 8;
  to_confirm[0][3] = 11;

  to_confirm[1][0] = 1;
  to_confirm[1][1] = 4;
  to_confirm[1][2] = 7;
  to_confirm[1][3] = 10;

  to_confirm[2][0] = 0;
  to_confirm[2][1] = 3;
  to_confirm[2][2] = 6;
  to_confirm[2][3] = 9;

  int** uut = rotate_left(to_rotate, a, b);

  for (int i = 0 ; i < b ; i++) {
    for (int j = 0 ; j < a ; j++) {
      ASSERT_EQ(to_confirm[i][j], uut[i][j]) <<
                "=== to_rotate:" << endl << to_str(to_rotate, a, b) <<
                "=== to_confirm:" << endl << to_str(to_confirm, b, a) <<
                "=== uut:" << endl << to_str(uut, b, a);
    }
  }
}

TEST(ArrayManipulationTest, rotate_right) {
  int a = 4, b = 3;
  int count = 0;
  int** to_rotate = create(a, b);
  for (int i = 0 ; i < a ; i++) {
    for (int j = 0 ; j < b ; j++) {
      to_rotate[i][j] = count++;
    }
  }

  // to_rotate == [0, 1, 2]
  //              [3, 4, 5]
  //              [6, 7, 8]
  //              [9, 10, 11]

  int** to_confirm = create(b, a);
  to_confirm[0][0] = 9;
  to_confirm[0][1] = 6;
  to_confirm[0][2] = 3;
  to_confirm[0][3] = 0;

  to_confirm[1][0] = 10;
  to_confirm[1][1] = 7;
  to_confirm[1][2] = 4;
  to_confirm[1][3] = 1;

  to_confirm[2][0] = 11;
  to_confirm[2][1] = 8;
  to_confirm[2][2] = 5;
  to_confirm[2][3] = 2;

  int** uut = rotate_right(to_rotate, a, b);

  for (int i = 0 ; i < b ; i++) {
    for (int j = 0 ; j < a ; j++) {
      ASSERT_EQ(to_confirm[i][j], uut[i][j]) <<
                "=== to_rotate:" << endl << to_str(to_rotate, a, b) <<
                "=== to_confirm:" << endl << to_str(to_confirm, b, a) <<
                "=== uut:" << endl << to_str(uut, b, a);
    }
  }
}

TEST(ArrayManipulationTest, to_str) {
  int** to_confirm = create(3, 4);
  to_confirm[0][0] = 9;
  to_confirm[0][1] = 6;
  to_confirm[0][2] = 3;
  to_confirm[0][3] = 0;

  to_confirm[1][0] = 10;
  to_confirm[1][1] = 7;
  to_confirm[1][2] = 4;
  to_confirm[1][3] = 1;

  to_confirm[2][0] = 11;
  to_confirm[2][1] = 8;
  to_confirm[2][2] = 5;
  to_confirm[2][3] = 2;

  string expected_str(
      "  9  6  3  0\n"
      " 10  7  4  1\n"
      " 11  8  5  2\n");
  ASSERT_EQ(expected_str, to_str(to_confirm, 3, 4));
}

TEST(ArrayManipulationTest, read_from_file) {
  int** expected = create(3, 4);

  expected[0][0] = 1;
  expected[0][1] = 2;
  expected[0][2] = 3;
  expected[0][3] = 4;

  expected[1][0] = 5;
  expected[1][1] = 6;
  expected[1][2] = 7;
  expected[1][3] = 8;

  expected[2][0] = 9;
  expected[2][1] = 10;
  expected[2][2] = 11;
  expected[2][3] = 12;

  int rows, cols;
  int** uut = read_from_file("test_file.txt", &rows, &cols);
  ASSERT_EQ(to_str(expected, 3, 4), to_str(uut, rows, cols));
}

TEST(ArrayManipulationTest, save_to_file) {
  int** expected = create(3, 4);

  expected[0][0] = 1;
  expected[0][1] = 2;
  expected[0][2] = 3;
  expected[0][3] = 4;

  expected[1][0] = 5;
  expected[1][1] = 6;
  expected[1][2] = 7;
  expected[1][3] = 8;

  expected[2][0] = 9;
  expected[2][1] = 10;
  expected[2][2] = 11;
  expected[2][3] = 12;

  save_to_file(string("test_file_output.txt"), expected, 3, 4);

  int rows, cols;
  int** uut = read_from_file(string("test_file_output.txt"),
                             &rows, &cols);

  ASSERT_EQ(3, rows);
  ASSERT_EQ(4, cols);

  for (int i = 0 ; i < 3 ; i++) {
    for (int j = 0 ; j < 4 ; j++) {
      ASSERT_EQ(expected[i][j], uut[i][j]) <<
                "=== expected:" << endl << to_str(expected, 3, 4) <<
                "=== uut:" << endl << to_str(uut, rows, cols);
    }
  }
}

