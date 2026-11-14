package dsa.arrays;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class TwoSumTest {

    @Test
    void findsPair() {
        assertArrayEquals(new int[] {0, 1}, TwoSum.solve(new int[] {2, 7, 11, 15}, 9));
    }

    @Test
    void handlesDuplicates() {
        assertArrayEquals(new int[] {0, 1}, TwoSum.solve(new int[] {3, 3}, 6));
    }

    @Test
    void noAnswerReturnsEmpty() {
        assertArrayEquals(new int[0], TwoSum.solve(new int[] {1, 2}, 10));
    }
}
