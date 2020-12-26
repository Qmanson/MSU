#include "Shop.h"
#include <iostream>

void CShop::display()
{
}

bool CShop::start(CPlayer* P1)
{
	//std::cout << "Shop\n";
	//generate();
	//display();
	//char in;
	//std::cin >> in;
}

void CShop::generate()
{
	CItem rock;
	rock.SetName("Rock");
	Inv[rock] = 30;
}

void CShop::purchase(CPlayer* user, CItem item)
{
	user->AddMoney(-Inv[item]);
	user->AddToInv(item);
}
