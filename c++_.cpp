#include<iostream>
#include<algorithm>
#include<vector>
#include<map>

#define fori(i,j) for(int i = 1 ;; ++i ) \
				{\
				if(i == 5)\
				{\
					ret[j] = 0;\
					break;\
				}\
					++ret[j];

class solution
{
public:
	solution() :ret(11, 0)
	{
	}

	void operator()()
	{
		fori(i1, 1)
			fori(i2, 2)
			fori(i3, 3)
			fori(i4, 4)
			fori(i5, 5)
			fori(i6, 6)
			fori(i7, 7)
			fori(i8, 8)
			fori(i9, 9)
			fori(i10, 10)

			if (f())
			{
				for (int i = 1; i != 11; ++i)
				{
					switch (ret[i])
					{
					case 1:std::cout << "A "; break;
					case 2:std::cout << "B "; break;
					case 3:std::cout << "C "; break;
					case 4:std::cout << "D "; break;
					}
				}
				std::cout << std::endl;
			}
	}}}}}}}}}}}

	bool f()
	{
		return (f1() && f2() && f3() && f4() && f5() && f6() && f8() && f9() && f7() && f10());
	}

	bool f1()
	{
		return (true);
	}

	bool f2()
	{
		switch (ret[2])
		{
		case 1:return (ret[5] == 3);
		case 2:return (ret[5] == 4);
		case 3:return (ret[5] == 1);
		case 4:return (ret[5] == 2);
		}
		return (false);
	}

	bool f3()
	{
		switch (ret[3])
		{
		case 1:return (ret[3] != ret[2] && ret[6] == ret[2] && ret[6] == ret[4]);
		case 2:return (ret[6] != ret[1] && ret[1] == ret[2] && ret[1] == ret[4]);
		case 3:return (ret[2] != ret[3] && ret[3] == ret[6] && ret[1] == ret[4]);
		case 4:return (ret[4] != ret[3] && ret[3] == ret[6] && ret[3] == ret[2]);
		}
		return (false);
	}

	bool f4()
	{
		switch (ret[4])
		{
		case 1:return (ret[1] == ret[5]);
		case 2:return (ret[2] == ret[7]);
		case 3:return (ret[1] == ret[9]);
		case 4:return (ret[6] == ret[10]);
		}
		return (false);
	}

	bool f5()
	{
		switch (ret[5])
		{
		case 1:return (ret[5] == ret[8]);
		case 2:return (ret[5] == ret[4]);
		case 3:return (ret[5] == ret[9]);
		case 4:return (ret[5] == ret[7]);
		}
		return (false);
	}

	bool f6()
	{
		switch (ret[6])
		{
		case 1:return (ret[8] == ret[2] && ret[8] == ret[4]);
		case 2:return (ret[8] == ret[1] && ret[8] == ret[6]);
		case 3:return (ret[8] == ret[3] && ret[8] == ret[10]);
		case 4:return (ret[8] == ret[5] && ret[8] == ret[9]);
		}
		return (false);
	}

	bool f7()
	{
		std::vector<int>counter(5, 0);
		for (int i = 1; i != 11; ++i)
			++counter[ret[i]];
		std::map<int, int>mp{ {counter[1],1},{counter[2],2},
		{ counter[3],3 },{ counter[4],4 } };
		int index = (*mp.begin()).second;
		switch (ret[7])
		{
		case 1:return (index == 3);
		case 2:return (index == 2);
		case 3:return (index == 1);
		case 4:return (index == 4);
		}
		return (false);
	}

	bool f8()
	{
		int temp;
		switch (ret[8])
		{
		case 1:return !((temp = ret[1] - ret[7]) == -1 || temp == 1);
		case 2:return !((temp = ret[1] - ret[5]) == -1 || temp == 1);
		case 3:return !((temp = ret[1] - ret[2]) == -1 || temp == 1);
		case 4:return !((temp = ret[1] - ret[10]) == -1 || temp == 1);
		}
		return (false);
	}

	bool f9()
	{
		bool tmp = (ret[1] == ret[6]);
		switch (ret[9])
		{
		case 1:return (tmp != (ret[6] == ret[5]));
		case 2:return (tmp != (ret[10] == ret[5]));
		case 3:return (tmp != (ret[2] == ret[5]));
		case 4:return (tmp != (ret[9] == ret[5]));
		}
		return (false);
	}

	bool f10()
	{
		std::vector<int>counter(4, 0);
		for (int i = 1; i != 11; ++i)
			++counter[ret[i] - 1];
		std::sort(counter.begin(), counter.end());
		int max = counter[3];
		int min = counter[0];
		switch (ret[10])
		{
		case 1:return (max - min == 3);
		case 2:return (max - min == 2);
		case 3:return (max - min == 4);
		case 4:return (max - min == 1);
		}
		return (false);
	}

private:
	std::vector<int>ret;
};

int main()
{
	solution solution;
	solution();
}
