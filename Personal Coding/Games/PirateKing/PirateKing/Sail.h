#pragma once
#include "Ship.h"
#include "Player.h"
#include "Island.h"
#include <vector>
#include <map>


class CSail
{
public:
	CSail(CPlayer &user);
	~CSail();
	void moveShip(CPlayer user);
	void generateMap();
	void generateShips();
	void displayMap();
	void moveAllShips();


private:
	int mapH = 15;
	CPlayer* User;
	std::map<int, CIsland> islands;
	int islandVals[1000] = {};
	int islandKnown[1000] = {};
	int islandDisc[1000] = {};
	int mapWid = 30;
	int islandTypes = 4;
	std::vector<int> islandImg[6] = {
		{176, 10},
		{79, 5}, 
		{88, 2}, 
		{78, 0},
		{178, 0},
		{4, 0}
	};
	std::vector<CShip> ships;
	int startX = mapWid / 6;
	int startY = mapH / 2;
	int compWid = 30;
	int vis = 1;
};

