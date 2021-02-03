#include <iostream>
#define MAX_V 10
#define MIN(a,b) a<b ? a:b
#define INF 99999

using namespace std;

int V, E;
int adj[MAX_V][MAX_V];

void initAdjacency()
{
	int i, j;

	for (i = 0; i < V; i++)
		for (j = 0; j < V; j++) {
			adj[i][j] = INF;

			if (i == j)
				adj[i][j] = 0;
		}
}


void Floyd() 
{
	int k, j, i;

	for (k = 0; k < V; k++)
		for (i = 0; i < V; i++)
			for (j = 0; j < V; j++)
				adj[i][j] = MIN(adj[i][j], adj[i][k] + adj[k][j]);
}


int main(void) 
{
	int i, j;

	cout << "정점 개수 : ";
	cin >> V;
	
	cout << "간선 개수 : ";
	cin >> E;
	
	initAdjacency();

	cout << "정점 연결(정점1, 정2, 비용)" << endl;


	for (i = 0; i < E; i++) 
	{
		int v1, v2, cost;

		cin >> v1 >> v2 >> cost;

		adj[v1][v2] = adj[v2][v1] = cost;
	}


	Floyd();

	for (i = 0; i < V; i++) {
		for (j = 0; j < V; j++)
			cout << i << " ~ " << j << "까지의 최단거리 : " << adj[i][j] << endl;

		cout << endl << endl;
	}
}
