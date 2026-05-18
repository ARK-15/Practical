// Implement depth first search algorithm and Breadth First Search algorithm, use an undirected
// graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
// structure.

#include <bits/stdc++.h>
using namespace std;

class Graph
{
    map<int, vector<int>> g;

public:
    Graph()
    {
        int node_count = 0;
        cout << "Enter number of nodes in graph(numbers from 0 onwards):";
        cin >> node_count;
        for (int i = 0; i < node_count; i++)
        {
            int node_name = 0;
            cout << "Enter name of node:";
            cin >> node_name;
            int neighbor_count = 0;
            cout << "Enter Number of neighbours:";
            cin >> neighbor_count;
            vector<int> neighbors;
            for (int j = 0; j < neighbor_count; j++)
            {
                int neighbor = 0;
                cout << "Enter neighbour node name :";
                cin >> neighbor;
                neighbors.push_back(neighbor);
            }
            g[i] = neighbors;
        }
    }
    void showGraph()
    {
        for (int i = 0; i < g.size(); i++)
        {
            cout << i << "\t";
            for (int j = 0; j < g[i].size(); j++)
            {
                cout << g[i][j] << " ";
            }
            cout << "\n";
        };
    }
    void bfsDriver(int starter)
    {
        queue<int> q;
        vector<int> v;
        q.push(starter);
        v.push_back(starter);
        cout << "BFS TRAVERSAL: ";
        bfs(q, v);
    }
    void bfs(queue<int> q, vector<int> visited)
    {
        if (q.empty())
        {
            return;
        }
        int first = q.front();
        q.pop();
        cout << first << " ";
        for (int i : g[first])
        {
            if (find(visited.begin(), visited.end(), i) == visited.end())
            {
                visited.push_back(i);
                q.push(i);
            }
        }
        bfs(q, visited);
    }
    void dfsDriver(int starter)
    {
        stack<int> s;
        vector<int> v;
        s.push(starter);
        v.push_back(starter);
        cout << "DFS TRAVERSAL: ";
        dfs(s, v);
    }
    void dfs(stack<int> s, vector<int> visited)
    {
        if (s.empty())
        {
            return;
        }
        int first = s.top();
        s.pop();
        cout << first << " ";
        for (int i : g[first])
        {
            if (find(visited.begin(), visited.end(), i) == visited.end())
            {
                visited.push_back(i);
                s.push(i);
            }
        }
        dfs(s, visited);
    }
};

int main()
{
    // cout << "HI";
    Graph g;
    g.showGraph();
    g.bfsDriver(0);
    g.dfsDriver(0);
    return 0;
}