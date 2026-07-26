from django.db import models


class ProductType(models.TextChoices):
    """
    Product classification.
    """

    VEGETABLE = "VEGETABLE", "Vegetable"
    FRUIT = "FRUIT", "Fruit"
    GRAIN = "GRAIN", "Grain"
    PULSE = "PULSE", "Pulse"
    DAIRY = "DAIRY", "Dairy"
    FLOWER = "FLOWER", "Flower"
    HERB = "HERB", "Herb"
    SPICE = "SPICE", "Spice"
    OIL_SEED = "OIL_SEED", "Oil Seed"
    DRY_FRUIT = "DRY_FRUIT", "Dry Fruit"
    HONEY = "HONEY", "Honey"
    EGG = "EGG", "Egg"
    FISH = "FISH", "Fish"
    MEAT = "MEAT", "Meat"
    PLANT = "PLANT", "Plant"
    OTHER = "OTHER", "Other"


class ProductUnit(models.TextChoices):
    """
    Default selling unit.
    """

    KG = "KG", "Kilogram"
    GRAM = "GRAM", "Gram"
    QUINTAL = "QUINTAL", "Quintal"
    TON = "TON", "Ton"

    LITER = "LITER", "Liter"
    ML = "ML", "Milliliter"

    PIECE = "PIECE", "Piece"
    UNIT = "UNIT", "Unit"
    DOZEN = "DOZEN", "Dozen"
    BUNCH = "BUNCH", "Bunch"

    BAG = "BAG", "Bag"
    BOX = "BOX", "Box"
    PACK = "PACK", "Pack"
    TRAY = "TRAY", "Tray"
    BOTTLE = "BOTTLE", "Bottle"
    SACK = "SACK", "Sack"
    CRATE = "CRATE", "Crate"


class ProductSeason(models.TextChoices):
    """
    Product availability season.
    """

    YEAR_ROUND = "YEAR_ROUND", "Year Round"
    SUMMER = "SUMMER", "Summer"
    WINTER = "WINTER", "Winter"
    MONSOON = "MONSOON", "Monsoon"
    SEASONAL = "SEASONAL", "Seasonal"


class StorageType(models.TextChoices):
    """
    Storage requirement.
    """

    AMBIENT = "AMBIENT", "Ambient"
    REFRIGERATED = "REFRIGERATED", "Refrigerated"
    FROZEN = "FROZEN", "Frozen"


class CatalogStatus(models.TextChoices):
    """
    Farm2Home catalog status.
    """

    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"
    ARCHIVED = "ARCHIVED", "Archived"


class SupplierProductStatus(models.TextChoices):
    """
    Supplier product lifecycle.
    """

    DRAFT = "DRAFT", "Draft"
    SUBMITTED = "SUBMITTED", "Submitted"
    PENDING_REVIEW = "PENDING_REVIEW", "Pending Review"
    APPROVED = "APPROVED", "Approved"
    REJECTED = "REJECTED", "Rejected"
    LIVE = "LIVE", "Live"
    OUT_OF_STOCK = "OUT_OF_STOCK", "Out of Stock"
    ARCHIVED = "ARCHIVED", "Archived"


class CatalogImageType(models.TextChoices):
    """
    Catalog product images.
    """

    PRIMARY = "PRIMARY", "Primary"
    GALLERY = "GALLERY", "Gallery"


class SupplierImageType(models.TextChoices):
    """
    Supplier uploaded images.
    """

    PRIMARY = "PRIMARY", "Primary"
    GALLERY = "GALLERY", "Gallery"
    FARM = "FARM", "Farm"
    HARVEST = "HARVEST", "Harvest"
    PACKAGING = "PACKAGING", "Packaging"
    CERTIFICATE = "CERTIFICATE", "Certificate"