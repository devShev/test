from pydantic import BaseModel


class CardOptionResponseSchema(BaseModel):
    name: str
    value: str
    charc_type: int | None = None


class CardCompositionResponseSchema(BaseModel):
    name: str


class CardCertificateValueResposneSchema(BaseModel):
    verified: bool | None = None


class CardFullColorResponseSchema(BaseModel):
    nm_id: int


class CardSellingResponseSchema(BaseModel):
    no_return_map: int | None = None
    brand_name: str | None = None
    brand_hash: str | None = None
    supplier_id: int


class CardMediaResponseSchema(BaseModel):
    has_video: bool | None = None
    is_autoplaying_video: bool | None = None
    photo_count: int


class CardDataResponseSchema(BaseModel):
    subject_id: int
    subject_root_id: int
    chrt_ids: list[int]


class CardGrouppedOptionResponseSchema(BaseModel):
    group_name: str
    options: list[CardOptionResponseSchema]


class CardResponseSchema(BaseModel):
    imt_id: int
    nm_id: int
    has_rich: bool | None = None
    imt_name: str
    slug: str
    subj_name: str
    subj_root_name: str
    vendor_code: str
    description: str
    options: list[CardOptionResponseSchema]
    compositions: list[CardCompositionResponseSchema] | None = None
    certificate: CardCertificateValueResposneSchema
    colors: list[int]
    contents: str | None = None
    full_colors: list[CardFullColorResponseSchema]
    selling: CardSellingResponseSchema
    media: CardMediaResponseSchema
    data: CardDataResponseSchema
    grouped_options: list[CardGrouppedOptionResponseSchema]
    enable_tags: bool | None = None
    has_photo_tags: bool | None = None
