#include "Fight.h"
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <ctype.h>
#include <string>
#include <numeric>

#include <vector>

/* startBattle Function
 * Param: user : User in battle
 * Param: enemies : Enemies in battle
 * Return : True if won, False if lost
 */
bool CFight::startBattle(CPlayer user, std::vector<CEnemy> enemies)
{
	//Initialize User in Fight Class
	User = user;

	//Set Action stats to base stats with current energy equal to max energy
	int* tempActionStatsEnergy = User.GetBaseStats();
	tempActionStatsEnergy[9] = User.GetBaseStats()[8];
	User.SetActionStats(tempActionStatsEnergy);

	/*
	 * Add Treasures activation here
	 * Stage = 0, Using user
	 * Run func: ActivateTreasures(int Stage = 0, CCharacter user = User)
	 */

	 //Initialize Enemies vector in Fight Class
	Enemies = enemies;
	int enemyCounter = 0;
	for (CEnemy enemy : enemies)
	{
		enemy.SetActionStats(enemy.GetBaseStats());
		Enemies.at(enemyCounter) = enemy;
		enemyCounter += 1;
		/*
		 * Add Treasures activation here
		 * Stage = 0, Using enemy
		 * Run func: ActivateTreasures(int Stage = 0, CCharacter user = enemy)
		 */
	}

	//Move to player action stage 
	return playerStartAction();
}

bool CFight::playerStartAction()
{

	//Continue with battle as long as Player has more then 0 health
	if (User.GetActionStats()[7] > 0)
	{
		//Discard all cards in hand
		User.DiscardHand();

		//Display All Cards
		User.DisplayHand();
		return playerAction();
	}
	else
	{
		//Player lost as they have less then 0 health return false for losing
		return false;
	}
}

void CFight::Display(int card)
{
	//Display UserName
	std::cout << "\n" << User.GetName() << ":" << std::setw(28 - User.GetName().size()) << std::right << "VS ";

	/*
	 * Add Crew display
	 */

	 //Display Enemies Names
	for (int i = 0; i < Enemies.size(); i++)
	{
		std::cout << Enemies.at(i).GetName() << ":";
	}

	//Display Player Health Bars 
	std::string HealthBar = "";
	if ((((double)User.GetActionStats()[7] / (double)User.GetActionStats()[2])) > 0.0)
	{
		HealthBar.insert(0, (int)(((double)User.GetActionStats()[7] / (double)User.GetActionStats()[2]) * 26), '\xDB');
	}
	std::cout << "\n" << std::setw(26) << HealthBar;

	//Display Enemies Health Bar
	for (int i = 0; i < Enemies.size(); i++)
	{
		HealthBar = "";
		if ((((double)Enemies.at(i).GetActionStats()[7] / (double)Enemies.at(i).GetActionStats()[2])) > 0.0)
		{
			HealthBar.insert(0, (int)(((double)Enemies.at(i).GetActionStats()[7] / (double)Enemies.at(i).GetActionStats()[2]) * 29), '\xDB');
		}
		std::cout << std::setw(31) << HealthBar;
	}
	std::cout << "\n";

	//Display Player and Enemy Stats
	for (int i = 0; i < 11; i++)
	{
		//Do not Display Max Health or Max Energy
		if (i != 8 && i != 2)
		{
			if (i == 7)
			{
				//Display Ratios of Health
				//Player Stats
				std::cout << std::setw(15) << User.IntToName[i] << "-" << std::setw(6) << std::right << User.GetActionStats()[i] << "/" << std::setw(3) << User.GetActionStats()[2] << " |";
				//Enemy Stats
				for (int j = 0; j < Enemies.size(); j++)
				{
					std::cout << std::setw(18) << Enemies.at(j).IntToName[i] << "-" << std::setw(6) << std::right << Enemies.at(j).GetActionStats()[i] << "/" << std::setw(3) << Enemies.at(j).GetActionStats()[2] << "\n";
				}

			}
			else if (i == 9)
			{
				//Display Ratios of Energy
				//Player Stats
				std::cout << std::setw(15) << User.IntToName[i] << "-" << std::setw(6) << std::right << User.GetActionStats()[i] << "/" << std::setw(3) << User.GetActionStats()[8] << " |";
				//Enemy Stats
				for (int j = 0; j < Enemies.size(); j++)
				{
					std::cout << std::setw(18) << Enemies.at(j).IntToName[i] << "-" << std::setw(6) << std::right << Enemies.at(j).GetActionStats()[i] << "/" << std::setw(3) << Enemies.at(j).GetActionStats()[8] << "\n";
				}
			}
			else
			{
				//Display Other Stats
				//Player Stats
				std::cout << std::setw(15) << User.IntToName[i] << "-" << std::setw(10) << std::right << User.GetActionStats()[i] << " |";
				//Enemy Stats
				for (int j = 0; j < Enemies.size(); j++)
				{
					std::cout << std::setw(18) << Enemies.at(j).IntToName[i] << "-" << std::setw(10) << std::right << Enemies.at(j).GetActionStats()[i] << "\n";
				}
			}
		}
	}

	//Display Cards
	std::cout << "\nCards in Hand:\n \n";
	int HandChoice = 1;
	//Card Names when not in card select mode
	if (card == -1)
	{
		for (CAction a : User.GetHand())
		{
			std::cout << "[" << HandChoice << "]" << std::setw(20) << std::left << a.GetName();
			HandChoice += 1;
		}
		std::cout << "\n";
		std::cout << "\nChoose action number (1-9) or end turn with any other key\n";
	}
	else
	{
		//Card display
		CAction a = (User.GetHand()[card - 1]);
		std::cout << std::setw(20) << std::right << "[" << card << "]" <<  a.GetName() << ": " << a.GetCost()  << " ENG" << "\n" << "\n";
		std::cout << std::setw(35) << std::right << "Player Effects: ";
		std::cout << "\n";
		int counter = 0;
		std::cout << std::setw(21) << std::right << "| ";
		for (int i = 0; i < 11; i++)
		{
			if (a.GetEffectPlayer()[i] != 0)
			{
				std::cout  << User.IntToName[i] << "(" << a.GetEffectPlayer()[i] << ") ";
				counter++;
			}
		}
		if (counter == 0)
		{
			std::cout << "NONE";
		}
		std::cout << "\n" << "\n";
		std::cout << std::setw(34) << std::right << "Enemy Effects: ";
		std::cout << "\n";
		counter = 0;
		std::cout << std::setw(21) << std::right << "| ";
		for (int i = 0; i < 11; i++)
		{
			if (a.GetEffectEnemy()[i] != 0)
			{
				std::cout << User.IntToName[i] << "(" << a.GetEffectEnemy()[i] << ") ";
				counter++;
			}
		}
		if (counter == 0)
		{
			std::cout << "NONE";
		}
		std::cout << "\n";
		std::cout << "\nThis is the move you selected would you like to use it? (y/n) \n";
	}
}

