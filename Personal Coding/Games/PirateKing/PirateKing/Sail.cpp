#include "Sail.h"
#include "Player.h"
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <windows.h> 

CSail::CSail(CPlayer &user)
{
	User = &user;
	CShip ship = (user).GetShip();
	ship.setX(startX);
	ship.setY(startY);
	(user).SetShip(ship);
	generateMap();
	generateShips();
}

CSail::~CSail()
{
}

void CSail::moveShip(CPlayer user)
{
	User = &user;

	displayMap();
	char dir;
	std::cin >> dir;
	std::cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
	CShip ship = (user).GetShip();
	switch (dir)
	{
	case('2'):
		if (islandVals[(((user).GetShip().getY()) * mapWid) + ((user).GetShip().getX())] != 176)
		{
			islands[(((user).GetShip().getY()) * mapWid) + ((user).GetShip().getX())].land(user);
		}
		break;
	case('n'):
		if ((user).GetShip().getY() >0)
		{
			ship.setY(ship.getY()-1);
			(user).SetShip(ship);
		}
		moveAllShips();
		moveShip(user);
		break;
	case('s'):
		if ((user).GetShip().getY() < (mapH-1))
		{
			ship.setY(ship.getY() + 1);
			(user).SetShip(ship);
		}
		moveAllShips();
		moveShip(user);
		break;
	case('e'):
		if ((user).GetShip().getX() < (mapWid - 1))
		{
			ship.setX(ship.getX() + 1);
			(user).SetShip(ship);
		}
		moveAllShips();
		moveShip(user);
		break;
	case('w'):
		if ((user).GetShip().getX() > 0)
		{
			ship.setX(ship.getX() - 1); 
			(user).SetShip(ship);
		}
		moveAllShips();
		moveShip(user);
		break;
	default:
		break;
	}
}

void CSail::generateMap()
{
	std::srand(std::time(NULL));
	for (int i = 0; i < (mapH*mapWid); i++)
	{
		int rand = std::rand() % 100;
		for (int j = 0; j < islandTypes; j++)
		{
			if (rand >= islandImg[j][1])
			{
				islandVals[i] = islandImg[j][0];
				break;
			}
		}
		islandKnown[i] = islandImg[4][0];
		if (islandVals[i] != 176)
		{
			CIsland made;
			made.generateIsland("Home");
			islands[i] = made;
		}
	}
	islandVals[(startY * mapWid) + startX] = islandImg[1][0];
}

void CSail::generateShips()
{
	int i = 0;
	for (auto& island : islandVals)
	{
		CShip ship;
		ship.setX(i % mapWid);
		ship.setY((i - ship.getX()) / mapWid);
		switch (island)
		{
		case(88):
			ships.push_back(ship);
			break;
		default:
			break;
		}
		i++;
	}
}

