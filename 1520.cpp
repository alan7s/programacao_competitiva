#PROBLEMA: 1520 - Parafusos e Porcas
#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>
#include <stdio.h>

using namespace std;
 
int main() {
    
    // armazena range de parafusos
    vector<int> parafusos;
    
    int qtde = 0;
    while (std::cin >> qtde) {
        //cin >> qtde;
    
        int count = 0;
    
        while (count < qtde){
    
            int rangeStart, rangeEnd;
    
            cin >> rangeStart;
            cin >> rangeEnd;
          
            for(int i = rangeStart; i <= rangeEnd; i++){
                parafusos.push_back(i);
            }
    
            count++;
        }
    
        sort(parafusos.begin(), parafusos.end());
    
        int parafuso_alvo;
        cin >> parafuso_alvo;
    
        vector<int>::iterator lower, upper;
        lower = lower_bound(parafusos.begin(), parafusos.end(), parafuso_alvo);
        upper = upper_bound(parafusos.begin(), parafusos.end(), parafuso_alvo);
        
        int low, up;
        
        low = lower-parafusos.begin();
        up = upper-parafusos.begin()-1;

        //printf("lower %d\n", lower-parafusos.end());
        //printf("upper %d\n", upper-parafusos.end());
    
        if(low == (up+1)) {
            printf("%d not found\n",parafuso_alvo);       
        }else{
            printf("%d found from %d to %d\n",parafuso_alvo,low,up);    
        }
        parafusos.clear();
    }
    return 0;
}
