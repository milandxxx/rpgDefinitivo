using UnityEngine;
using UnityEngine.UI;

public class UIPlayerHUD : MonoBehaviour
{
    public Text levelText;
    public Text hpText;
    public PlayerStats stats;

    void Update()
    {
        levelText.text = ""Lv. "" + stats.level;
        hpText.text = ""HP: "" + stats.hp;
    }
}