void CSail::displayMap()
{
	for (int i = 0; i < (vis*2)+1; i++)
	{
		if (((*User).GetShip().getX() - (vis - i))/mapWid == (*User).GetShip().getX()/mapWid)
		{
			for (int j = 0; j < (vis * 2) + 1; j++)
			{
				islandKnown[(((*User).GetShip().getY() - (vis - j)) * mapWid) + ((*User).GetShip().getX() - (vis - i))] = islandVals[(((*User).GetShip().getY() - (vis - j)) * mapWid) + ((*User).GetShip().getX() - (vis - i))];
				islandDisc[(((*User).GetShip().getY() - (vis - j)) * mapWid) + ((*User).GetShip().getX() - (vis - i))] = 1;
			}
		}
	}
	for (std::vector<CShip>::iterator it = ships.begin(); it != ships.end(); ++it)
	{
		if (islandVals[((*it).getY() * mapWid) + (*it).getX()] == 176)
		{
			islandKnown[((*it).getY() * mapWid) + (*it).getX()] = 5;
		}
	}
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	int k = 1;
	SetConsoleTextAttribute(hConsole, k);
	int count = 0;
	std::vector<std::string> compDisp = {
		"_____________",
		"  Choose A   ",
		" Direction:  ",
		"     [N]     ",
		"      \xBA      ",
		"     \xC9\xBA\xBB     ",
		"[W]\xCD\xCD\xCD\xCE\xCD\xCD\xCD[E]",
		"     \xC8\xBA\xBC     ",
		"      \xBA      ",
		"     [S]     ",
		"_____________",
		"[1] Manage   ",
		"[2] Dock     ",
		"[3] Rest     ",
		"[4] Repair   ",
		"[5] Fish     ",
		"             ",
		"             ",
		"             ",
		"             ",
		"             ",
		"             ",
		"             ",
		"             ",
		"             ",
		"             ",
		"             ",
		"            |",
		"             "
	};
	std::string compassSpace = "";
	int compCounter = 0;
	compassSpace.append((compWid-(compDisp[0]).length())/2, ' ');
	for (int i = 0; i < (mapH*mapWid); i++)
	{
		if (count == 0)
		{
			if (i == 0)
			{
				std::cout << "\n|";
			}
			else
			{
				std::string water = "";
				water.append((mapWid*4)+2, (char)176);
				k = 1;
				SetConsoleTextAttribute(hConsole, k);
				std::cout << "|" << water << "|";
				k = 15;
				SetConsoleTextAttribute(hConsole, k);
				std::cout << compassSpace << compDisp[compCounter] << compassSpace << "|" << "\n|";
				if (compCounter < compDisp.size()-1)
				{
					compCounter += 1;
				}
			}
		}
		if ((((*User).GetShip().getY()*mapWid)+(*User).GetShip().getX()) == i)
		{
			k = 1;
			SetConsoleTextAttribute(hConsole, k);
			std::cout << (char)176;
			k = 4;
			SetConsoleTextAttribute(hConsole, k);
			std::cout << "[";
			k = 1;
			SetConsoleTextAttribute(hConsole, k);
			if (islandKnown[i] == 5)
			{
				k = 5;
				SetConsoleTextAttribute(hConsole, k);
			}
			else if (islandKnown[i] != 176 && islandKnown[i] != 178)
			{
				k = 2;
				SetConsoleTextAttribute(hConsole, k);
			}
			std::cout << (char)islandKnown[i];
			k = 4;
			SetConsoleTextAttribute(hConsole, k);
			std::cout << "]";
		}
		else 
		{
			k = 1;
			SetConsoleTextAttribute(hConsole, k);
			std::cout << (char)176 << (char)176;
			if (islandKnown[i] == 5)
			{
				k = 5;
				SetConsoleTextAttribute(hConsole, k);
			}
			else if(islandKnown[i] != 176 && islandKnown[i] != 178)
			{
				k = 2;
				SetConsoleTextAttribute(hConsole, k);
			}
			std::cout << (char)islandKnown[i];
			k = 1;
			SetConsoleTextAttribute(hConsole, k);
			std::cout << (char)176;
		}

		count++;
		if (count >= mapWid)
		{
			k = 1;
			SetConsoleTextAttribute(hConsole, k);
			std::cout << (char)176 << (char)176 << "|";
			k = 15;
			SetConsoleTextAttribute(hConsole, k);
			std::cout << compassSpace << compDisp[compCounter] << compassSpace << "|" << "\n";
			if (compCounter < compDisp.size() - 1)
			{
				compCounter += 1;
			}
			count = 0;
		}
	}
	for (std::vector<CShip>::iterator it = ships.begin(); it != ships.end(); ++it)
	{
		if (islandVals[((*it).getY() * mapWid) + (*it).getX()] == 176)
		{
			if (islandDisc[((*it).getY() * mapWid) + (*it).getX()] == 1)
			{
				islandKnown[((*it).getY() * mapWid) + (*it).getX()] = 176;
			}
			else
			{
				islandKnown[((*it).getY() * mapWid) + (*it).getX()] = 178;
			}
			
		}
	}
}

void CSail::moveAllShips()
{
	std::srand(std::time(NULL));
	for (std::vector<CShip>::iterator it = ships.begin(); it != ships.end(); ++it)
	{
		int x = 0;
		int y = 0;
		int rand = std::rand() % 4;
		switch (rand)
		{
		case(0):
			y += 1;
			break;
		case(1):
			x += 1;
			break;
		case(2):
			y -= 1;
			break;
		case(3):
			x -= 1;
			break;
		default:
			break;
		}
		if (((*it).getX() + x) < mapWid && ((*it).getX() + x) > 0)
		{
			(*it).setX((*it).getX() + x);
		}
		if (((*it).getY() + y) < mapH && ((*it).getY() + y) > 0)
		{
			(*it).setY((*it).getY() + y);
		}
	}
}
