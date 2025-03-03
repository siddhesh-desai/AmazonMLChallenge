entity_unit_map = {
    'width': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard', 'cm', 'ft', 'in', '\'', 'mm', 'm'},
    'depth': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard', 'cm', 'ft', 'in', '\'', 'mm', 'm'},
    'height': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard', 'cm', 'ft', 'in', '\'', 'mm', 'm'},
    'item_weight': {'gram',
                    'kilogram',
                    'microgram',
                    'milligram',
                    'ounce',
                    'pound',
                    'ton',
                    'kg',
                    'gm',
                    'grams',
                    'kilo',
                    'mg'},
    'maximum_weight_recommendation': {'gram',
                                      'kilogram',
                                      'microgram',
                                      'milligram',
                                      'ounce',
                                      'pound',
                                      'ton',
                                      'kg',
                                      'gm',
                                      'grams',
                                      'kilo',
                                      'mg'},
    'voltage': {'kilovolt', 'millivolt', 'volt', 'V', 'kV', 'mV'},
    'wattage': {'kilowatt', 'watt', 'W', 'kW'},
    'item_volume': {'centilitre',
                    'cubic foot',
                    'cubic inch',
                    'cup',
                    'decilitre',
                    'fluid ounce',
                    'gallon',
                    'imperial gallon',
                    'litre',
                    'microlitre',
                    'millilitre',
                    'pint',
                    'quart',
                    'ft',
                    'cm3',
                    'ft3',
                    'L',
                    'mL'}
}

allowed_units = {
    unit for entity in entity_unit_map for unit in entity_unit_map[entity]}
