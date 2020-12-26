#pragma once
#include "Character.h"
#include "Ship.h"
#include "Relic.h"
#include <string>
#include <vector>
#include <map>

class CSail;

class CPlayer : public CCharacter
{
public:
	CPlayer();
	~CPlayer();
	std::vector<CAction> GetDeck() { return Deck; }
	std::vector<CAction> GetHand() { return Hand; }
	std::vector<CAction> GetDiscard() { return Discard; }
	std::vector<CAction> GetDraw() { return Draw; }
	int GetCardsOnDraw() { return cardsOnDraw; }
	CShip GetShip() { return Ship; }
	void SetShip(CShip ship) { Ship = ship; }
	virtual void SetSail(CSail* sail) { Sail = sail; }
	virtual CSail* GetSail() { return Sail; }
	void SetInv(std::vector<CItem> inv) { Inventory = inv; }
	std::vector<CItem> GetInv() { return Inventory; }
	void AddToInv(CItem item) { Inventory.push_back(item); }
	void SetWeapons(std::map<std::string, std::vector<CAction>> weapons) { Weapons = weapons; }
	std::map<std::string, std::vector<CAction>> GetWeapons() { return Weapons; }
	void SetMoney(long money) { Money = money; }
	long GetMoney() { return Money; }
	void AddMoney(long adding) { Money += adding; }
	void SetDeck(std::vector<CAction> newDeck) { Deck = newDeck; }
	void SetHand(std::vector<CAction> newHand) { Hand = newHand; }
	void SetDiscard(std::vector<CAction> newDiscard) { Discard = newDiscard; }
	void SetDraw(std::vector<CAction> newDraw) { Draw = newDraw; }
	void SetCardsOnDraw(int cards) { cardsOnDraw = cards; }
	void DiscardHand();
	void DisplayHand();
	void RemoveCardHand(int remove);
private:
	std::vector<CAction> Deck;
	std::vector<CAction> Hand;
	std::vector<CAction> Discard;
	std::vector<CAction> Draw;
	std::map<std::string, std::vector<CAction>> Weapons;
	std::vector<CRelic> Relics;
	std::vector<CItem> Inventory;
	long Money;
	CShip Ship;
	int cardsOnDraw;
	CSail* Sail;


};

