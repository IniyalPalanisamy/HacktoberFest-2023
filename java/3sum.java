import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        
        // Check for null or too few elements
        if (nums == null || nums.length < 3) {
            return result;
        }

        // Sort the array to facilitate the two-pointer approach
        Arrays.sort(nums);

        // Iterate through the sorted array
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicate values for 'i'
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue; 
            }
            int target = -nums[i]; // Target for the two-pointer search
            int left = i + 1; // Left pointer
            int right = nums.length - 1; // Right pointer

            // Two-pointer approach to find pairs that sum to the target
            while (left < right) {
                int sum = nums[left] + nums[right];
                if (sum == target) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;

                    // Skip duplicates for the left pointer
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                    // Skip duplicates for the right pointer
                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                } else if (sum < target) {
                    left++; // Move left pointer to increase the sum
                } else {
                    right--; // Move right pointer to decrease the sum
                }
            }
        }

        return result; // Return the list of triplets
    }

    public static void main(String[] args) {
        ThreeSum solution = new ThreeSum();
        int[] nums = {-1, 0, 1, 2, -1, -4}; // Example input
        List<List<Integer>> result = solution.threeSum(nums);

        // Print the resulting triplets
        for (List<Integer> triplet : result) {
            System.out.println(triplet);
        }
    }
}
