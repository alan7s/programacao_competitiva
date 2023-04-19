#PROBLEMA: 1932 - Bolsa de Valores
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, c;
    cin >> n >> c;

    vector<int> p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }

    vector<int> lucro(n);

    int lucro_max = -1e9;
    for (int i = 1; i < n; i++) {
        lucro_max = max(lucro_max, lucro[i-1] - p[i-1]);
        lucro[i] = max(lucro[i-1], lucro_max + p[i] - c);
    }

    cout << lucro[n-1] << endl;

    return 0;
}
