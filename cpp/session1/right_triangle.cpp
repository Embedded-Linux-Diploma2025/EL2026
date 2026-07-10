#include <algorithm>
#include <cassert>
#include <iostream>
#include<limits>
#include<cmath>

int getMax(int num1,int num2,int num3)
{
    int max = std::numeric_limits<int>::min();
    if(max < num1)
    {
        max = num1;
    }
    if(max < num2)
    {
        max = num2;
    }
    if(max < num3)
    {
        max = num3;
    }

    return max;
}

int ipow(int base,int exponent)
{
    return static_cast<int>(pow(base,exponent));
}

bool isRightTriangle(int a, int b, int c) {
  unsigned int max = getMax(a,b,c);
  bool answer = false;
  if(a == max)
  {
    answer = ipow(a,2) == (ipow(b,2) + ipow(c,2));
  }
  else if(b == max)
  {
    answer = ipow(b,2) == (ipow(a,2) + ipow(c,2));
  }
  else
  {
    answer = ipow(c,2) == (ipow(b,2) + ipow(a,2));
  }

  return answer;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "      RIGHT ANGLE TRIANGLE CHECKER\n";
  std::cout << "==============================================\n\n";

  // Test the isRightTriangle function
  // Test classic Pythagorean triples
  assert(isRightTriangle(3, 4, 5) == true);
  assert(isRightTriangle(4, 3, 5) == true);
  assert(isRightTriangle(5, 3, 4) == true);
  assert(isRightTriangle(5, 4, 3) == true);

  // Test other Pythagorean triples
  assert(isRightTriangle(5, 12, 13) == true);
  assert(isRightTriangle(12, 5, 13) == true);
  assert(isRightTriangle(13, 12, 5) == true);

  assert(isRightTriangle(8, 15, 17) == true);
  assert(isRightTriangle(15, 8, 17) == true);
  assert(isRightTriangle(17, 15, 8) == true);

  assert(isRightTriangle(7, 24, 25) == true);
  assert(isRightTriangle(24, 7, 25) == true);

  // Test scaled Pythagorean triples
  assert(isRightTriangle(6, 8, 10) == true);   // 3-4-5 * 2
  assert(isRightTriangle(9, 12, 15) == true);  // 3-4-5 * 3
  assert(isRightTriangle(10, 24, 26) == true); // 5-12-13 * 2

  // Test non-right triangles
  assert(isRightTriangle(1, 2, 3) == false);
  assert(isRightTriangle(2, 3, 4) == false);
  assert(isRightTriangle(5, 6, 7) == false);
  assert(isRightTriangle(1, 1, 1) == false);
  assert(isRightTriangle(2, 2, 2) == false);

  // Test invalid triangles (violate triangle inequality)
  assert(isRightTriangle(1, 1, 5) == false);
  assert(isRightTriangle(1, 2, 4) == false);
  assert(isRightTriangle(10, 1, 1) == false);

  std::cout
      << "\n\n[✓] All tests passed! Right triangle checker works correctly.\n";
  std::cout << "Function correctly identifies right triangles using "
               "Pythagorean theorem.\n";

  return 0;
}
