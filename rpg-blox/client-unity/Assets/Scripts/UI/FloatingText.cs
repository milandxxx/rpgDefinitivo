using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class FloatingText : MonoBehaviour
{
    public Text text;
    public float speed = 1f;
    public float duration = 1f;

    public void Show(string msg)
    {
        text.text = msg;
        StartCoroutine(FadeOut());
    }

    IEnumerator FadeOut()
    {
        float elapsed = 0f;
        Color c = text.color;
        while (elapsed < duration)
        {
            transform.Translate(Vector3.up * speed * Time.deltaTime);
            c.a = Mathf.Lerp(1, 0, elapsed/duration);
            text.color = c;
            elapsed += Time.deltaTime;
            yield return null;
        }
        Destroy(gameObject);
    }
}
