import sys


def count_triplets_sum_zero(arr):
  arr.sort()
  n = len(arr)
  count = 0

  for i in range(n - 2):
    if arr[i] > 0:
      break

    l = i + 1
    r = n - 1

    while l < r:
      s = arr[i] + arr[l] + arr[r]
      if s < 0:
        l += 1
      elif s > 0:
        r -= 1
      else:
        if arr[l] == arr[r]:
          m = r - l + 1
          count += m * (m - 1) // 2
          break

        left_count = 1
        right_count = 1

        while l + 1 < r and arr[l] == arr[l + 1]:
          left_count += 1
          l += 1

        while r - 1 > l and arr[r] == arr[r - 1]:
          right_count += 1
          r -= 1

        count += left_count * right_count
        l += 1
        r -= 1

  return count


def solve():
  data = list(map(int, sys.stdin.buffer.read().split()))
  it = iter(data)
  t = next(it)
  out = []

  for _ in range(t):
    n = next(it)
    arr = [next(it) for _ in range(n)]
    out.append(str(count_triplets_sum_zero(arr)))

  sys.stdout.write("\n".join(out))


if __name__ == "__main__":
  solve()
