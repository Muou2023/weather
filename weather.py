以下是使用Python中的requests和json模块来查询北京天气的示例代码：

```python
import requests

# 发送HTTP请求获取天气数据
url = "https://api.openweathermap.org/data/2.5/weather?q=Beijing&appid=YOUR_API_KEY&units=metric"
# 将 YOUR_API_KEY 替换为你实际的 API Key
response = requests.get(url)

# 解析JSON数据
data = response.json()
temperature = data["main"]["temp"]
description = data["weather"][0]["description"].capitalize()

# 输出天气信息
print(f"Current temperature in Beijing is {temperature}°C with {description}.")
```

注意，为了运行这个代码，你需要去 [OpenWeatherMap](https://openweathermap.org/) 网站上注册一个帐号，然后生成一个 API Key。将代码中的 YOUR_API_KEY 替换为你生成的 API Key 后，就可以使用了。
