#pragma once
#include <string>
class CItem
{
public:
	virtual void SetName(std::string name) { ItemName = name; }
	virtual std::string GetName() { return ItemName; }
	virtual void SetDescription(std::string description) { ItemDescription = description; }
	virtual std::string GetDescription() { return ItemDescription; }

private:
	std::string ItemName = "";
	std::string ItemDescription = "";
};

