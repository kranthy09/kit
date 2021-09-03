# TODO:
# 1. Create five brands
# 2. Create 25 items
# 3. add 5 items to each brand

# 4. add 6 items in each form

# Create 5 Brands

from essentails.models import Brand, Form, Item


brands = Brand.objects.bulk_create(
    Brand(name="Nestle", is_available=True),
    Brand(name="Britania", is_available=True),
    Brand(name="Cadbury", is_available=True),
    Brand(name="Unibic", is_available=True),
)
# 4. Create 4 Forms - Done
snack_form = Form(name="Snacks Form", status="Live")
fruits_form = Form(name="Fruits Form", status="Live")
cloths_form = Form(name="Cloths Form", status="Live")
accom_form = Form(name="Accomidation Kit Form", status="Live")

# For Snacks form Create 5 items

spinash_chips = Item(name="Potato Chips - Spanish Tomato Tango", category="Snacks"),
american_style = Item(name="Potato Chips -  American Style Cream & Onion", category="Snacks"),
mad_angles = Item(name="MAD Angels", category="Snacks"),
rusks = Item(name="Haldiram Rusk", category="Snacks"),
halke_fulke = Item(name="Halke fulke", category="Snacks")

# for each snack item create 3 brands
lays = Brand.objects.create(name="Lays")
bingo = Brand.objects.create(name="Bingo")
haldirams = Brand.objects.create(name="Haldirams")

lays.items.add(spinash_chips, american_style)
bingo.items.add(mad_angles)
haldirams.items.add(rusks, halke_fulke)

snack_form.items.add(spinash_chips, american_style, mad_angles, rusks, halke_fulke)