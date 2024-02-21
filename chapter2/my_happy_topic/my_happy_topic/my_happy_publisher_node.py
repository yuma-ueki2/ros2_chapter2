import rclpy  # 1. ROS2 Python モジュールのインポート
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート
from std_msgs.msg import String


class MyHappyPublisherNode(Node):  # クラス
    def __init__(self):  # コンストラクタ
        super().__init__('my_happy_publisher_node')  # 基底クラスコンストラクタのよび出し
        self.pub = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(1, self.timer_callback)  # タイマーの生成
        self.i = 10

    def timer_callback(self):  # タイマーのコールバック関数
        msg = String()
        if self.i > 0:
            msg.data = f'ハッピーわいワールド {self.i}'
        else:
            msg.data = f'終わり'
            self.destroy_timer(self.timer)
        self.pub.publish(msg)
        self.get_logger().info(f'パブリッシュ: {msg.data}')
        self.i -= 1


def main():  # main 関数
    print('プログラム開始')
    rclpy.init()               # 2. 初期化
    node = MyHappyPublisherNode()         # 3. ノードの生成
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Ctrl+Cが押されたった')    
    rclpy.shutdown()           # 5. 終了処理
    print('プログラム終了')
