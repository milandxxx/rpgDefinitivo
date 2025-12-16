using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public float speed = 6f;
    public float rotationSpeed = 10f;

    void Update()
    {
        float h = Input.GetAxis(""Horizontal"");
        float v = Input.GetAxis(""Vertical"");
        Vector3 dir = new Vector3(h,0,v);

        if (dir.magnitude > 0.1f)
        {
            transform.Translate(dir.normalized * speed * Time.deltaTime, Space.World);
            Quaternion rot = Quaternion.LookRotation(dir);
            transform.rotation = Quaternion.Slerp(transform.rotation, rot, rotationSpeed * Time.deltaTime);
        }
    }
}
