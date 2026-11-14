package dsa.arrays;

import java.util.HashMap;
import java.util.Map;

/**
 * Two Sum
 *
 * Difficulty: Easy
 * Approach: one pass with a HashMap of value -> index; look up the complement.
 * Time: O(n)   Space: O(n)
 */
public class TwoSum {

    public static int[] solve(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer j = seen.get(target - nums[i]);
            if (j != null) {
                return new int[] {j, i};
            }
            seen.put(nums[i], i);
        }
        return new int[0];
    }

    public static void main(String[] args) {
        int[] result = solve(new int[] {2, 7, 11, 15}, 9);
        System.out.println(result[0] + ", " + result[1]);
    }
}
