import tweepy

# 添加您的 Twitter API 密钥和访问令牌
from app.gpt import get_answer_from_chatGPT

CONSUMER_KEY = '4zV9ddzLgnbUsHUrHSVdc8Y5U'
CONSUMER_SECRET = 'k5qNIOI70mYvo4IpBtnfEelaisDIiGW10Vl4LSmoXyC6oXecQz'
ACCESS_TOKEN = '1522472373202522112-uH2l9InMw4lwMj3A9luQjyltGTk80F'
ACCESS_TOKEN_SECRET = '9B7tZT19MucNWKPm7hhhwMsJ20cURD5kBakX24l9p0J5v'

# 认证
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# 创建 API 对象
api = tweepy.API(auth)
text="总结这个NFT项目"
screen_name='LazyLionsNFT'
# 获取用户概要信息
user = api.get_user(screen_name=screen_name)
# text = text + "用户名:" + user.screen_name + "\n"
# text = text + "关注者数:" + str(user.followers_count) + "\n"
# text = text + "好友数:" + str(user.friends_count) + "\n"
text = text + "bio:" + str(user.description) + "\n"
print(text)


# 获取用户最新的 10 条推文
tweets = api.user_timeline(screen_name=screen_name, count=20, tweet_mode='extended', exclude_replies=True)

# 打印每条推文
for tweet in tweets:
    print("\n时间: ", tweet.created_at)
    print("内容: ", tweet.full_text)
    text = text + "推文:" + str(tweet.full_text) + "\n"
    print("点赞数: ", tweet.favorite_count)
    print("转发数: ", tweet.retweet_count)


gpt_response, total_llm_model_tokens, total_embedding_model_tokens = get_answer_from_chatGPT(text)

print(gpt_response)