#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cmath>
#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<unordered_set>
using namespace std;

#define OUT 0
#define endl '\n'
#define MAMBA return
typedef long long ll;
const int N = 3e5 + 10;
const int INF = 0x3f3f3f3f;
typedef unsigned long long ull;
int _pow(int a,int b){int x=1,y=a;while(b>0){if(b&1)x*=y;y*=y;b>>=1;}return x;}
void print(ll x){if(x<0){putchar('-');x=-x;}if(x>9){print(x/10);}putchar(char(x%10+'0'));}
void print(int x){if(x<0){putchar('-');x=-x;}if(x>9){print(x/10);}putchar(char(x%10+'0'));}
void print(string s){int n=s.length();for(int i=0;i<n;i++)putchar(s[i]);}
inline int read_int(){int f=1,x=0;char ch=getchar();while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}while(isdigit(ch)){x=(x<<1)+(x<<3)+(ch^48);ch=getchar();}return x*f;}
inline ll read_ll(){int f=1;ll x=0;char ch=getchar();while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}while(isdigit(ch)){x=(x<<1)+(x<<3)+(ch^48);ch=getchar();}return x*f;}
// ----------------------------

// ----------------------------
ll len[N];
ll head_idx[N];
// ----------------------------


int man() {
	int q = read_int();
	// ------------------------
	int op,k;
	ll sum = 0;
	int pop_cnt = 0;
	int snake_cnt = 0;
	while (q--) {
		op = read_int();
		if (op == 1) {
			len[++snake_cnt] = read_int();
			head_idx[snake_cnt] = head_idx[snake_cnt-1] + len[snake_cnt-1];
		}
		else if (op == 2) sum += len[++pop_cnt];
		else {
			k = read_int();
			print(head_idx[k+pop_cnt]-sum);
			putchar('\n');
		}
	}
	MAMBA OUT;
}
 		   	  				   			  						   														   															  	 																																			int main() {MAMBA man();}