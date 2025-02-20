import logging
import logging.config
import os

# 設定ファイルのパス
config_path = os.path.join(os.path.dirname(__file__), 'logging.conf')

# 設定ファイルの読み込み
logging.config.fileConfig(config_path)

# ロガーの取得
logger = logging.getLogger('my_logger')

# ログメッセージの出力
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
