/*
'''
Вася подсчитал, что у него есть m гаджетов, которые нужно подключить к USB и всего n USB-портов на компьютере. 
В ближайшем интернет-магазине продаются разветвители с одного USB на два за c2 рублей и USB-хабы с одного USB 
на 5 по c5 рублей. Разветвители и хабы можно подключать друг к другу и к USB-портам компьютера. Определите, 
какое минимальное количество рублей нужно потратить Васе, чтобы подключить все USB устройства. При этом 
можно обеспечить возможность подключить и больше m гаджетов, главное минимизировать цену.

Ограничение времени - 2 секунды
Ограничение памяти - 256mb

Формат ввода (по порядку):
n - количество портов
m - количество гаджетов
c2 - цена разветвителя
c2 - цена хаба

Формат вывода:
целое число - минимальная цена

Примеры:
1,3,1,10 -> 2
2,4,9,10 -> 10
3,8,9,10 -> 19

'''
*/
#include<iostream>
#include<vector>

using namespace std;

int gadget;
int price2;
int price5;
vector<int> res;

struct Node {
	int money = 0;
	int port = 0;
	Node* left = NULL;
	Node* right = NULL;
};

void Split(Node* root, int money)
{
	Node* node = new Node;
	root->left = node;
	node->money = root->money + money;
	node->port = root->port - 1 + 2;
	node->left = NULL;
	node->right = NULL;
}

void Hub(Node* root, int money)
{
	Node* node = new Node;
	root->right = node;
	node->money = root->money + money;
	node->port = root->port - 1 + 5;
	node->left = NULL;
	node->right = NULL;
}

void checkThisSwag(Node* root, int gadget) {
	//cout << root->money << " " << root->port << endl;
	if ( (root->port) >= gadget )
		res.push_back(root->money);
	else {
		Split(root, price2);
		Hub(root, price5);

		checkThisSwag(root->left, gadget);
		checkThisSwag(root->right, gadget);
		checkThisSwag(root->left, gadget);
		checkThisSwag(root->right, gadget);
	}

}

int main() {
	Node* start = new Node;

	cin >> start->port;
	cin >> gadget;
	cin >> price2;
	cin >> price5;

	checkThisSwag(start, gadget);

	int Size = res.size();
	int min = res[0];
	
	
	for (int i = 0; i < Size - 1; i++) {
		//cout << res[i] << " ";
		if (res[i] < min) min = res[i];
	}

	cout << min;
}



//print(solution(1,3,1,10)) # -> 2
//print(solution(2,4,9,10)) # -> 10
//print(solution(3,8,9,10)) # -> 19