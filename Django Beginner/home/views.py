from django.shortcuts import render
from django.http import HttpResponse


json = """
[
  {
    "id": "110579",
    "url": "https://product-images.ibotta.com/offer/dUxYcQPeq391-DiywFZF8g-normal.png",
    "name": "Scotch-Brite® Scrub Dots Non-Scratch Scrub Sponges",
    "description": "Any variety - 2 ct. pack or larger",
    "terms": "Rebate valid on Scotch-Brite® Scrub Dots Non-Scratch Scrub Sponges for any variety, 2 ct. pack or larger.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "110580",
    "url": "https://product-images.ibotta.com/offer/OS0MnVcHXe7snozDC7nIiw-normal.png",
    "name": "Scotch-Brite® Scrub Dots Heavy Duty Scrub Sponges",
    "description": "Any variety - 2 ct. pack or larger",
    "terms": "Rebate valid on Scotch-Brite® Scrub Dots Heavy Duty Scrub Sponges for any variety, 2 ct. pack or larger.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "112726",
    "url": "https://product-images.ibotta.com/offer/BhGZKpjhRyqKBkPPIbjCbg-normal.png",
    "name": "Girl Scout Cookie™ Inspired Baking Mix",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on Girl Scout Cookie™ Inspired Baking Mix for any variety, any size.",
    "current_value": "$0.50 Cash Back"
  },
  {
    "id": "114163",
    "url": "https://product-images.ibotta.com/offer/YJbCsEcQvxNXzV3rQL1O2g-normal.png",
    "name": "Dove Men+Care Antiperspirant Deodorant Stick",
    "description": "Select varieties - 2.7 oz. stick",
    "terms": "Rebate valid on Dove Men+Care Antiperspirant Deodorant Stick for select varieties, 2.7 oz. stick. Rebate valid on the following varieties only:\r\n\r\n• Dove Men+Care Invisible\r\n• Dove Men+Care Invisible Fresh",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "110582",
    "url": "https://product-images.ibotta.com/offer/2NNlZie6ReiDo91k2TX6KQ-normal.png",
    "name": "Scotch-Brite® Scrub Dots Heavy Duty Dishwand",
    "description": "Heavy Duty variety only - 1 ct. pack",
    "terms": "Rebate valid on Scotch-Brite® Scrub Dots Dishwand for Heavy Duty variety only, 1 ct. pack.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "110581",
    "url": "https://product-images.ibotta.com/offer/QrsVNeBv_MI8_05GindVfQ-normal.png",
    "name": "Scotch-Brite® Scrub Dots Non-Scratch Dishwand",
    "description": "Non-Scratch variety only - 1 ct. pack",
    "terms": "Rebate valid on Scotch-Brite® Scrub Dots Dishwand for Non-Scratch variety only, 1 ct. pack.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "113018",
    "url": "https://product-images.ibotta.com/offer/mG_beej_CBbhSj0IUkBs7A-normal.png",
    "name": "Apple Cinnamon Toast Crunch™",
    "description": "11.1 oz. box or larger",
    "terms": "Rebate valid on Apple Cinnamon Toast Crunch™, 11.1 oz. box or larger.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "110442",
    "url": "https://product-images.ibotta.com/offer/oaOAOJle4RxCxVzPe06FsQ-normal.png",
    "name": "Sunsweet® Ones™",
    "description": "Any variety - 6 oz. pack or larger",
    "terms": "Rebate valid on Sunsweet® Ones™ for any variety, 6 oz. pack or larger.",
    "current_value": "$1.50 Cash Back"
  },
  {
    "id": "114198",
    "url": "https://product-images.ibotta.com/offer/t4WOEGRM2ngwEfY-srGI3A-normal.png",
    "name": "OREO Big Crunch Chocolate Candy Bars",
    "description": "Any variety - 10.5 oz.",
    "terms": "Rebate valid on OREO Big Crunch Chocolate Candy Bars, 10.5 oz. size only. \r\n\r\nThis rebate may not be combined with any other offer.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "116532",
    "url": "https://product-images.ibotta.com/offer/Pno2c24GGkaxAuij7L1pjA-normal.png",
    "name": "Stage 1 Gerber® Good Start® Formula",
    "description": "Any variety - 23.2 oz. container or larger.",
    "terms": "Rebate valid on Stage 1 Gerber® Good Start® Formula for any variety, 23.2 oz. container or larger.",
    "current_value": "$6.00 Cash Back"
  },
  {
    "id": "114456",
    "url": "https://product-images.ibotta.com/offer/_CKP6c-fiGkzA_U5kI7J2A-normal.png",
    "name": "Energizer MAX® Batteries",
    "description": "Any MAX variety - Any size",
    "terms": "Rebate valid on Energizer MAX® Batteries for any MAX variety, any size.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "105747",
    "url": "https://product-images.ibotta.com/offer/BlqQzZLiPjhN0cMtGDfYBA-normal.png",
    "name": "OREO® Ice Cream Cake",
    "description": "OREO® Ice Cream Cake, 46 oz. only",
    "terms": "Rebate valid on OREO® Ice Cream Cake, 46 oz. only.",
    "current_value": "$2.75 Cash Back"
  },
  {
    "id": "106077",
    "url": "https://product-images.ibotta.com/offer/uGpPnkGLD8Ov-o5scVFDKg-normal.png",
    "name": "French's® Mustard",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on French's® Mustard for any variety, any size.",
    "current_value": "$0.50 Cash Back"
  },
  {
    "id": "105671",
    "url": "https://product-images.ibotta.com/offer/QdgKEWr6twMUsRQOTnRNWA-normal.png",
    "name": "1915 Organic™ Juice",
    "description": "Any variety - 12 oz. size",
    "terms": "Rebate valid on 1915 Organic™ Juice for any variety, 12 oz. size.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "112688",
    "url": "https://product-images.ibotta.com/offer/hrkvOFJ0likJuz9pOgcBAg-normal.png",
    "name": "Palmolive® Ultra Dish Soap",
    "description": "Palmolive® Ultra Strength™ & Antibacterial varieties - 68.5 oz. bottle only",
    "terms": "Rebate valid on Palmolive® Ultra Strength™ & Antibacterial varieties, 68.5 oz. bottle only.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "116306",
    "url": "https://product-images.ibotta.com/offer/gspx1SQMAOdIyZ0Rq4hKrQ-normal.png",
    "name": "Playtex® Tampons",
    "description": "Select varieties - 18 ct. pack or larger. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on Playtex® Tampons for select varieties, 18 ct. pack or larger. Rebate includes the following:\r\n\r\n•Playtex® Sport® Compact 18 ct. pack & 36 ct. pack\r\n•Playtex® Sport 36 ct. pack & 50 ct. pack\r\n•Playtex® Gentle Glide® 36 ct. pack & 50 ct. pack",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "104182",
    "url": "https://product-images.ibotta.com/offer/-74YvDYiZjy21JpiZnRsyg-normal.png",
    "name": "Rubbermaid® BRILLIANCE™",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on Rubbermaid® BRILLIANCE™ for any variety, any size.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "116626",
    "url": "https://product-images.ibotta.com/offer/FR2FfUR92fZ0RjYwEX3ssA-normal.png",
    "name": "Crest® Scope® Mouthwash",
    "description": "Any variety - 500 ml. bottle or larger",
    "terms": "Rebate valid on Crest® Scope® Mouthwash for any variety, 500 ml. bottle or larger.",
    "current_value": "$0.50 Cash Back"
  },
  {
    "id": "112847",
    "url": "https://product-images.ibotta.com/offer/XQGOksDoQMCgy25LvLDmqw-normal.png",
    "name": "Martha White® Baking Mixes",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on Martha White® Baking Mixes for any variety, any size.",
    "current_value": "$0.25 Cash Back"
  },
  {
    "id": "114162",
    "url": "https://product-images.ibotta.com/offer/fjC2ZcQBjCl3Jh0A1c6Uzw-normal.png",
    "name": "Dove Men+Care Antiperspirant Deodorant Dry Spray",
    "description": "Select varieties - 3.8 oz. can",
    "terms": "Rebate valid on Dove Men+Care Antiperspirant Deodorant Dry Spray for select varieties, 3.8 oz. can. Rebate valid on the following varieties only:\r\n\r\n• Dove Men+Care Invisible\r\n• Dove Men+Care Invisible Fresh",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "110441",
    "url": "https://product-images.ibotta.com/offer/H3FElAZmyzlJ1e71AneyWA-normal.png",
    "name": "Sunsweet® D’Noir™ Prunes",
    "description": "Any variety - 7 oz. bag or larger",
    "terms": "Rebate valid on Sunsweet® D’Noir™ Prunes for any variety, 7 oz. bag or larger.",
    "current_value": "$1.25 Cash Back"
  },
  {
    "id": "112931",
    "url": "https://product-images.ibotta.com/offer/87u9ROine3V1lG-EY8TNDA-normal.png",
    "name": "Purex® Crystals™",
    "description": "Any variety - 18 oz. bottle only",
    "terms": "Rebate valid on Purex® Crystals™ for any variety, 18 oz. bottle only. Rebate includes the following varieties:\r\n\r\n•Purex® Crystals™ Fresh Spring Waters\r\n•Purex® Crystals™ Lavender Blossom\r\n•Purex® Crystals™ Fresh Mountain Breeze\r\n•Purex® Crystals™ Fabulously Fresh\r\n•Purex® Crystals™ Oh So Chic\r\n•Purex® Crystals™ Aromatherapy Well Being\r\n•Purex® Crystals™ Aromatherapy Serenity\r\n•Purex® Crystals™ Aromatherapy Tahitian Breeze\r\n•Purex® Crystals™ Cherry Blossom & Ginger \r\n•Purex® Crystals™ Warm Sandalwood & Vanilla",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "106101",
    "url": "https://product-images.ibotta.com/offer/PiDOQ-4OrXjJVowuNtucKg-normal.png",
    "name": "French's™ Crispy Jalapeños",
    "description": "5 oz. package",
    "terms": "Rebate valid on French's™ Crispy Jalapeños, 5 oz. package.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "116533",
    "url": "https://product-images.ibotta.com/offer/FvSF0gPkik0MenSATuffnw-normal.png",
    "name": "Gerber® Good Start® Soothe®",
    "description": "Any variety - 22.2 oz. or larger",
    "terms": "Rebate valid on Gerber® Good Start® Soothe® for any variety, 22.2 oz. or larger.",
    "current_value": "$6.25 Cash Back"
  },
  {
    "id": "116627",
    "url": "https://product-images.ibotta.com/offer/w5Lh5XG1pOH6__k-59aG3g-normal.png",
    "name": "Crest® Mouthwash",
    "description": "Any variety - 473 ml. bottle or larger. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on Crest® Mouthwash for any variety, 473 ml. bottle or larger. Rebate excludes the following varieties:\r\n\r\n• Crest® Scope® Mouthwash",
    "current_value": "$0.50 Cash Back"
  },
  {
    "id": "108640",
    "url": "https://product-images.ibotta.com/offer/XOhlb6L0OSWXto6TtzZodQ-normal.png",
    "name": "Del Monte® Fruit Refreshers™",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on Del Monte® Fruit Refreshers™ for any variety, any size.",
    "current_value": "$0.50 Cash Back"
  },
  {
    "id": "106427",
    "url": "https://product-images.ibotta.com/offer/jS9MQ_iwoRw7St__Qq-7yA-normal.png",
    "name": "Playtex Baby™ Products",
    "description": "Any Baby Bottles or Playtex® Sipsters® variety - 3 ct. pack bottles or 2 ct. pack cups only",
    "terms": "Rebate valid on Playtex Baby™ Products for any Baby Bottles or Playtex® Sipsters® variety, 3 ct. pack bottles or 2 ct. pack cups only.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "115890",
    "url": "https://product-images.ibotta.com/offer/14AaHUDh6ZS7GGHcskBC5A-normal.png",
    "name": "L’Oréal Paris® Eyeliner, Eye Shadow or Brow Products",
    "description": "Any variety - Any size. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on L’Oréal Paris® Eyeliner, Eye Shadow or Brow Products for any variety, any size.\r\n\r\nRebate not valid on L’Oréal Paris® Mascaras.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "119070",
    "url": "https://product-images.ibotta.com/offer/DtKyQjrk-Iz5vk388QRUyA-normal.png",
    "name": "Energizer® Ultimate Lithium™ Batteries",
    "description": "Any Ultimate Lithium variety - Any size",
    "terms": "Rebate valid on Energizer® Ultimate Lithium™ Batteries for any Ultimate Lithium variety, any size.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "114177",
    "url": "https://product-images.ibotta.com/offer/DD3az4ZHTRRdWWwoST0x3Q-normal.png",
    "name": "Zout® Stain Remover",
    "description": "12 fl. oz or larger",
    "terms": "Rebate valid on Zout® Stain Remover, 12 fl. oz or larger.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "111371",
    "url": "https://product-images.ibotta.com/offer/PGt4U7ThHm3Wn5qu9PeKpA-normal.png",
    "name": "ScarAway® Silicone Scar Sheets",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on ScarAway® Silicone Scar Sheets for any variety, any size.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "116370",
    "url": "https://product-images.ibotta.com/offer/p6dvbWzybWxrbzVbRgCZbw-normal.png",
    "name": "Seventh Generation™ Natural Liquid Laundry Detergent",
    "description": "Any variety - 100 oz. bottles",
    "terms": "Rebate valid on Seventh Generation™ Natural Liquid Laundry Detergent for any variety, 100 oz. bottles.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "116372",
    "url": "https://product-images.ibotta.com/offer/Sc81a8oVc3iSpjELgZkV_Q-normal.png",
    "name": "Seventh Generation™ Hand Wash",
    "description": "Buy 2 - Any variety - Select Sizes. See rebate details.",
    "terms": "Rebate valid on Seventh Generation™ Hand Wash. Buy 2 of any variety, select sizes. Rebate valid on the following sizes:\r\n\r\n• 32 oz. bottles\r\n• 12 oz. bottles\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.\r\n\r\nMulti-packs will only be counted as one (1) product toward the Buy 2 requirement.",
    "current_value": "$1.50 Cash Back"
  },
  {
    "id": "111348",
    "url": "https://product-images.ibotta.com/offer/Equrp2Y-cQZtl4F2d4eHPQ-normal.png",
    "name": "AXE & DENIZEN® from Levi's® Men's Jeans Combo",
    "description": "Combo rebate. See rebate details.",
    "terms": "• Product 1: AXE - Any variety - Any size - Rebate excludes travel and trial sizes.\r\n\r\n• Product 2: DENIZEN® from Levi's® Men's Jeans - Any variety - Any size\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$5.00 Cash Back"
  },
  {
    "id": "116002",
    "url": "https://product-images.ibotta.com/offer/3m7sBXqG81OZyXCCVekdJg-normal.png",
    "name": "Pabst Blue Ribbon® Beer & Totino's™ Crisp Party Pizza™ OR Pizza Rolls™ Hot Snacks Combo",
    "description": "Combo rebate. See rebate details.",
    "terms": "• Product 1: Pabst Blue Ribbon® Beer - 12 pack or larger\r\n\r\n• Product 2: Totino's™ Crisp Party Pizza™ OR Pizza Rolls™ Hot Snacks - Buy 3 - Any variety - Any size\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$4.00 Cash Back"
  },
  {
    "id": "116531",
    "url": "https://product-images.ibotta.com/offer/2c5lzZKU2YaWXUHU8vlJgA-normal.png",
    "name": "Stage 3 Gerber® Good Start® Toddler Drink",
    "description": "Any variety - 24 oz. container only",
    "terms": "Rebate valid on Stage 3 Gerber® Good Start® Toddler Drink for any variety, 24 oz. container only.",
    "current_value": "$5.00 Cash Back"
  },
  {
    "id": "113849",
    "url": "https://product-images.ibotta.com/offer/fTb7mXFjPoWHaiG-V463kA-normal.png",
    "name": "Neutrogena® Makeup Remover Towelettes",
    "description": "Any variety - Select Sizes. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on Neutrogena® Makeup Remover Towelettes for any variety, select sizes. \r\n\r\nRebate not valid on trial/travel sized products, clearance, or cosmetic products.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "108099",
    "url": "https://product-images.ibotta.com/offer/BxzEgi07INdLsZGycbrfOQ-normal.png",
    "name": "smartwater® sparkling",
    "description": "smartwater® sparkling variety - 1 L bottle only",
    "terms": "Rebate valid on smartwater® sparkling variety, 1 L bottle only.",
    "current_value": "$0.85 Cash Back"
  },
  {
    "id": "105294",
    "url": "https://product-images.ibotta.com/offer/WAuukfA0pl4gll0guR4isg-normal.png",
    "name": "RiceSelect®",
    "description": "Any variety - 21 oz. jar or larger",
    "terms": "Rebate valid on RiceSelect® for any variety, 21 oz. jar or larger.",
    "current_value": "$1.25 Cash Back"
  },
  {
    "id": "116310",
    "url": "https://product-images.ibotta.com/offer/uOMMWKqV2YgQhw7Jgg2RxQ-normal.png",
    "name": "Special K® Protein Bites and Bars",
    "description": "Any variety - 6 oz. bag and 6 ct. or 12 ct. box",
    "terms": "Rebate valid on Special K® Protein Bites and Bars for any variety, 6 oz. bag and 6 ct. or 12 ct. box.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "114837",
    "url": "https://product-images.ibotta.com/offer/RdgUnXMR6gGYT8KypfQnbw-normal.png",
    "name": "Affresh® Washer Cleaner",
    "description": "Washer variety - 6 ct. box only",
    "terms": "Rebate valid on Affresh® Washer Cleaner for Washer variety, 6 ct. box only.",
    "current_value": "$1.50 Cash Back"
  },
  {
    "id": "112485",
    "url": "https://product-images.ibotta.com/offer/TsonrAjrQeYZT3b4b-6uNQ-normal.png",
    "name": "Sargento® Ultra Thin® Cheese Slices",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on Sargento® Ultra Thin® Cheese Slices for any variety, any size.",
    "current_value": "$0.25 Cash Back"
  },
  {
    "id": "95682",
    "url": "https://product-images.ibotta.com/offer/ZSpRIQd1m4Xi2slUm73_0A-normal.png",
    "name": "FUTURO™ Reversible Splint Wrist Brace Black, Adjustable",
    "description": "Any variety - 1 ct. pack only",
    "terms": "Rebate valid on FUTURO™ Reversible Splint Wrist Brace Black, Adjustable for any variety, 1 ct. pack only.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "106057",
    "url": "https://product-images.ibotta.com/offer/brok6C4Dtl0CsMh9tTZWFQ-normal.png",
    "name": "Ensueño® Fabric Softener",
    "description": "Any variety - 45 fl. oz. bottle",
    "terms": "Rebate valid on Ensueño® Fabric Softener for any variety, 45 fl. oz. bottle.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "115983",
    "url": "https://product-images.ibotta.com/offer/0g9ZrMGYX1DC-QoAOOUpUw-normal.png",
    "name": "SUPERPRETZEL® Soft Pretzels",
    "description": "Any variety - Any size. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on SUPERPRETZEL® Soft Pretzels for any variety, any size. Rebate excludes the following varieties:\r\n\r\n• Stand Up Bags (7oz. - 9oz.)",
    "current_value": "$0.50 Cash Back"
  },
  {
    "id": "116530",
    "url": "https://product-images.ibotta.com/offer/SZipraRW7Wy8P1Q5QmgEKw-normal.png",
    "name": "Stage 2 Gerber® Good Start® Formula",
    "description": "Any variety - 26.6 or 27.8 oz. container only",
    "terms": "Rebate valid on Stage 2 Gerber® Good Start® Formula for any variety, 26.6 or 27.8 oz. container only.",
    "current_value": "$5.00 Cash Back"
  },
  {
    "id": "103560",
    "url": "https://product-images.ibotta.com/offer/rLaB7MnlxDGfQl9VuenQPA-normal.png",
    "name": "Advil® Liqui-Gels®",
    "description": "Any variety - 80 ct. or larger",
    "terms": "Rebate valid on Advil® Liqui-Gels®, including new Advil® Liqui-Gels® minis, for any variety 80 ct. or larger.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "107060",
    "url": "https://product-images.ibotta.com/offer/MmtefP6Ng_qynWbZxvzcXA-normal.png",
    "name": "Kleenex® Bundle Packs",
    "description": "Any variety - 2 pack or larger. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on Kleenex® Bundle Packs for any variety, 2 pack or larger. Rebate excludes trial and travel sizes.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "114861",
    "url": "https://product-images.ibotta.com/offer/1wCHoi6RJMfpZfKTPzV59w-normal.png",
    "name": "L’Oréal Paris® Infallible Paints Eyeliner or Eye Shadow Products",
    "description": "Infallible Paints variety only.",
    "terms": "Rebate valid on L’Oréal Paris® Infallible Paints Eyeliner or Eye Shadow Products only.\r\n\r\nRebate does not include other L’Oréal Paris® Eye Products.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "114194",
    "url": "https://product-images.ibotta.com/offer/kuyDHIjM0WMMgKuoVujz2Q-normal.png",
    "name": "Ortega® Good Grains Blue Corn Taco Shells",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on Ortega® Good Grains Blue Corn Taco Shells, any size.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "119336",
    "url": "https://product-images.ibotta.com/offer/T_1sl88BDiSYPYIuasYd5g-normal.png",
    "name": "Miller Lite OR Coors Light and Any Deli Chicken",
    "description": "Combo rebate. See rebate details",
    "terms": "• Product 1: (1) ONE 15-pack of Miller Lite OR Coors Light\r\n\r\n• Product 2: Any Deli Chicken*\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$6.00 Cash Back"
  },
  {
    "id": "119337",
    "url": "https://product-images.ibotta.com/offer/NXm4sLSBv1PrwTbAxJEJPw-normal.png",
    "name": "Any Deli Chicken",
    "description": "Select varieties - Select sizes",
    "terms": "Rebate valid on Any Deli Chicken for select varieties, select sizes. \r\n\r\nSelect varieties include:\r\n•  8 pc mixed (fried or baked)\r\n• 10 pc Dark (fried or baked)\r\n• 1 Rotisserie Chicken\r\n• 1 lb. of chicken wings/tenders.",
    "current_value": "$5.00 Cash Back"
  },
  {
    "id": "108471",
    "url": "https://product-images.ibotta.com/offer/hhgKkcwx94r-ywQcHcPyvg-normal.png",
    "name": "Michelob Ultra®",
    "description": "12-pack of cans or bottles",
    "terms": "Earn a $3.00 rebate on the purchase of one (1) Michelob ULTRA® 12-pack (cans or bottles).",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "118190",
    "url": "https://product-images.ibotta.com/offer/unPF5SOOf5OOAVz222NVwQ-normal.png",
    "name": "Shock Top® AND Fruit Combo",
    "description": "Combo rebate. See rebate details.",
    "terms": "Earn a $3.00 rebate on your purchase of one (1) Shock Top® Family 6-pack or larger (cans or bottles) AND Oranges, Grapefruits, Lemons, Pumpkins or any fruit*.*Purchase price of Oranges, Grapefruits, Lemons, Pumpkins, or any fruit must exceed $3.00, excluding sales tax. Both products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "117756",
    "url": "https://product-images.ibotta.com/offer/3rY7BleYfo3WHGgiJayX0g-normal.png",
    "name": "Goose Island® WITH Fresh or Frozen Meat, Seafood, BBQ Sauces, Rubs, Marinades OR Seasonings Combo",
    "description": "Combo Rebate. See rebate details.",
    "terms": "Earn a $3.00 rebate on the purchase of one (1) Goose Island® Family 6-pack or larger (cans or bottles) with the purchase of Fresh or Frozen Meat, Seafood, BBQ Sauces, Rubs, Marinades or Seasonings.* *Purchase price of Meat, Seafood, BBQ Sauces, Rubs, Marinades or Seasonings must exceed $3.00, excluding sales tax. All items must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "120331",
    "url": null,
    "name": "Carapelli® Olive Oil",
    "description": "Any variety - Any size",
    "terms": "Rebate on Carapelli® Olive Oil for any variety, any size.",
    "current_value": "$1.50 Cash Back"
  },
  {
    "id": "121252",
    "url": "https://product-images.ibotta.com/offer/03bQor3WfYeeVMVsXSwWew-normal.png",
    "name": "Peroni",
    "description": "12-pack - 12 oz. bottles or cans",
    "terms": "Rebate valid on ONE (1) 12-pack of Peroni for any variety, 12 oz. bottles or cans.",
    "current_value": "$4.00 Cash Back"
  },
  {
    "id": "121253",
    "url": "https://product-images.ibotta.com/offer/sguUM4MPuJ0fBCirCay4GQ-normal.png",
    "name": "Peroni",
    "description": "12-pack - 12 oz. bottles or cans",
    "terms": "Rebate valid on ONE (1) 12-pack of Peroni for any variety, 12 oz. bottles or cans.",
    "current_value": "$4.00 Cash Back"
  },
  {
    "id": "118822",
    "url": "https://product-images.ibotta.com/offer/WqhWM4IPi8UORU4MRbiUbQ-normal.png",
    "name": "L’Oréal Paris® Excellence Hair Color",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on L’Oréal Paris® Excellence Hair Color for any variety, any size.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "118824",
    "url": "https://product-images.ibotta.com/offer/sm5kORbo-pZWsus9TY9pGA-normal.png",
    "name": "L’Oréal Paris® Superior Preference Hair Color",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on L’Oréal Paris® Superior Preference Hair Color for any variety, any size.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "119325",
    "url": "https://product-images.ibotta.com/offer/IEbbghRFyRSy1hNjMaR5bw-normal.png",
    "name": "L’Oréal Paris® Magic Root Cover Up Temporary Gray Concealer Spray",
    "description": "Any variety - 1 ct. pack only",
    "terms": "Rebate valid on L’Oréal Paris® Magic Root Cover Up Temporary Gray Concealer Spray for any variety, 1 ct. pack only.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "119534",
    "url": "https://product-images.ibotta.com/offer/TAspYjvDDpF153ZgFeGkNQ-normal.png",
    "name": "Any Item",
    "description": "Submit Any Grocery Receipt",
    "terms": "Rebate valid on the submission of any grocery receipt. Simply tap the Redeem button in the navigation bar after unlocking and follow the instructions.",
    "current_value": "$0.25 Cash Back"
  },
  {
    "id": "120330",
    "url": null,
    "name": "Carapelli® Olive Oil",
    "description": "Any variety - Any size",
    "terms": "Rebate on Carapelli® Olive Oil for any variety, any size.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "116630",
    "url": "https://product-images.ibotta.com/offer/kw9RY8oS4ItiU0djAo95hQ-normal.png",
    "name": "Budweiser® or Bud Light®",
    "description": "12-pack or larger of cans or bottles",
    "terms": "Earn a $2.00 rebate on your purchase of one (1) 12-pack or larger of Budweiser® or Bud Light®.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "102756",
    "url": "https://product-images.ibotta.com/offer/_hjLqbkM0V44JuLGaGCOmg-normal.png",
    "name": "Smucker's® Fruit & Honey™ Fruit Spread",
    "description": "Any variety - 9 oz. jar",
    "terms": "Rebate valid on Smucker's® Fruit & Honey™ Fruit Spread for any variety, 9 oz. jar.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "113155",
    "url": "https://product-images.ibotta.com/offer/BXcbBUTZTnZEyqWHmIII5w-normal.png",
    "name": "SMITHWICK’S Ale",
    "description": "12-pack only",
    "terms": "Valid off ONE (1) 12-pack of SMITHWICK’S Ale.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "119414",
    "url": "https://product-images.ibotta.com/offer/wsTHkHaQ9rum2KPwIVYcSQ-normal.png",
    "name": "Mederma® Scar Cream plus SPF 30",
    "description": "Select varieties - Select sizes",
    "terms": "Rebate valid on Mederma® Scar Cream plus SPF 30 for select varieties, select sizes. \r\n\r\n• Mederma® Scar Cream + SPF 30, 20 gram tube only \r\n• Mederma® PM, 1 oz. tube only",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "119463",
    "url": "https://product-images.ibotta.com/offer/zPMfE4GotezFERiw0iU3LQ-normal.png",
    "name": "Neutrogena® Cosmetics Face Products",
    "description": "Any variety - Select sizes. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on Neutrogena® Cosmetics Face Products for any variety, select sizes. Rebate excludes the following varieties:\r\n\r\n•Neutrogena® trial/travel sized products\r\n•Neutrogena® clearance products\r\n•Neutrogena® face lotions or face wipes",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "117134",
    "url": "https://product-images.ibotta.com/offer/0kjTqb0eXhrBz4z9GeVgVQ-normal.png",
    "name": "Ready Pac Foods® Bistro Bowls®",
    "description": "Buy 2 - Any variety - Any size",
    "terms": "Rebate valid on Ready Pac Foods® Bistro Bowls®. Buy 2 of any variety, any size.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "112491",
    "url": "https://product-images.ibotta.com/offer/012BGR49DRw7Iut4LDQe1A-normal.png",
    "name": "REDD'S® Apple Ale",
    "description": "12-pack - 12 oz. bottles or cans",
    "terms": "Rebate valid on ONE (1) 12-pack of REDD'S® Apple Ale for select varieties, 12 oz. bottles or cans.\r\n\r\nRebate excludes select varieties:\r\n• REDDS® Wicked Apple\r\n• REDDS® Wicked Black Cherry\r\n• REDDS® Wicked Mango\r\n• REDDS® Wicked Strawberry Kiwi\r\n• REDDS® Wicked Blood Orange",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "116853",
    "url": "https://product-images.ibotta.com/offer/VZQDEUmQ52rmmn2pCD3Kug-normal.png",
    "name": "Cayman Jack®",
    "description": "Any variety - 12 pack of 11.2 oz. bottles",
    "terms": "Rebate valid on Cayman Jack® for any variety, 12 pack of 11.2 oz. bottles.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "116899",
    "url": "https://product-images.ibotta.com/offer/VZQDEUmQ52rmmn2pCD3Kug-normal.png",
    "name": "SUPERUSER TEST",
    "description": "Any variety - 12 pack of 11.2 oz. bottles",
    "terms": "Rebate valid on Cayman Jack® Margarita for any variety, 12 pack of 11.2 oz. bottles.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "119413",
    "url": "https://product-images.ibotta.com/offer/FssTmHLt1UkA3OsmJ4PDSw-normal.png",
    "name": "Mederma® Advanced Scar Gel",
    "description": "Mederma® Advanced Scar Gel - Any size",
    "terms": "Rebate valid on Mederma® Advanced Scar Gel, any size.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "119421",
    "url": "https://product-images.ibotta.com/offer/0e87W-rl8rhekpweSRzpaA-normal.png",
    "name": "Mederma® Quick Dry Oil",
    "description": "Mederma® Quick Dry Oil - 100 ml bottle only",
    "terms": "Rebate valid on Mederma® Quick Dry Oil, 100 ml bottle only.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "119039",
    "url": "https://product-images.ibotta.com/offer/rBEHo-cZMJtZCv8EiGVLtg-normal.png",
    "name": "The Original Donut Shop® Coffee K-Cup® Pod",
    "description": "Any variety - 12 ct. pack or larger",
    "terms": "Rebate valid on Keurig® The Original Donut Shop® Coffee K-Cup® Pod for any variety, 12 ct. pack or larger.",
    "current_value": "$0.50 Cash Back"
  },
  {
    "id": "117135",
    "url": "https://product-images.ibotta.com/offer/tK0u6P-Q1pgpUvOquTsuyA-normal.png",
    "name": "Ready Pac Foods® elevAte™ Salads",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on Ready Pac Foods® elevAte™ Salads for any variety, any size.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "116208",
    "url": "https://product-images.ibotta.com/offer/XpGa4d0zGCmZc5h5Dp9sng-normal.png",
    "name": "Budweiser® or Bud Light®",
    "description": "18-pack or larger, cans or bottles",
    "terms": "Earn a $3.00 rebate on your purchase of one (1) Budweiser® or Bud Light® 18-pack or larger (cans or bottles).",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "112685",
    "url": "https://product-images.ibotta.com/offer/QdgKEWr6twMUsRQOTnRNWA-normal.png",
    "name": "1915 Organic™ Juice",
    "description": "Any variety - 12 oz. size",
    "terms": "Rebate valid on 1915 Organic™ Juice for any variety, 12 oz. size.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "114233",
    "url": "https://product-images.ibotta.com/offer/6r3UUCp3_uOhFKux7o9-EQ-normal.png",
    "name": "Werther's® Original® Harvest Caramels",
    "description": "Select Varieties - Select sizes.",
    "terms": "Rebate valid on Werther's® Original® Harvest Caramels for select varieties, select sizes. Rebate valid on the following varieties/sizes only:\r\n\r\n• Werther's® Original® Pumpkin Spice Soft Caramels, 9.4 oz. bag\r\n• Werther's® Original® Caramel Apple Soft Caramels, 9.4 oz. bag",
    "current_value": "$1.25 Cash Back"
  },
  {
    "id": "111964",
    "url": "https://product-images.ibotta.com/offer/E9nCSJIE3S59Gdyk7sLuHQ-normal.png",
    "name": "Blue Bunny® Ice Cream",
    "description": "Buy 2 - Any variety - 46/48 oz. only",
    "terms": "Rebate valid on Blue Bunny® Ice Cream. Buy 2 of any variety, 46/48 oz. only.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "116900",
    "url": "https://product-images.ibotta.com/offer/rKz3OveQahWKljV8ZsSD6g-normal.png",
    "name": "L’Oréal Paris® Advanced Hairstyle",
    "description": "Any variety - Select sizes. Exclusions apply.",
    "terms": "Rebate valid on L’Oréal Paris® Advanced Hairstyle for any variety, select sizes. \r\n\r\nRebate not valid on trial sizes.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "114512",
    "url": "https://product-images.ibotta.com/offer/UPsE5SQpPU_8ocr_AcIzyw-normal.png",
    "name": "New York Strip Steak - Any Brand",
    "description": "16 oz. or larger",
    "terms": "Rebate valid on Any Brand New York Strip Steak, 16 oz. or larger.",
    "current_value": "$2.50 Cash Back"
  },
  {
    "id": "118803",
    "url": "https://product-images.ibotta.com/offer/0kjTqb0eXhrBz4z9GeVgVQ-normal.png",
    "name": "Ready Pac Foods® Bistro Bowls®",
    "description": "Buy 2 - Any variety - Any size",
    "terms": "Rebate valid on Ready Pac Foods® Bistro Bowls®. Buy 2 of any variety, any size.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$0.25 Cash Back"
  },
  {
    "id": "118801",
    "url": "https://product-images.ibotta.com/offer/tK0u6P-Q1pgpUvOquTsuyA-normal.png",
    "name": "Ready Pac Foods® elevAte™ Salads",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on Ready Pac Foods® elevAte™ Salads for any variety, any size.",
    "current_value": "$0.25 Cash Back"
  },
  {
    "id": "118542",
    "url": "https://product-images.ibotta.com/offer/geu7nysmVRaMvBZpnM5Ctg-normal.png",
    "name": "noosa® yoghurt",
    "description": "Any size - mates™ variety",
    "terms": "Rebate valid on noosa® yoghurt for any size, mates™ variety.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "115159",
    "url": "https://product-images.ibotta.com/offer/WWOXLzmldn8pd22CBRovHQ-normal.png",
    "name": "Ommegang Three Philosophers",
    "description": "750ml bottle or 4pk bottle",
    "terms": "Rebate valid on Ommegang Three Philosophers, 750ml bottle or 4pk bottle.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "116851",
    "url": "https://product-images.ibotta.com/offer/DTfvHGdtpcaew1nBQ0eoPQ-normal.png",
    "name": "Cayman Jack®",
    "description": "Any variety - 6 pack of 11.2 oz. bottles",
    "terms": "Rebate valid on Cayman Jack® for any variety, 6 pack of 11.2 oz. bottles.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "118608",
    "url": "https://product-images.ibotta.com/offer/OE0IWDc3r7IfxDm8eQdN-Q-normal.png",
    "name": "Always® Radiant or Infinity Pads",
    "description": "Buy 2 - Any variety - 11 ct. pack or larger",
    "terms": "Rebate valid on Always® Radiant or Infinity Pads. Buy 2 of any variety, 11 ct. pack or larger.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "119464",
    "url": "https://product-images.ibotta.com/offer/ZMmf-799AwNxgKxC4A3v4g-normal.png",
    "name": "Neutrogena® Cosmetics Lip or Eye Products",
    "description": "Any variety - Select sizes. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on Neutrogena® Cosmetics Lip or Eye Products for any variety, select sizes. Rebate excludes the following varieties:\r\n\r\n•Neutrogena® trial/travel sized products\r\n•Neutrogena® clearance products\r\n•Neutrogena® eye makeup remover",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "121246",
    "url": "https://product-images.ibotta.com/offer/WWR3Df-caT0wkYruCbd2sg-normal.png",
    "name": "Peroni",
    "description": "6-pack - 12 oz. bottles or cans",
    "terms": "Rebate valid on ONE (1) 6-pack of Peroni for any variety, 12 oz. bottles or cans.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "121250",
    "url": "https://product-images.ibotta.com/offer/WWR3Df-caT0wkYruCbd2sg-normal.png",
    "name": "Peroni",
    "description": "6-pack - 12 oz. bottles or cans",
    "terms": "Rebate valid on ONE (1) 6-pack of Peroni for any variety, 12 oz. bottles or cans.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "113156",
    "url": "https://product-images.ibotta.com/offer/KWBFclY_KooKxuiWkOs50Q-normal.png",
    "name": "SMITHWICK’S Ale",
    "description": "6-pack only",
    "terms": "Valid off ONE (1) 6-pack of SMITHWICK’S Ale.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "115163",
    "url": "https://product-images.ibotta.com/offer/-GrQLI1mfHcSMDNjo5Wh7g-normal.png",
    "name": "New Belgium®",
    "description": "Any variety - 12 pack or larger of 12 oz. bottles or cans only. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on New Belgium® for any variety, 12 pack or larger of 12 oz. bottles or cans only. Rebate excludes the following varieties:\r\n\r\n• New Belgium® Fat Tire",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "115203",
    "url": "https://product-images.ibotta.com/offer/t60E5QrR_0tv-jzDCiEvrA-normal.png",
    "name": "Zarbee’s® Naturals",
    "description": "Children's Multivitamin - 110 ct. bottle",
    "terms": "Rebate valid on Zarbee’s® Naturals Children's Multivitamin, 110 ct. bottle.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "118612",
    "url": "https://product-images.ibotta.com/offer/1cPwF57jvVv5UKY0nwzqsQ-normal.png",
    "name": "Tampax® Pearl or Radiant Tampons",
    "description": "Buy 2 - Any variety - 16 ct. or larger",
    "terms": "Rebate valid on Tampax® Pearl or Radiant Tampons. Buy 2 of any variety, 16 ct. or larger.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "116615",
    "url": "https://product-images.ibotta.com/offer/_qjYVgLFFeaQiw09z3oxHA-normal.png",
    "name": "Holland House® Cooking Wine",
    "description": "Any variety - 16 oz. bottle",
    "terms": "Rebate valid on Holland House® Cooking Wine for any variety, 16 oz. bottle.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "118732",
    "url": "https://product-images.ibotta.com/offer/CulmX_4iPXA7nFUl4Gs2Ww-normal.png",
    "name": "Golden Crisp®",
    "description": "Buy 2 - Any variety - Any size",
    "terms": "Rebate valid on Golden Crisp®. Buy 2 of any variety, any size.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$1.75 Cash Back"
  },
  {
    "id": "116315",
    "url": "https://product-images.ibotta.com/offer/KIRASoT3eKIqIJTZaqu1lA-normal.png",
    "name": "Tyson® Any'tizers® Snacks",
    "description": "Any variety - Any size. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on Tyson® Any'tizers® Snacks for any variety, any size. \r\n\r\nRebate excludes boxed varieties.",
    "current_value": "$1.50 Cash Back"
  },
  {
    "id": "116328",
    "url": "https://product-images.ibotta.com/offer/6k0lhdVMRAM6KKv1gEbYHw-normal.png",
    "name": "Tyson® Chicken Strips",
    "description": "Any variety - Any size. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on Tyson® Chicken Strips for any variety, any size. Rebate excludes the following varieties:\r\n\r\n• Boxed varieties \r\n• Tyson® Naturals®\r\n• Tyson® Grilled & Ready®",
    "current_value": "$1.50 Cash Back"
  },
  {
    "id": "107401",
    "url": "https://product-images.ibotta.com/offer/m3OQCza9zimX1bJ1b1b0Rw-normal.png",
    "name": "Newman's Own® Pizza",
    "description": "Any variety - Any size.",
    "terms": "Rebate valid on Newman's Own® Pizza any variety, any size.",
    "current_value": "$1.50 Cash Back"
  },
  {
    "id": "116205",
    "url": "https://product-images.ibotta.com/offer/PkugcNgzAl2dzxUl7OV8FQ-normal.png",
    "name": "Glow by Nature Made®",
    "description": "Daily Skin Hydration Supplement - All varieties. See rebate details.",
    "terms": "Rebate valid on Glow by Nature Made® for all varieties.\r\n\r\nVarieties include:\r\n• Skin Moisture\r\n• Skin Moisture + Sleep\r\n• Skin Moisture + Hair & Nails",
    "current_value": "$4.00 Cash Back"
  },
  {
    "id": "114820",
    "url": "https://product-images.ibotta.com/offer/JbiIz3f4RV3bGsdzJGK2jQ-normal.png",
    "name": "Sanford",
    "description": "Select Varieties - 750 ml. bottle only",
    "terms": "Rebate valid on Sanford for select varieties, 750 ml. bottle only. Rebate valid on the following varieties:\r\n\r\n• Chardonnay\r\n• Rosé",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "113062",
    "url": "https://product-images.ibotta.com/offer/tf_IqjUiL_F19YdPKtnUgA-normal.png",
    "name": "CLIF Kid Zbar Filled",
    "description": "Any variety - Single bar",
    "terms": "Rebate valid on CLIF Kid Zbar Filled for any variety, single bar only.",
    "current_value": "$0.25 Cash Back"
  },
  {
    "id": "114588",
    "url": "https://product-images.ibotta.com/offer/kKkaEF7TtfkiB2gdu9g3uA-normal.png",
    "name": "Jelly - Any Brand",
    "description": "Valid on Any Brand Jelly, jarred varieties only, 12 oz. or larger.",
    "terms": "Rebate excludes: \r\n• Jelly and peanut butter mixed varieties\r\n• All other mixed varieties\r\n• Multipacks",
    "current_value": "$0.25 Cash Back"
  },
  {
    "id": "116057",
    "url": "https://product-images.ibotta.com/offer/SV6XG7fTUjc4lUYeu2Opkw-normal.png",
    "name": "[ yellow tail ]® Wine",
    "description": "Select varieties - 750ml or 1.5L bottle. Exclusions apply. See rebate details.",
    "terms": "Rebate valid on [ yellow tail ]® Wine for any variety, 750ml or 1.5L bottle only. Rebate excludes [ yellow tail ]® bubbles and [ yellow tail ]® Reserve.",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "115685",
    "url": "https://product-images.ibotta.com/admin/5112015/any-brand-packaging_cereal_v2.png",
    "name": "Breakfast Cereal - Any Brand",
    "description": "Valid on Any Brand Boxed Breakfast Cereal, 11 oz. or larger.",
    "terms": "Rebate excludes:\r\n\r\n• Hot cereal varieties\r\n• Bagged cereal varieties\r\n• Cereal bar varieties\r\n• Multi-packs of any size box less than 11 oz.\r\n\r\nCereal varieties with no visible branding or visible barcode will not be accepted.",
    "current_value": "$0.25 Cash Back"
  },
  {
    "id": "117760",
    "url": "https://product-images.ibotta.com/offer/BlZUrTHnXpzp9cG221Jbyg-normal.png",
    "name": "Challenge® Butter",
    "description": "Salted or Unsalted varieties - 1 lb.",
    "terms": "Rebate valid on Challenge® Butter for any salted or unsalted varieties, 1 lb. only.",
    "current_value": "$0.50 Cash Back"
  },
  {
    "id": "115988",
    "url": "https://product-images.ibotta.com/offer/hVNtvQ-3Sic8dISDlvP7jw-normal.png",
    "name": "Cusumano",
    "description": "Any variety - 750 ml. bottle",
    "terms": "Rebate valid on Cusumano for any variety, 750 ml. bottle",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "112836",
    "url": "https://product-images.ibotta.com/offer/9ahrb9csgzT4DtnDOFOxvg-normal.png",
    "name": "CLIF Kid Zbar Filled",
    "description": "Any variety - Multipack",
    "terms": "Rebate valid on CLIF Kid Zbar Filled for any variety, multipack only.\r\n\r\nMultipacks count as a single item.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "116644",
    "url": "https://product-images.ibotta.com/offer/upHI5fmDAEnibl66lcSCew-normal.png",
    "name": "Budweiser® or Bud Light®",
    "description": "Buy 2 - 8-packs - 16 oz. Aluminum Bottle",
    "terms": "Earn a $5.00 rebate on the purchase of two (2) Budweiser® or Bud Light® 8-packs 16 oz. aluminum bottles. Both products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$5.00 Cash Back"
  },
  {
    "id": "114392",
    "url": "https://product-images.ibotta.com/offer/3_w1qx1Ho86OYWN2X_bxtg-normal.png",
    "name": "BIRRA MORETTI & Any Brand Pizza",
    "description": "Combo rebate. See rebate details.",
    "terms": "• Product 1 : BIRRA MORETTI - Select varieties, 6-pack only.\r\n\r\nSelect varieties include:\r\n• BIRRA MORETTI Lager\r\n• BIRRA MORETTI La Rossa\r\n\r\n\r\n• Product 2: Pizza - Any Brand\r\n\r\nRebate includes: \r\n• Gluten-free varieties \r\n\r\nRebate excludes: \r\n• Pizzas made in-store \r\n• Pizza bagel bites \r\n• Pizza rolls \r\n• Dairy free pizza \r\n• Garlic bread pizza \r\n• Mini-Pizza varieties \r\n• Dipping strips \r\n• Pizza pockets\r\n\r\nAll products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$4.00 Cash Back"
  },
  {
    "id": "116777",
    "url": "https://product-images.ibotta.com/offer/e3ttsc6-k-dX1iOAAQMzsQ-normal.png",
    "name": "ZICO® Chilled Coconut Water or Juice Blend",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on ZICO® Chilled Coconut Water or Juice Blend for any variety, any size.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "115070",
    "url": "https://product-images.ibotta.com/offer/GHo6b9oYozGkPIk9M3a8Hg-normal.png",
    "name": "DeKuyper®",
    "description": "Any variety - 750 ml. bottle or larger",
    "terms": "Rebate valid on DeKuyper® for any variety, 750 ml. bottle or larger.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "114399",
    "url": "https://product-images.ibotta.com/offer/Bkpaai6iVnkhVcw_yRo_Ew-normal.png",
    "name": "NEWCASTLE BROWN ALE®",
    "description": "12-pack only",
    "terms": "Rebate valid on NEWCASTLE BROWN ALE® for 12-pack only.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "116916",
    "url": "https://product-images.ibotta.com/offer/ur6SwhSEiDYTqxG13eYZyg-normal.png",
    "name": "Lindeman's",
    "description": "Select varieties - 750 ml. bottle. See rebate details.",
    "terms": "Rebate valid on Lindeman's for select varieties, 750 ml. bottle only.\r\n\r\nSelect varieties include:\r\n• Cabernet Sauvignon\r\n• Chardonnay\r\n• Chardonnay Riesling\r\n• Merlot\r\n• Pinot Noir\r\n• Sauvignon Blanc\r\n• Pinot Grigio\r\n• Moscato\r\n• Shiraz\r\n• Shiraz Cabernet Sauvignon\r\n• Cabernet Sauvignon Merlot",
    "current_value": "$1.00 Cash Back"
  },
  {
    "id": "115987",
    "url": "https://product-images.ibotta.com/offer/0Gwg2Q1e4ySHO-UxLGqSvA-normal.png",
    "name": "Federalist",
    "description": "Any variety - 750 ml. bottle",
    "terms": "Rebate valid on Federalist for any variety, 750 ml. bottle.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "116274",
    "url": "https://product-images.ibotta.com/offer/Zbj1JNPJoU3F0ogFIWP6Jw-normal.png",
    "name": "Sour Punch® Candy",
    "description": "Any variety - 4.5 oz. pack or larger",
    "terms": "Rebate valid on Sour Punch® Straws and Sour Punch® Bites for any variety, 4.5 oz. pack or larger.",
    "current_value": "$0.50 Cash Back"
  },
  {
    "id": "116778",
    "url": "https://product-images.ibotta.com/offer/9gG3wuyxPAfF_inC6ztbpg-normal.png",
    "name": "Odwalla®",
    "description": "Any variety - 15.2 fl. oz. bottle only",
    "terms": "Rebate valid on Odwalla® for any variety, 15.2 fl. oz. bottle only.",
    "current_value": "$0.75 Cash Back"
  },
  {
    "id": "116371",
    "url": "https://product-images.ibotta.com/offer/2s8Z3-FMCjwFu3tai0C4zQ-normal.png",
    "name": "Seventh Generation™ Auto Dish Soap",
    "description": "Any variety - Select sizes. Exclusions apply.",
    "terms": "Rebate valid on Seventh Generation™ Auto Dish Soap for any variety, select sizes. Rebate excludes the following size only: \r\n\r\n•8 oz. bottle",
    "current_value": "$1.50 Cash Back"
  },
  {
    "id": "118050",
    "url": "https://product-images.ibotta.com/offer/3eJKvvrna690BVo50Q2B9g-normal.png",
    "name": "Brummel & Brown® Organic",
    "description": "Any variety - Any size",
    "terms": "Rebate valid on Brummel & Brown® Organic for any variety, any size.",
    "current_value": "$2.00 Cash Back"
  },
  {
    "id": "118157",
    "url": "https://product-images.ibotta.com/offer/e8MXnI0GGsty9pKCBdEIIQ-normal.png",
    "name": "MOTRIN®",
    "description": "Select varieties - 20 ct. pack or larger. See rebate details.",
    "terms": "Rebate valid on the following MOTRIN® varieties, 20 ct. pack or larger:\r\n\r\n•Motrin® IB\r\n•Motrin® IB Liquid Gels\r\n•Motrin® PM\r\n\r\nUse products as directed.",
    "current_value": "$1.50 Cash Back"
  },
  {
    "id": "118604",
    "url": "https://product-images.ibotta.com/offer/Fy40APGOPyjMzoCFPjSaag-normal.png",
    "name": "Pretzels - Any Brand",
    "description": "Valid on Any Brand Pretzels",
    "terms": "Rebate excludes:\r\n\r\n• Stuffed pretzels\r\n• Dipped or coated pretzels\r\n• Soft pretzels\r\n• Snack mixes",
    "current_value": "$0.25 Cash Back"
  },
  {
    "id": "118607",
    "url": "https://product-images.ibotta.com/offer/8QvDP1YxyRLmeQm2WkDIDA-normal.png",
    "name": "A to Z Wineworks",
    "description": "Buy 2 - Any variety - 750 ml. bottle",
    "terms": "Rebate valid on A to Z Wineworks. Buy 2 of any variety, 750 ml. bottle.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$3.00 Cash Back"
  },
  {
    "id": "118689",
    "url": "https://product-images.ibotta.com/offer/pMcbvpZRsvn4OCPf6hpZoA-normal.png",
    "name": "Grape Nuts®",
    "description": "Buy 2 - Any variety - Any size",
    "terms": "Rebate valid on Grape Nuts®. Buy 2 of any variety, any size.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$1.75 Cash Back"
  },
  {
    "id": "118697",
    "url": "https://product-images.ibotta.com/offer/o1Mf-6trDT6m-VIIIu3dVQ-normal.png",
    "name": "Fruity Pebbles™",
    "description": "Buy 2 - Any variety - Any size",
    "terms": "Rebate valid on Fruity Pebbles™. Buy 2 of any variety, any size.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$1.75 Cash Back"
  },
  {
    "id": "118705",
    "url": "https://product-images.ibotta.com/offer/HbaW_HKiAB4Vas9XBbhCvw-normal.png",
    "name": "Post® Shredded Wheat",
    "description": "Buy 2 - Any variety - Any size. Exclusions apply.",
    "terms": "Rebate valid on Post® Shredded Wheat. Buy 2 of any variety, any size. \r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate. \r\n\r\nRebate excludes the following varieties: \r\n\r\n• Frosted S'mores\r\n• Frosted Cinnamon \r\n• Frosted Mixed Berry",
    "current_value": "$1.75 Cash Back"
  },
  {
    "id": "118710",
    "url": "https://product-images.ibotta.com/offer/icdYxHq5B5URkAypgAsxqw-normal.png",
    "name": "Great Grains®",
    "description": "Buy 2 - Any variety - Any size. Exclusions Apply.",
    "terms": "Rebate valid on Great Grains®. Buy 2 of any variety, any size.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.\r\n\r\nRebate excludes the following varieties: \r\n\r\n• Banana Nut Crunch\r\n• Cranberry Almond\r\n• Crunchy Pecan",
    "current_value": "$1.75 Cash Back"
  },
  {
    "id": "118726",
    "url": "https://product-images.ibotta.com/offer/USj9GyQiaGpX9tTrD2RReQ-normal.png",
    "name": "Post® Raisin Bran",
    "description": "Buy 2 - Any variety - Any size",
    "terms": "Rebate valid on Post® Raisin Bran. Buy 2 of any variety, any size. \r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$1.75 Cash Back"
  },
  {
    "id": "118798",
    "url": "https://product-images.ibotta.com/offer/KYFC2mHd8ZopmGaX2yPnpA-normal.png",
    "name": "Alpha-Bits®",
    "description": "Buy 2 - Any variety - Any size",
    "terms": "Rebate valid on Alpha-Bits®. Buy 2 of any variety, any size.\r\n\r\nBoth products must be purchased on the same receipt to receive credit for this rebate.",
    "current_value": "$1.75 Cash Back"
  },
  {
    "id": "121231",
    "url": "https://product-images.ibotta.com/offer/Jp9DuC4ASBrwK-6mmV3sow-normal.png",
    "name": "Trail's End",
    "description": "750 ml. bottle",
    "terms": "Rebate valid on Trail's End, 750 ml. bottle.",
    "current_value": "$10.00 Cash Back"
  },
  {
    "id": "117771",
    "url": "https://product-images.ibotta.com/offer/R8PgDvoPsfjtancvsKNdZw-normal.png",
    "name": "NUK® Simply Natural™ Bottles",
    "description": "3 pk. - 5 or 9 oz. bottles",
    "terms": "Rebate valid on NUK® Simply Natural™ Bottles for 3 pk, 5 or 9 oz. bottles.",
    "current_value": "$3.75 Cash Back"
  },
  {
    "id": "119738",
    "url": "https://product-images.ibotta.com/offer/jc8m4DqJMrSm7zBOkKALKA-normal.png",
    "name": "Quaker Life® Cereal",
    "description": "Any variety - 18 oz. box or larger",
    "terms": "Rebate valid on Quaker Life® Cereal for any variety, 18 oz. box or larger.",
    "current_value": "$1.00 Cash Back"
  }
]
"""

def home(request):
    return HttpResponse(json)
