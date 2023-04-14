//PROBLEMA: 2449 - Fechadura
#include <iostream>
#include <vector>
 
using namespace std;
 
int main() {
    vector<int> alturasPinos;
    int alturaIdealPino;
    int qtdePinosFechadura;

    cin >> qtdePinosFechadura;
    cin >> alturaIdealPino;
    

    bool soulucaoEncontrada = false;
    int qtdeMovimentos = 0;

    // Armazenando altura dos pinos individualmente
    for (int i=0; i < qtdePinosFechadura; i++){
        int alturaPino;
        cin >> alturaPino;  
        alturasPinos.push_back(alturaPino);
    }
    
    // Calcula solução para o problema
    while (!soulucaoEncontrada){

        // Um set em todos os pinos individualmente
        for (int i = 0; i < qtdePinosFechadura; i++){
            while (alturasPinos[i] != alturaIdealPino){
                if (alturasPinos[i] > alturaIdealPino){
                    alturasPinos[i] -= 1;
                    if (i != qtdePinosFechadura - 1){
                        alturasPinos[i + 1] -= 1;
                    }
                }
                else if (alturasPinos[i] == alturaIdealPino){
                    continue;
                }
                else {
                    alturasPinos[i] += 1;
                    if (i != qtdePinosFechadura - 1){
                        alturasPinos[i + 1] += 1;
                    }
                }
                qtdeMovimentos++;
            }
        }
        

        // Verifica se pinos estão na altura ideal
        int count = 0;
        for (int i = 0; i < qtdePinosFechadura; i++){
            if (alturasPinos[i] == alturaIdealPino){
                count++;
            }
        }
        if (count == qtdePinosFechadura){
            soulucaoEncontrada = true;
        }
    }

    cout << qtdeMovimentos << endl;

    return 0;
}
