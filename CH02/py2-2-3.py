import json

config = {"url":"https://example.com","retry":3}

with open("config.json", "w") as f:
    json.dump(config, f)


with open("config.json", "r") as f:
    loaded_config = json.load(f)
    print(loaded_config)


