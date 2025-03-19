#include <bits/stdc++.h>

using namespace std;

int N;
int paper[2200][2200];
int cnt[3];

bool check(int x, int y, int n){
    for(int i = x; i < x + n; i++)
    for(int j = y; j < y + n; j++)
        if(paper[x][y] != paper[i][j])
            return false;
    return true;
}

void func(int x, int y, int z){
    if(check(x, y, z)){
        cnt[paper[x][y] + 1] += 1;
        return;
    }
    int n = z / 3;
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            func(x + i * n, y + j * n, n);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    //1. 종이가 같으면 그대로 사용
    //2. 같지 않으면 같은 크기 9개로 자르고 종이가 같으면 그대로 사용
    cin >> N;
    for(int i = 0; i < N; i++)
        for (int j = 0; j < N; ++j) {
            cin >> paper[i][j];
        }
    func(0, 0, N);

    for(int i = 0; i < 3; i++){
        cout << cnt[i] << "\n";
    }

    return 0;
}
