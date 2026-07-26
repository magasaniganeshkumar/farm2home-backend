from django.db import models


class ProductUnit(models.TextChoices):
    KG = "KG", "Kilogram"
    GRAM = "GRAM", "Gram"
    QUINTAL = "QUINTAL", "Quintal"
    TON = "TON", "Ton"

    LITER = "LITER", "Liter"
    ML = "ML", "Milliliter"

    PIECE = "PIECE", "Piece"
    DOZEN = "DOZEN", "Dozen"
    BUNCH = "BUNCH", "Bunch"

    BAG = "BAG", "Bag"
    BOX = "BOX", "Box"
    PACK = "PACK", "Pack"
    TRAY = "TRAY", "Tray"
    BOTTLE = "BOTTLE", "Bottle"
    SACK = "SACK", "Sack"


class ProductSeason(models.TextChoices):
    YEAR_ROUND = "YEAR_ROUND", "Year Round"
    SUMMER = "SUMMER", "Summer"
    WINTER = "WINTER", "Winter"
    MONSOON = "MONSOON", "Monsoon"
    SEASONAL = "SEASONAL", "Seasonal"


class StorageType(models.TextChoices):
    ROOM_TEMPERATURE = "ROOM_TEMPERATURE", "Room Temperature"
    REFRIGERATED = "REFRIGERATED", "Refrigerated"
    FROZEN = "FROZEN", "Frozen"


class ProductStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PENDING_REVIEW = "PENDING_REVIEW", "Pending Review"
    APPROVED = "APPROVED", "Approved"
    COMING_SOON = "COMING_SOON", "Coming Soon"
    LIVE = "LIVE", "Live"
    OUT_OF_STOCK = "OUT_OF_STOCK", "Out of Stock"
    DISABLED = "DISABLED", "Disabled"
    ARCHIVED = "ARCHIVED", "Archived"


class ProductImageType(models.TextChoices):
    PRIMARY = "PRIMARY", "Primary"
    GALLERY = "GALLERY", "Gallery"
    FARM = "FARM", "Farm"
    HARVEST = "HARVEST", "Harvest"
    PACKAGING = "PACKAGING", "Packaging"
    CERTIFICATE = "CERTIFICATE", "Certificate"