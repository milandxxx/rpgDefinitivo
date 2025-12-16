using UnityEngine;
using System.Collections;

public class PlayerSkills : MonoBehaviour
{
    public float cooldownTime = 3f;
    private bool skillReady = true;

    public void UseSkill(string skillName)
    {
        if (!skillReady) return;
        skillReady = false;
        Debug.Log(""Usando skill: "" + skillName);
        StartCoroutine(Cooldown());
        // Lógica de skill + partículas
    }

    IEnumerator Cooldown()
    {
        yield return new WaitForSeconds(cooldownTime);
        skillReady = true;
    }
}
