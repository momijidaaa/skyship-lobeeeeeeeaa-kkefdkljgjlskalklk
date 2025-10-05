
from mcstatus import BedrockServer

# ユーザー入力
ip = input("サーバーのIPアドレスを入力してください: ")
port_input = input("ポート番号を入力してください（未入力なら19132）: ")
port = int(port_input) if port_input else 19132

# サーバーオブジェクト作成
server = BedrockServer.lookup(f"{ip}:{port}")

try:
    status = server.status()
    print(f"\nサーバー状態: オンライン")
    print(f"バージョン: {status.version.version}")
    print(f"プレイヤー数: {status.players.online} / {status.players.max}")
    print(f"サーバーMotd: {status.motd}")
except Exception as e:
    print("\nサーバーに接続できませんでした。オフラインかIP/ポートが間違っている可能性があります。")
    # print(e)  # デバッグ用
