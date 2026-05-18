// #include<iostream>
// #include<vector>

// using namespace std;

// vector<int> graph[10];
// bool visited[10];

// void DFS(int node){

//     visited[node] = true;
//     cout<<node<<" ";

//     for(int nb:graph[node]){
//         if(!visited[nb])
//         {
//             DFS(nb);
//         }
//     }
// }

// int main(){
//     int v,e;
//     cout<<"enter number of vertices and edges";
//     cin>>v>>e;
    
//     cout<<"enter edges\n";
//     for(int i=0;i<e;i++){
//         int u,v;
//         cin>>u>>v;
//         graph[u].push_back(v);
//         graph[v].push_back(u);

//     }
//     int start;

//     cout<<"enter starting index";
//     cin>>start;
//     cout<<"dfs traversal";
//     DFS(start);
//     return 0;
// }

#include<iostream>
#include<queue>

using namespace std;

int graph[10][10];
int visited[10];

int n;

void BFS(int start){
    queue<int> q;
    visited[start] = 1;
    q.push(start);

    while(!q.empty()){
        int node = q.front();
        q.pop();
        cout<<node<<" ";
        for(int i=0;i<n;i++){
            if(graph[node][i]==1&&visited[i]==0){
            visited[i]=1;
            q.push(i);
        }}

    }


}
int main(){
    int u,v,ver,ed,start;

    cout<<"enter number of vertices: ";
    cin>>ver;
    n = ver;

    cout<<"enter number of edges: ";
    cin>>ed;

    cout<<"enter edges: \n";
    for(int i=0;i<ed;i++){
       cin>>u>>v;

       graph[u][v]=1;
       graph[v][u]=1;
       
    }
    cout<<"enter starting vertex: ";
       cin>>start;

       cout<<"bfs traversal: ";

       BFS(start);
       return 0;
    


}
