from prompt import YING_SYSTEM_PROMPT, YI_MASTER_SYSTEM_PROMPT


class Config:
    MEMORY: str = "./memory"
    YING_SYSTEM_PROMPT: str = YING_SYSTEM_PROMPT
    YI_SYSTEM_PROMPT: str = YI_MASTER_SYSTEM_PROMPT

    ZHIPUAI_API_KEY: str = "your zhipuai api key"
    ZHIPUAI_MODEL: str = "your zhipuai model"

    OPENAI_API_BASE: str = "your openai api base"
    OPENAI_API_KEY: str = "your openai api key"
    OPENAI_MODEL_NAME: str = "your openai model"

    YING = "小樱"
    YI = "易大师"
