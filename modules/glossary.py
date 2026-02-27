"""
Domain-aware glossary helpers for EN/ZH -> RU translation.

Danila_AI supports two domain families:
1) medical/pharmacopeia
2) judicial/business

Glossary output is consumed by prompt-building code in modules/translator.py.
"""

from __future__ import annotations

from collections import OrderedDict

SUPPORTED_SOURCE_LANGUAGES = ("auto", "en", "zh")
SUPPORTED_DOMAIN_PROFILES = ("combined", "medical", "judicial_business")


MEDICAL_EN_RU = {
    "Certificate of Analysis": "Сертификат анализа",
    "COA": "Сертификат анализа",
    "Specification": "Спецификация",
    "Product Name": "Наименование продукта",
    "Batch Number": "Номер серии",
    "Lot Number": "Номер серии",
    "Manufacturing Date": "Дата производства",
    "Expiry Date": "Срок годности",
    "Retest Date": "Дата переконтроля",
    "Manufacturer": "Производитель",
    "Supplier": "Поставщик",
    "Test": "Испытание",
    "Test Method": "Метод испытания",
    "Result": "Результат",
    "Acceptance Criteria": "Критерии приемлемости",
    "Appearance": "Внешний вид",
    "Assay": "Количественное определение",
    "Purity": "Чистота",
    "Impurities": "Примеси",
    "Related Substances": "Родственные примеси",
    "Residual Solvents": "Остаточные растворители",
    "Heavy Metals": "Тяжелые металлы",
    "Loss on Drying": "Потеря в массе при высушивании",
    "Water Content": "Содержание воды",
    "Identification": "Идентификация",
    "HPLC": "ВЭЖХ",
    "GC": "ГХ",
    "IR": "ИК",
    "USP": "Фармакопея США",
    "EP": "Европейская фармакопея",
    "Pharmacopeia": "Фармакопея",
    "Storage Conditions": "Условия хранения",
    "Conforms": "Соответствует",
    "Complies": "Соответствует",
    "Not Detected": "Не обнаружено",
}


MEDICAL_ZH_RU = {
    "分析证书": "Сертификат анализа",
    "产品名称": "Наименование продукта",
    "批号": "Номер серии",
    "生产日期": "Дата производства",
    "有效期": "Срок годности",
    "复验期": "Дата переконтроля",
    "生产商": "Производитель",
    "供应商": "Поставщик",
    "检验项目": "Испытание",
    "检验方法": "Метод испытания",
    "结果": "Результат",
    "标准": "Критерии приемлемости",
    "外观": "Внешний вид",
    "含量测定": "Количественное определение",
    "纯度": "Чистота",
    "杂质": "Примеси",
    "有关物质": "Родственные примеси",
    "残留溶剂": "Остаточные растворители",
    "重金属": "Тяжелые металлы",
    "干燥失重": "Потеря в массе при высушивании",
    "水分": "Содержание воды",
    "鉴别": "Идентификация",
    "储存条件": "Условия хранения",
    "符合规定": "Соответствует",
    "未检出": "Не обнаружено",
}


JUDICIAL_BUSINESS_EN_RU = {
    "Agreement": "Соглашение",
    "Contract": "Договор",
    "Party": "Сторона",
    "Parties": "Стороны",
    "Counterparty": "Контрагент",
    "Governing Law": "Применимое право",
    "Jurisdiction": "Юрисдикция",
    "Arbitration": "Арбитраж",
    "Dispute Resolution": "Разрешение споров",
    "Confidentiality": "Конфиденциальность",
    "Non-Disclosure Agreement": "Соглашение о неразглашении",
    "Liability": "Ответственность",
    "Indemnification": "Возмещение убытков",
    "Damages": "Убытки",
    "Force Majeure": "Форс-мажор",
    "Termination": "Расторжение",
    "Breach": "Нарушение",
    "Claim": "Требование",
    "Plaintiff": "Истец",
    "Defendant": "Ответчик",
    "Judgment": "Судебное решение",
    "Court": "Суд",
    "Regulation": "Нормативный акт",
    "Compliance": "Соблюдение требований",
    "Invoice": "Счет",
    "Payment Terms": "Условия оплаты",
    "Purchase Order": "Заказ на поставку",
    "Statement of Work": "Техническое задание",
    "Annex": "Приложение",
    "Appendix": "Приложение",
    "Seal": "Печать",
    "Authorized Signatory": "Уполномоченный подписант",
}


JUDICIAL_BUSINESS_ZH_RU = {
    "合同": "Договор",
    "协议": "Соглашение",
    "甲方": "Сторона А",
    "乙方": "Сторона Б",
    "适用法律": "Применимое право",
    "管辖权": "Юрисдикция",
    "仲裁": "Арбитраж",
    "争议解决": "Разрешение споров",
    "保密": "Конфиденциальность",
    "违约": "Нарушение",
    "赔偿": "Возмещение убытков",
    "责任": "Ответственность",
    "不可抗力": "Форс-мажор",
    "终止": "Расторжение",
    "诉讼": "Судебный процесс",
    "原告": "Истец",
    "被告": "Ответчик",
    "法院": "Суд",
    "判决": "Судебное решение",
    "合规": "Соблюдение требований",
    "付款条件": "Условия оплаты",
    "发票": "Счет",
    "采购订单": "Заказ на поставку",
    "附件": "Приложение",
    "盖章": "Печать",
    "授权签字人": "Уполномоченный подписант",
}


def _merge_glossaries(*items: dict[str, str]) -> dict[str, str]:
    merged: OrderedDict[str, str] = OrderedDict()
    for glossary in items:
        for key, value in glossary.items():
            merged[key] = value
    return dict(merged)


def _normalise_source_language(source_language: str) -> str:
    value = (source_language or "").strip().lower()
    return value if value in SUPPORTED_SOURCE_LANGUAGES else "auto"


def _normalise_domain_profile(domain_profile: str) -> str:
    value = (domain_profile or "").strip().lower()
    return value if value in SUPPORTED_DOMAIN_PROFILES else "combined"


def get_glossary_dict(
    source_language: str = "auto",
    domain_profile: str = "combined",
) -> dict[str, str]:
    """
    Return merged glossary dict for selected source language + domain profile.
    """
    lang = _normalise_source_language(source_language)
    domain = _normalise_domain_profile(domain_profile)

    use_en = lang in ("auto", "en")
    use_zh = lang in ("auto", "zh")

    include_medical = domain in ("combined", "medical")
    include_judicial = domain in ("combined", "judicial_business")

    parts: list[dict[str, str]] = []

    if include_medical and use_en:
        parts.append(MEDICAL_EN_RU)
    if include_medical and use_zh:
        parts.append(MEDICAL_ZH_RU)
    if include_judicial and use_en:
        parts.append(JUDICIAL_BUSINESS_EN_RU)
    if include_judicial and use_zh:
        parts.append(JUDICIAL_BUSINESS_ZH_RU)

    return _merge_glossaries(*parts)


def get_glossary_prompt_section(
    source_language: str = "auto",
    domain_profile: str = "combined",
) -> str:
    """
    Build formatted glossary lines for inclusion in the translator prompt.
    """
    glossary = get_glossary_dict(
        source_language=source_language,
        domain_profile=domain_profile,
    )
    return "\n".join(f'  "{src}" -> "{dst}"' for src, dst in glossary.items())
