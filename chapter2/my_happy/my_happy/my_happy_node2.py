import rclpy  # 1. ROS2 Python モジュールのインポート
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート


class HappyNode2(Node):  # HappyNode2クラス
    def __init__(self):  # コンストラクタ
        print('ノードの生成')
        super().__init__('my_happy_node2')  # 基底クラスコンストラクタのよび出し
        self.timer = self.create_timer(1.0, self.timer_callback)  # タイマーの生成

    def timer_callback(self):  # タイマーのコールバック関数
        self.get_logger().info('ハッピーわいワールド２')


def main():  # main 関数
    print('プログラム開始')
    rclpy.init()               # 2. 初期化
    node = HappyNode2()        # 3. ノードの生成
    rclpy.spin(node)           # 4. ノードの処理．コールバック関数を繰り返しよび出す．
    rclpy.shutdown()           # 5. 終了処理
    print('プログラム終了')
