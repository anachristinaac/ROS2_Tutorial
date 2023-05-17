"""
MIT LICENSE

Copyright (C) 2023 Murilo Marques Marinho (www.murilomarinho.info)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import random
import rclpy
from rclpy.node import Node
from package_with_interfaces.srv import WhatIsThePoint


class WhatIsThePointServiceClientNode(Node):
    """A ROS2 Node with a Service Client for WhatIsThePoint."""

    def __init__(self):
        super().__init__('what_is_the_point_service_client')

        self.service_client = self.create_client(
            srv_type=WhatIsThePoint,
            srv_name='/what_is_the_point')

        while not self.service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service {} not available, waiting...'.format(self.service_client.srv_name))

        timer_period: float = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        """Method that is periodically called by the timer."""

        request = WhatIsThePoint.Request()
        if random.uniform(0, 1) < 0.5:
            request.quote.quote = "I wonder about the Ultimate Question of Life, the Universe, and Everything."
            request.quote.philosopher_name = "Creators of Deep Thought"
            request.quote.id = 1979
        else:
            request.quote.quote = """My life, it's potato... 
                                     In your working life, and your living
                                     it is always potatoes. I dream of potatoes."""
            request.quote.philosopher_name = "a young Maltese potato farmer"
            request.quote.id = 2013

        future = self.service_client.call_async(request)
        rclpy.spin_until_future_complete(
            node=self,
            future=future,
            timeout_sec=None
        )
        return future.result()


def main(args=None):
    """
    The main function.
    :param args: Not used directly by the user, but used by ROS2 to configure
    certain aspects of the Node.
    """
    try:
        rclpy.init(args=args)

        what_is_the_point_service_client_node = WhatIsThePointServiceClientNode()

        rclpy.spin(what_is_the_point_service_client_node)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
