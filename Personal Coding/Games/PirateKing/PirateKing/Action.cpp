#include "Action.h"
void CAction::SetEffectEnemy(int stats[11])
{
	for (int i = 0; i < 11; i++)
	{
		statsEffectEnemy[i] = stats[i];
	}
}

void CAction::SetEffectPlayer(int stats[11])
{
	for (int i = 0; i < 11; i++)
	{
		statsEffectPlayer[i] = stats[i];
	}
}

void CAction::SetEnemyDuration(int dur[11])
{
	for (int i = 0; i < 11; i++)
	{
		EnemyEffectDuration[i] = dur[i];
	}
}

void CAction::SetPlayerDuration(int dur[11])
{
	for (int i = 0; i < 11; i++)
	{
		PlayerEffectDuration[i] = dur[i];
	}
}

