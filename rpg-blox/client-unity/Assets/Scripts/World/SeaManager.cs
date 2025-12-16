using UnityEngine;

public enum SeaType { Sea1, Sea2, Sea3, Sea4, Sea5 }

public class SeaManager : MonoBehaviour
{
    public static SeaManager Instance;
    public SeaType currentSea = SeaType.Sea1;

    void Awake() { Instance = this; }

    public void ChangeSea(SeaType sea)
    {
        currentSea = sea;
        Debug.Log(""Entraste a: "" + sea);
    }
}
