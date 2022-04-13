#include <gtest/gtest.h>
#include "A/index.h"
#include "B/lib.h"

TEST (tast_index, tast1) {
    ASSERT_EQ(sum2_2(), 4); }
TEST (tast_lib, tast2) {
    ASSERT_EQ(mult(4, 2), 8);
    ASSERT_EQ(mult(7, 7), 49);
}
