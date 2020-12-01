/*
Generate Fibonacci sequence using an 
iterative method (with loops):
*/

function getFib(position) {
  if (position == 0) { return 0; }
  if (position == 1) { return 1; }

  let first = 0, second = 1,
    next = first + second;

  for (let i = 2; i < position; i++) {
    first = second;
    second = next;
    next = first + second;
  }
  return next;
}