import rclpy  # 1. ROS2 Python モジュールのインポート
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート


class HappyNode3(Node):  # HappyNode2クラス
    def __init__(self):  # コンストラクタ
        print('ノードの生成')
        super().__init__('my_happy_node3')  # 基底クラスコンストラクタのよび出し
        self.timer = self.create_timer(1.0, self.timer_callback)  # タイマーの生成

    def timer_callback(self):  # タイマーのコールバック関数
        self.get_logger().info('ハッピーわいワールド3')


def main():  # main 関数
    print('プログラム開始')
    rclpy.init()               # 2. 初期化
    node = HappyNode3()        # 3. ノードの生成
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Ctrl+Cが押されたった')    
    rclpy.shutdown()           # 5. 終了処理
    print('プログラム終了')
