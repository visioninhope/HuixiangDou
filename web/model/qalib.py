from pydantic import BaseModel
from typing import Optional, List


class Feishu(BaseModel):
    webhookUrl: str
    appId: str
    appSecret: str
    encryptKey: str
    verificationToken: str
    eventUrl: str


class Wechat(BaseModel):
    onMessageUrl: str


class WebSearch(BaseModel):
    token: str


class QalibInfo(BaseModel):
    featureStoreId: Optional[str] = None
    name: Optional[str] = None
    docs: Optional[List[str]] = []
    docBase: Optional[str] = None
    status: Optional[int] = None
    suffix: Optional[str] = None
    feishu: Optional[Feishu] = None
    wechat: Optional[Wechat] = None
    webSearch: Optional[WebSearch] = None


class QalibPositiveNegative(BaseModel):
    positives: Optional[List] = None
    negatives: Optional[List] = None


class QalibSample(QalibPositiveNegative):
    name: str
    featureStoreId: str
    confirmed: bool