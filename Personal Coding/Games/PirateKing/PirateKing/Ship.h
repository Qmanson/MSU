#pragma once
#include <vector>
class CShip
{
public:
	int getX() { return locX; }
	void setY(int Y) { locY = Y; }
	int getY() { return locY; }
	void setX(int X) { locX = X; }
private:
	int locX;
	int locY;
	std::vector<int> stats = {};
};

