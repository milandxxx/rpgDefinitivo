using UnityEngine;
using NativeWebSocket;
using System.Text;

public class PlayerNetwork : MonoBehaviour
{
    public static PlayerNetwork Instance;
    private WebSocket ws;

    void Awake()
    {
        if (Instance == null) Instance = this;
        else Destroy(gameObject);
    }

    async void Start()
    {
        ws = new WebSocket(""ws://localhost:8765"");

        ws.OnOpen += () => { Debug.Log(""Conectado al servidor""); };
        ws.OnMessage += (bytes) => {
            string msg = Encoding.UTF8.GetString(bytes);
            Debug.Log(""Server: "" + msg);
        };
        ws.OnError += (e) => { Debug.LogError(""WS Error: "" + e); };
        await ws.Connect();
    }

    public async void Send(string json)
    {
        if (ws.State == WebSocketState.Open)
            await ws.SendText(json);
    }

    void Update() { ws.DispatchMessageQueue(); }
    async void OnApplicationQuit() { await ws.Close(); }
}
