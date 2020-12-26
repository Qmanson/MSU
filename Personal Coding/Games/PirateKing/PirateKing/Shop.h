#pragma once
#include "Event.h"
#include <map>
class CPlayer;

class CShop : public CEvent
{
public:
	virtual void display();
	virtual bool start(CPlayer* P1);
	virtual void generate();
	virtual void purchase(CPlayer* user, CItem item);
	virtual std::map<CItem, int> GetInv() { return Inv;}
	virtual void SetInv(std::map<CItem, int> inv) { Inv = inv; }
private:
	CCharacter Keeper;
	std::map<CItem, int> Inv;

};

