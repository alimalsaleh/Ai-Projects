import csv
# Lint as: python3
import os

import datasets


logger = datasets.logging.get_logger(__name__)


_CITATION = """\
@InProceedings{D17-1063,
  author = "Zhang, Xingxing and Lapata, Mirella",
  title = "Sentence Simplification with Deep Reinforcement Learning",
  booktitle = "Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing",
  year = "2017",
  publisher = "Association for Computational Linguistics",
  pages = "595--605",
  location = "Copenhagen, Denmark",
  url = "http://aclweb.org/anthology/D17-1063"
}
"""

_DESCRIPTION = "WikiLarge corpus for sentence simplification gathered by Zhang, Xingxing and Lapata, Mirella."

_URLS = {
    "train_src_ori": "https://huggingface.co/datasets/waboucay/wikilarge/resolve/main/wiki.full.aner.ori.train.src?download=true",
    "train_dst_ori": "https://huggingface.co/datasets/waboucay/wikilarge/resolve/main/wiki.full.aner.ori.train.dst?download=true",
    "valid_src_ori": "https://huggingface.co/datasets/waboucay/wikilarge/raw/main/wiki.full.aner.ori.valid.src",
    "valid_dst_ori": "https://huggingface.co/datasets/waboucay/wikilarge/raw/main/wiki.full.aner.ori.valid.dst",
    "test_src_ori": "https://huggingface.co/datasets/waboucay/wikilarge/raw/main/wiki.full.aner.ori.test.src",
    "test_dst_ori": "https://huggingface.co/datasets/waboucay/wikilarge/raw/main/wiki.full.aner.ori.test.dst",
    "train_src_ner": "https://huggingface.co/datasets/waboucay/wikilarge/resolve/main/wiki.full.aner.train.src?download=true",
    "train_dst_ner": "https://huggingface.co/datasets/waboucay/wikilarge/resolve/main/wiki.full.aner.train.dst?download=true",
    "valid_src_ner": "https://huggingface.co/datasets/waboucay/wikilarge/raw/main/wiki.full.aner.valid.src",
    "valid_dst_ner": "https://huggingface.co/datasets/waboucay/wikilarge/raw/main/wiki.full.aner.valid.dst",
    "test_src_ner": "https://huggingface.co/datasets/waboucay/wikilarge/raw/main/wiki.full.aner.test.src",
    "test_dst_ner": "https://huggingface.co/datasets/waboucay/wikilarge/raw/main/wiki.full.aner.test.dst"
}
_TRAINING_FILE = "train.csv"
_DEV_FILE = "valid.csv"
_TEST_FILE = "test.csv"

class WikiLargeConfig(datasets.BuilderConfig):
    """BuilderConfig for WikiLarge dataset"""

    def __init__(self, **kwargs):
        """BuilderConfig for WikiLarge dataset
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(WikiLargeConfig, self).__init__(**kwargs)


class WikiLarge(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version("1.0.0", "")
    BUILDER_CONFIG_CLASS = WikiLargeConfig
    BUILDER_CONFIGS = [
        WikiLargeConfig(
            name="original",
            version=datasets.Version("1.0.0", ""),
            description=_DESCRIPTION,
        ),
        WikiLargeConfig(
            name="ner_tagged",
            version=datasets.Version("1.0.0", ""),
            description=_DESCRIPTION + "\n\nVersion with NER tags replacing named entities.",
        )
    ]

    def _info(self):
        features = datasets.Features(
            {
                "complex": datasets.Value("string"),
                "simple": datasets.Value("string"),
            }
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            supervised_keys=None,
            homepage="https://github.com/XingxingZhang/dress/tree/master",
        )

    def _split_generators(self, dl_manager):
        dl_files = dl_manager.download(_URLS)

        train_path = os.path.join(os.path.dirname(dl_files["train_src_ori"]), _TRAINING_FILE)
        valid_path = os.path.join(os.path.dirname(dl_files["train_src_ori"]), _DEV_FILE)
        test_path = os.path.join(os.path.dirname(dl_files["train_src_ori"]), _TEST_FILE)

        if self.config.name == "original":
            train_src_path = os.path.abspath(dl_files["train_src_ori"])
            train_dst_path = os.path.abspath(dl_files["train_dst_ori"])
            valid_src_path = os.path.abspath(dl_files["valid_src_ori"])
            valid_dst_path = os.path.abspath(dl_files["valid_dst_ori"])
            test_src_path = os.path.abspath(dl_files["test_src_ori"])
            test_dst_path = os.path.abspath(dl_files["test_dst_ori"])
        elif self.config.name == "ner_tagged":
            train_src_path = os.path.abspath(dl_files["train_src_ner"])
            train_dst_path = os.path.abspath(dl_files["train_dst_ner"])
            valid_src_path = os.path.abspath(dl_files["valid_src_ner"])
            valid_dst_path = os.path.abspath(dl_files["valid_dst_ner"])
            test_src_path = os.path.abspath(dl_files["test_src_ner"])
            test_dst_path = os.path.abspath(dl_files["test_dst_ner"])
        else:
            raise FileNotFoundError

        with open(train_src_path, encoding="utf-8") as train_src, open(train_dst_path, encoding="utf-8") as train_dst, open(train_path, "w", encoding="utf-8") as train_csv, \
             open(valid_src_path, encoding="utf-8") as valid_src, open(valid_dst_path, encoding="utf-8") as valid_dst, open(valid_path, "w", encoding="utf-8") as valid_csv, \
             open(test_src_path, encoding="utf-8") as test_src, open(test_dst_path, encoding="utf-8") as test_dst, open(test_path, "w", encoding="utf-8") as test_csv:

            field_names = ["complex", "simple"]
            train_writer = csv.DictWriter(train_csv, fieldnames=field_names)
            valid_writer = csv.DictWriter(valid_csv, fieldnames=field_names)
            test_writer = csv.DictWriter(test_csv, fieldnames=field_names)

            train_writer.writeheader()
            valid_writer.writeheader()
            test_writer.writeheader()

            for src, dst in zip(train_src.readlines(), train_dst.readlines()):
                train_writer.writerow({"complex": src.strip(), "simple": dst.strip()})

            for src, dst in zip(valid_src.readlines(), valid_dst.readlines()):
                valid_writer.writerow({"complex": src.strip(), "simple": dst.strip()})

            for src, dst in zip(test_src.readlines(), test_dst.readlines()):
                test_writer.writerow({"complex": src.strip(), "simple": dst.strip()})

        data_files = {
            "train": train_path,
            "valid": valid_path,
            "test": test_path,
        }

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": data_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": data_files["valid"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": data_files["test"]}),
        ]

    def _generate_examples(self, filepath):
        """This function returns the examples in the raw (text) form."""

        with open(filepath, encoding="utf-8") as f:
            guid = 0

            reader = csv.DictReader(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                yield guid, {
                    "complex": row["complex"],
                    "simple": row["simple"]
                }
                guid += 1
