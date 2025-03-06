# ベースイメージとして公式のRabbitMQイメージを使用
FROM rabbitmq:3-management

# ポートを公開
EXPOSE 5672 15672

# デフォルトのユーザーとパスワードを設定
ENV RABBITMQ_DEFAULT_USER=user
ENV RABBITMQ_DEFAULT_PASS=password

# RabbitMQサーバーを起動
CMD ["rabbitmq-server"]
