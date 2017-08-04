from scrapy_rabbitmq import connection
from unittest import TestCase, main
from logging import basicConfig, DEBUG, debug
basicConfig(level=DEBUG)


class CommonTest(TestCase):
    def test_get_conn_localhost(self):
        settings = {
            'host': 'localhost',
            'port': 5672,
        }
        conn = connection.from_settings(settings)
        debug(conn)


if __name__ == '__main__':
    main()
