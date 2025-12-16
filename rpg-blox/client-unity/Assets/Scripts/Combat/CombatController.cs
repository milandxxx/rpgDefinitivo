using UnityEngine;

public class CombatController : MonoBehaviour
{
    public PlayerStats stats;
    public float attackCooldown = 1f;
    private float lastAttack;

    void Start() { stats.Calculate(); }

    void Update()
    {
        if (Input.GetMouseButtonDown(0)) { TryAttack(); }
    }

    void TryAttack()
    {
        if (Time.time - lastAttack < attackCooldown) return;
        lastAttack = Time.time;
        string json = ""{\""action\"":\""attack\""}"";
        PlayerNetwork.Instance.Send(json);
        Debug.Log(""Ataque enviado"");
    }
}
