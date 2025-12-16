using NativeWebSocket;
using UnityEngine;

public class PlayerNetwork : MonoBehaviour
{
    WebSocket ws;

    async void Start()
    {
        ws = new WebSocket(""ws://localhost:8765"");

        ws.OnMessage += (bytes) =>
        {
            string msg = System.Text.Encoding.UTF8.GetString(bytes);
            Debug.Log(""Server: "" + msg);
        };

        await ws.Connect();
    }

    void Update()
    {
        ws.DispatchMessageQueue();
    }
}
