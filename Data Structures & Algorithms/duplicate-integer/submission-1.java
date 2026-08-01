class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean b = false;
        Set<Integer> set = new HashSet<>();
        for(int i = 0;i<nums.length;i++){
            if(!set.add(nums[i]))
                b = true;
        }
        return b;
    }
}