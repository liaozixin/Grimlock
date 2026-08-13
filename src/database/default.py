DEFAULT_PROVIDERS = [
    {
        "name": "DeepSeek",
        "api_key": "",
        "base_url": "https://api.deepseek.com",
        "models": [
            {
                "name": "deepseek-v4-flash",
                "max_context": 1000000
            },
            {
                "name": "deepseek-v4-pro",
                "max_context": 1000000
            }
        ]
    },
]


DEFAULT_THEMES = [
    {
        "name": "tokyo-night"
    }
]


DEFAULT_CONFIG = {
    "provider": "DeepSeek",
    "model": "deepseek-v4-flash",
    "theme": "tokyo-night"
}