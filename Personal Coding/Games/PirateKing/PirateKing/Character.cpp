#include "Character.h"
#include <fstream>
#include <iostream>
#include <sstream>

void CCharacter::SetBaseStats(int stats[11])
{
	for (int i = 0; i < 11; i++)
	{
		baseStats[i] = stats[i];
	}
}

void CCharacter::SetActionStats(int stats[11])
{
	for (int i = 0; i < 11; i++)
	{
		actionStats[i] = stats[i];
	}
}

CAction CCharacter::GetFileAction(int actionID)
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

void CCharacter::UpdateOffenseStats(CAction action)
{
    int tempP[11] = {};     //Temporary Player stats array 
    for (int j = 0; j < 11; j++)
    {
        tempP[j] += GetActionStats()[j] + action.GetEffectPlayer()[j];
    }
    tempP[9] -= action.GetCost();
    SetActionStats(tempP);
}

void CCharacter::UpdateDefenceStats(CAction action, int enemyStats[11])
{
    int tempE[11] = {};
    for (int j = 0; j < 11; j++)
    {
        if (j == 7 && action.GetEffectEnemy()[j] != 0)
        {
            if (tempE[3] > (enemyStats[0] - action.GetEffectEnemy()[j]))
            {
                tempE[3] -= (enemyStats[0] + action.GetEffectEnemy()[j]);
            }
            else
            {
                tempE[j] += tempE[3] - (enemyStats[0] - action.GetEffectEnemy()[j]);
                tempE[3] = 0;
            }
            tempE[j] += GetActionStats()[j];
        }
        else
        {
            tempE[j] += GetActionStats()[j] + action.GetEffectEnemy()[j];
        }
    }
    SetActionStats(tempE);
}

