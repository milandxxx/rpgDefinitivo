using UnityEngine;
using System.Collections;

public class Spawner : MonoBehaviour
{
    public GameObject[] enemies;
    public Transform[] spawnPoints;
    public float spawnInterval = 5f;

    void Start()
    {
        StartCoroutine(SpawnLoop());
    }

    IEnumerator SpawnLoop()
    {
        while(true)
        {
            int idxEnemy = Random.Range(0, enemies.Length);
            int idxPoint = Random.Range(0, spawnPoints.Length);
            Instantiate(enemies[idxEnemy], spawnPoints[idxPoint].position, Quaternion.identity);
            yield return new WaitForSeconds(spawnInterval);
        }
    }
}
