#include <bits/stdc++.h>

using namespace std;

int memo[25][105];
vector<int> p;

int fr(int i, int w) {

  if (w == 0)
    return true;
  if (w < 0 || i == (int)p.size())
    return false;

  if (memo[i][w] != -1)
    return memo[i][w];

  int res = fr(i + 1, w - p[i]) || fr(i + 1, w);
  return memo[i][w] = res;
}

bool check_parity() {
  int sum = 0;

  for (int peso : p) {
    sum += peso;
  }

  if (sum % 2 != 0)
    return false;

  memset(memo, -1, sizeof(memo));
  return fr(0, sum / 2);
}

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int tc;
  if (!(cin >> tc))
    return 0;

  string line;

  getline(cin, line);

  while (tc--) {

    getline(cin, line);

    stringstream ss(line);
    int peso;

    p.clear();

    while (ss >> peso) {
      p.push_back(peso);
    }

    if (check_parity()) {
      cout << "YES\n";
    } else {
      cout << "NO\n";
    }
  }

  return 0;
}
