using UnityEngine;

[System.Serializable]
public class PlayerStats
{
    public int level = 1;
    public int hp;
    public int stamina;
    public int atk;
    public int defense;

    public void Calculate()
    {
        hp = 100 + level * 12;
        stamina = 100 + level * 8;
        atk = 10 + level * 2;
        defense = Mathf.RoundToInt(5 + level * 1.5f);
    }
}
