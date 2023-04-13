#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const nums = args.map(num => parseInt(num));
  nums.sort((a, b) => a - b);
  console.log(nums[nums.length - 2]);
}
