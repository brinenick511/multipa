from datasets import load_dataset

def download_and_save_all_splits(language, save_path):
    # 定义数据集名和版本
    dataset_name = "mozilla-foundation/common_voice_11_0"
    # 加载数据集的所有可用分割
    dataset = load_dataset(dataset_name, language, split="train")
    # 保存到本地指定路径
    for split in dataset.keys():
        dataset[split].save_to_disk(f"{save_path}/{language}/{split}")

# 例如，下载并保存 Tamil 语言的所有数据分割到指定目录
download_and_save_all_splits("ta", "/data/yanghq/datasets/mozilla-foundation/common_voice_11_0")