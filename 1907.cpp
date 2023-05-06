//PROBLEMA: 1907 - Coloração de Cenários de Jogos
#include <bits/stdc++.h>
using namespace std;

const int MAX = 1030;

int n, m;
char img[MAX][MAX];
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

bool checkGrid(int x, int y){
    if( x < 0 || x >= n || y < 0 || y >= m)
        return false;
    return img[x][y] == '.';
}

void dfs(int x, int y, char color) {
    stack<pair<int, int>> st;
    st.push(make_pair(x, y));
    while(!st.empty()){
        pair<int, int> p = st.top();
        st.pop();
        int x = p.first;
        int y = p.second;
        img[x][y] = color;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(checkGrid(nx, ny)) {
                st.push(make_pair(nx, ny));
            }
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> img[i];
    }
    int clicks = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (img[i][j] == '.') {
                clicks++;
                dfs(i, j, 'o');
            }
        }
    }
    cout << clicks << endl;
    return 0;
}
