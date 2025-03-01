# Problem Statement

The goal is to create a machine learning model that extracts entity values from images. This capability is crucial in fields like healthcare, e-commerce, and content moderation, where precise product information is vital. As digital marketplaces expand, many products lack detailed textual descriptions, making it essential to obtain key details directly from images. These images provide important information such as weight, volume, voltage, wattage, dimensions, and many more, which are critical for digital stores.

# Dataset Description

There were 2 different CSV files provided namely train.csv and test.csv. The dataset consists of the following columns:

1. index: A unique identifier (ID) for the data sample
2. image_link: Public URL where the product image is available for download. e.g. link
3. group_id: Category code of the product
4. entity_name: Product entity name. For eg: “item_weight”
5. entity_value: Product entity value. For eg: “34 gram”
6. Note: For test.csv, you will not see the column `entity_value` as it is the target variable.
