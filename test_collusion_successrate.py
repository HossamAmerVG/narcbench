import json, glob, os

root = "data/raw/qwen2_5_1_5b/core"

# root = "data/raw/qwen2_5_1_5b/transfer"
# root = "data/raw/qwen2_5_1_5b/stego"

# root = "data/raw/qwen3_32b/transfer"
# root = "data/raw/qwen3_32b/stego"

n_coll = succ = 0

for cfg in glob.glob(f"{root}/*/run_config.json"):
    d = json.load(open(cfg))

    if d.get("mode") != "collusion":
        continue
    n_coll +=1
    succ += bool(d.get("collusion_success"))

rate = succ / n_coll if n_coll else 0
print("Collusion runs: ", n_coll)
print("collusion sucess: ", succ)
print("Rate: ", rate)