/* playerAction Function
 * Return : True if won, False if lost
 */
bool CFight::playerAction()
{
	//Display Fight screen 
	Display(-1);

	//Choice of card 
	int choice;
	std::cin >> choice;

	//Determine if input is valid
	if (!std::cin)
	{
		std::cin.clear();
		std::cin.ignore();
	}
	//Max of 9 cards in hand so if greater then 9 print invalid message
	if (choice > 9)
	{
		std::cout << "\n \n \n \n \n \n";
		std::cout << "\n***********INVALID CARD CHOICE*************\n";
		return playerAction();
	}
	else if (choice > 0 && (User.GetHand().size() + 1) > choice)
	{
		//When valid choice...
		if ((User.GetHand()[choice - 1]).GetCost() <= User.GetActionStats()[9])
		{
			if (CardSelect(choice))
			{
				//Action decided
				CAction action = (User.GetHand()[choice - 1]);

				//Update Users Stats from using action
				User.UpdateOffenseStats(action);

				//Update each enemies stats from action
				for (int i = 0; i < Enemies.size(); i++)
				{
					Enemies.at(i).UpdateDefenceStats(action, User.GetActionStats());
				}
				User.RemoveCardHand((choice - 1));
			}
		}
		else
		{
			//Case where energy is greater then current energy
			std::cout << "\n \n \n \n \n \n";
			std::cout << "\n*********You do not Have enough energy for that card**********\n";
		}
		return playerAction();
	}
	else if (choice == 0)
	{
		//Ending players turn
		return playerActionEnd();
	}
	else
	{
		//Card chosen that isnt available
		std::cout << "\n \n \n \n \n \n";
		std::cout << "\n**********Card Not Available************\n";
		return playerAction();
	}

	return playerActionEnd();
}

bool CFight::CardSelect(int card)
{
	Display(card);
	char response;
	std::cin >> response;
	switch (response)
	{
	case('y'):
		return true;
		break;
	case('n'):
		return false;
		break;
	default:
		std::cout << "Please Choose 'y' or 'n'\n";
		return CardSelect(card);
		break;
	}
	return false;
}

bool CFight::playerActionEnd()
{
	//Remove Block from Enemies
	for (int i = 0; i < Enemies.size(); i++)
	{
		int* temp = Enemies.at(i).GetActionStats();
		temp[3] = 0;
		Enemies.at(i).SetActionStats(temp);
	}

	return enemyAction();
}

