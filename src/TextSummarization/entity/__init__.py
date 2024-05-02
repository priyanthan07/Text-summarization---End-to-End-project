from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
   root_dir: Path
   source_URL: str
   local_data_file: Path
   unzip_dir: Path


                                         # frozen means once the instance of the class is created, you cannot change its attributes.
@dataclass(frozen=True)                  # This can be useful for creating objects that should not be changed after they are created.
class DataValidationConfig:
   root_dir: Path
   STATUS_FILE: str
   ALL_REQUIRED_FILES: list


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

from dataclasses import dataclass
from pathlib import Path

@dataclass
class ModelTrainingConfig:
    root_dir : Path
    data_path : Path
    model_name : Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int