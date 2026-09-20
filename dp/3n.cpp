#include <bits/stdc++.h>

using namespace std;

map<int, int> dict;

int collatz(int n) {

  if (n == 1)
    return 1;

  if (dict.find(n) != dict.end()) {
    return dict[n];
  }

  int nextN;

  if (n % 2 == 0) {
    nextN = n / 2;
  } else {
    nextN = 3 * n + 1;
  }

  dict[n] = 1 + collatz(nextN);
  return dict[n];
}

int max_coll(int n, int m) {
  if (n > m) {
    swap(m, n);
  }

  int max_seq = 0;

  for (int i = n; i <= m; i++) {
    int sl = collatz(i);
    if (sl > max_seq) {
      max_seq = sl;
    }
  }
  return max_seq;
}

int main() {

  int n, m;
  while (cin >> n >> m) {
    int result = max_coll(n, m);
    cout << n << ' ' << m << ' ' << result << '\n';
  }
  return 0;
}
