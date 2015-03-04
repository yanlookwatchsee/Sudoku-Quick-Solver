#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <queue>
#include <mach/mach_time.h>
using namespace std;
typedef vector<vector<char> > charmap;
void dump(charmap& b) {
	for (int i=0;i<9;++i) {
		for (int j=0;j<9;++j) {
			if (b[i][j]) cout<<b[i][j]<<" ";
			else cout<<"- ";
		}
		cout<<endl;
	}
}
class simpleProfile {
	long long int start_ns,stop_ns;
public:
	simpleProfile() {
		start_ns=0;
		stop_ns=0;
	};
	void start_profile() {
		start_ns=mach_absolute_time();
	}
	void stop_profile() {
		stop_ns=mach_absolute_time();
	}
	void show_running_time() {
		double us=(stop_ns-start_ns)/1000;
		cout<<us/1000.0<<"ms"<<endl;
	}
};

class Solution {
	struct Record {
		vector<bool> check;
		int fn; //feasible number
		char num;
		Record() {
			check=vector<bool>(9,false);
			fn=9;
			num=0;
		}
		char trivial_elect() {
			if (num!=0 || fn!=1) return 0;
			for (int i=0;i<9;++i) {
				if (!check[i]) {
					return '1'+i;
				}
			}
			return 0;
		}
		bool mark(char ch) {
			if (check[ch-'1']==false) {
				check[ch-'1']=true;
				fn--;
			}
			return fn<=0;
		}
		
	};
	struct solvebuffer {
		vector<vector<Record> > buf;
		bool exception;
		solvebuffer() {
			buf=vector<vector<Record> > (9, vector<Record>(9, Record()));
			exception=false;
		}
		void populate(const int i, const int j, char ch) {
			if (buf[i][j].check[ch-'1']) {
				exception=true;
				return;
			}
			buf[i][j].num=ch;
			//row
			for (int k=0;k<9;++k) {
				if (buf[i][k].num) continue;
				exception=buf[i][k].mark(ch);
			}
			//col
			for (int k=0;k<9;++k) {
				if (buf[k][j].num) continue;
				exception=buf[k][j].mark(ch);
			}
			//block
			for (int p=i/3*3;p<(i+3)/3*3;++p) {
				for (int q=j/3*3;q<(j+3)/3*3;++q) {
					if (buf[p][q].num) continue;
					exception=buf[p][q].mark(ch);
				}
			}
			return;
		}
		char findone(int& x, int &y) {
			for (int i=0;i<9;++i) {
				for (int j=0;j<9;++j) {
					char e=buf[i][j].trivial_elect();
					if (e) {
						x=i,y=j;
						return e;
					}
				}
			}
			for (char ch='1'; ch<='9'; ++ch) {
				//row check
				for (int i=0;i<9;++i) {
					int cnt=0;
					for (int j=0;j<9;++j) {
						if (buf[i][j].num == ch) {
							cnt =0;
							break;
						} else if (buf[i][j].num==0 && !buf[i][j].check[ch-'1']) {
							cnt++;
							x=i, y=j;
						}
					}
					if (cnt==1) {
						return ch;
					}
				}
				//column check
				for (int j=0;j<9;++j) {
					int cnt=0;
					for (int i=0;i<9;++i) {
						if (buf[i][j].num == ch) {
							cnt =0;
							break;
						} else if (buf[i][j].num==0 && !buf[i][j].check[ch-'1']) {
							cnt++;
							x=i, y=j;
						}
					}
					if (cnt==1) {
						return ch;
					}
				}

				//block check
				for (int b=0;b<9;++b) {
					int cnt =0;
					for (int i=b/3*3;i<b/3*3+3;++i) {
						bool done=false;
						for (int j=b%3*3; j<b%3*3+3;++j) {
							if (buf[i][j].num == ch) {
								cnt =0;
								done = true;
								break;
							} else if (buf[i][j].num==0 && !buf[i][j].check[ch-'1']) {
								cnt++;
								x=i, y=j;
							}
						}
						if (done) {
							break;
						}
					} 					

					if (cnt==1) {
						return ch;
					}
				}
				
			}
			return 0;
		}
		bool complete(void) {
			for (int i=0;i<9;++i) {
				for (int j=0;j<9;++j) {
					if (buf[i][j].num==0) return false;
				}
			}
			return true;
		}
		bool feasible(int i, int j, char ch) {
			return !buf[i][j].check[ch-'1'];
		}
	};
	int trysolve(solvebuffer& sb) {
		while (true) {
			int x,y;
			char a=sb.findone(x,y);
			if (a==0||sb.exception) break;
			sb.populate(x, y, a);
			if (sb.exception) break;
		} 
		if (sb.exception) return -1;
		if (sb.complete()) return 0;
		return 1;
	}

	bool solve(solvebuffer& sb, int level) {
		int ret=trysolve(sb);
		if (ret==-1) return false;
		if (ret==0) return true;
		int ti=0, tj=0;
		for (int i=0;i<9;++i) {
			for (int j=0;j<9;++j) {
				if (sb.buf[i][j].num==0) {
					ti=i;
					tj=j;	
					break;
				}
			}
		}
		for (int k=0;k<9;++k) {
			if (!sb.feasible(ti,tj,'1'+k)) continue;
			solvebuffer tsb=sb;
			tsb.populate(ti,tj,'1'+k);
			if (solve(tsb, level+1)) {
				sb=tsb;
				return true;
			}
		}
		return false;
	}
public:
	void solveSudoku(vector<vector<char> >& board) {
		solvebuffer sb;
		for (int i=0;i<9;++i) {
			for (int j=0;j<9;++j) {
				if (board[i][j]!='.') sb.populate(i,j, board[i][j]);
			}
		}
		solve(sb, 0);
		//install board
		for (int i=0;i<9;++i) {
			for(int j=0;j<9;++j) {
				board[i][j]=sb.buf[i][j].num;
			}
		}
	}

};

int main(void) {
	int T;
	cin>>T;
	for (int t=0;t<T;++t) {
		cout<<"TC#"<<t+1<<endl;
		Solution sl;
		simpleProfile per;
		vector<vector<char> > board(9,vector<char>(9,0));
		for (int i=0;i<9;++i) {
			string s;
			cin>>s;
			for (int j=0;j<9;++j) {
				board[i][j]=s[j];
			}
		}
		dump(board);
		per.start_profile();
		sl.solveSudoku(board);
		per.stop_profile();
		dump(board);
		per.show_running_time();
	}
	return 0;
}
