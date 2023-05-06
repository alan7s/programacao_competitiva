//PROBLEMA: 2854 - Árvore Genealógica
using namespace std;

const int MAX = 305;

// representação grafo em vetor de lista de adjacência
vector<int> grafo[MAX];

bool visited[MAX];

void dfs(int v) {
    visited[v] = true;
    for(int i = 0; i < grafo[v].size(); i++) {
        int u = grafo[v][i];
        if(!visited[u]) dfs(u);
    }
}

int main() {
    int m, n;
	
	// leitura primeira linha arquivo de teste
    cin >> m >> n;

    // cria um map para associar cada nome a um número
    map<string, int> id;
    int grafo_id = 0;

    for(int i = 0; i < n; i++) {
        string nome1, relacao, nome2;
		
		// leitura nome próprio seguido de uma relação e de outro nome próprio
        cin >> nome1 >> relacao >> nome2;

        // se os nomes não estiverem no map, adiciona-os e associa um número a eles
        if(id.find(nome1) == id.end()) id[nome1] = grafo_id++;
        if(id.find(nome2) == id.end()) id[nome2] = grafo_id++;

        // adiciona uma aresta no grafo, representando a relação entre as pessoas
        int u = id[nome1], v = id[nome2];
        grafo[u].push_back(v);
        grafo[v].push_back(u);
    }

	// armazena quantidade de famílias diferentes encontradas
    int cont = 0;
	
	// preenchimento do vetor visited com o valor false, indicando que nenhuma pessoa foi visitada ainda.
    memset(visited, false, sizeof visited);

    // inicia DFS a partir de cada pessoa que ainda não foi visitada
    for(int i = 0; i < grafo_id; i++) {
        if(!visited[i]) {
            cont++;
            dfs(i);
        }
    }

    cout << cont << endl;
    return 0;
}