bool CFight::enemyAction()
{
	//Remove enemies that died
	std::vector<CEnemy> tempEnemy = Enemies;
	for (int i = 0; i < tempEnemy.size(); i++)
	{
		if (tempEnemy.at(i).GetActionStats()[7] <= 0)
		{
			Enemies.erase(Enemies.begin() + i);
			enemyCounter--;
		}
	}
	//If no enemies remain
	if (enemyCounter <= 0)
	{
		return true;
	}
	else
	{
		//Do action for each enemy
		for (int i = 0; i < Enemies.size(); i++)
		{
			//for each enemy with health do action
			std::cout << "\n \n \n \n \n \n";
			if (Enemies.at(i).GetActionStats()[7] > 0)
			{
				//Choose random attack
				int randAttack = rand() % Enemies.at(i).GetNumActions();
				CAction choice = Enemies.at(i).GetEnemyActions()[randAttack];
				std::cout << "\n" << Enemies.at(i).GetName() << " used: " << choice.GetName() << "\n";

				//Update Enemy stats
				Enemies.at(i).UpdateOffenseStats(choice);

				//Update User stats
				User.UpdateDefenceStats(choice, Enemies.at(i).GetActionStats());
			}
		}
	}
	//Set Energy to max energy
	User.SetOneActionStat(User.GetActionStats()[8], 9);

	for (int i = 0; i < Enemies.size(); i++)
	{
		Enemies.at(i).SetOneActionStat(Enemies.at(i).GetActionStats()[8], 9);
	}

	return enemyActionEnd();
}

bool CFight::enemyActionEnd()
{
	//Set Block to zero 
	User.SetOneActionStat(0, 3);

	return playerStartAction();
}

void CFight::AddEnemies(int enemyNum)
{
	std::ifstream InStream;
	InStream.open("Characters.txt", std::ifstream::in);
	int i = 0;
	int id;
	std::string name;
	int stats[11];
	int actionID;
	CAction action;
	if (InStream.good())
	{
		std::string line;
		while (getline(InStream, line) && i < enemyNum)
		{
			std::istringstream in(line);
			CEnemy enemy;
			in >> id >> name;
			for (int j = 0; j < 11; j++)
			{
				in >> stats[j];
			}
			while (in.good())
			{
				in >> actionID;
				action = GetFileAction(actionID);
				enemy.AddAction(action);
			}
			enemy.SetName(name);
			enemy.SetID(id);
			enemy.SetBaseStats(stats);
			Enemies.push_back(enemy);
			enemyCounter++;
			i++;
		}
	}
	InStream.close();
}

CAction CFight::GetFileAction(int actionID)
{
	CAction action;
	std::ifstream InStream;
	InStream.open("Actions.txt", std::ifstream::in);

	int i = 0;
	bool found = false;
	char character;
	int stat;
	char operation;
	char rounds;
	int quantity;
	int cost;

	int statsEffectEnemy[11] = {};
	//int EnemyEffectDuration[11] = {};
	int statsEffectPlayer[11] = {};
	//int PlayerEffectDuration[11] = {};
	std::string name = "";

	if (InStream.good())
	{
		std::string line;
		while (getline(InStream, line) && !found)
		{
			std::istringstream in(line);
			int id;
			in >> id;
			if (id == actionID)
			{
				found = true;
				in >> name >> cost;
				while (in.good())
				{
					in >> character >> stat >> operation >> rounds >> quantity;
					switch (character)
					{
					case 'P':
						switch (operation)
						{
							//case 'M':
						case 'S':
							if (!isdigit(rounds))
							{
								statsEffectPlayer[stat] -= quantity;
							}
							break;
						case 'A':
							if (!isdigit(rounds))
							{
								statsEffectPlayer[stat] += quantity;
							}
							break;
							//case 'D':
						default:
							std::cout << "INVALID OPERATION";
							break;
						}
						break;
					case 'O':
						switch (operation)
						{
							//case 'M':
						case 'S':
							if (!isdigit(rounds))
							{
								statsEffectEnemy[stat] -= quantity;
							}
							break;
						case 'A':
							if (!isdigit(rounds))
							{
								statsEffectEnemy[stat] += quantity;
							}
							break;
							//case 'D':
						default:
							std::cout << "INVALID OPERATION";
							break;
						}
						break;
					default:
						std::cout << "INVALID CHARACTER";
						break;

					}
				}
			}
		}
	}
	action.SetCost(cost);
	action.SetEffectEnemy(statsEffectEnemy);
	action.SetEffectPlayer(statsEffectPlayer);
	action.SetName(name);
	return action;
}
