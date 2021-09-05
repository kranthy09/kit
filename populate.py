# fruits_form
#     brands
#     items for each brand

from essentails.models import Brand, Form, Item
fruits_form = Form.objects.create(name="Fruits Form",status="Live",description="fruits form")
fruits_form.save()

simla = Brand(
    name="Simla",
    description="An Apple brand",
    is_available=True
)
simla.save()
mothichur = Brand(
    name="Mothichur",
    description="An Apple brand",
    is_available=True
)
mothichur.save()
alwal = Brand(
    name="Alwal",
    description="A multi fruit brand",
    is_available=True
)
alwal.save()
jingar = Brand(
    name="Jingar",
    description="A multi fruit brand",
    is_available=True
)
jingar.save()
dosthi = Brand(
    name="Dosthi Fruits",
    description="Dry Fruits brand",
    is_available=True
)
dosthi.save()

simla_apple = Item.objects.create(
    name="Apple",
    category="Seasonal",
    brand=simla,
    form=fruits_form,
    quantity=10,
    price=45,
    is_available=True
)
apple.save()


mothichur_apple = Item.objects.create(
    name="Apple",
    category="Seasonal",
    brand=mothichur,
    form=fruits_form,
    quantity=10,
    price=43,
    is_available=True
),
alwal_grapes = Item.objects.create(
    name="grapes",
    category="Non-Seasonal",
    brand=alwal,
    form=fruits_form,
    quantity=8,
    price=35,
    is_available=True
),
jingar_sapota = Item.objects.create(
    name="sapota",
    category="Non-Seasonal",
    brand=jingar,
    form=fruits_form,
    quantity=10,
    price=80,
    is_available=True
),
dosthi_mango = Item.objects.create(
    name="Mango",
    category="Seasonal",
    brand=dosthi,
    form=fruits_form,
    quantity=20,
    price=75,
    is_available=True
),
dosthi_carrot = Item.objects.create(
    name="carrot",
    category="Regular",
    brand=dosthi,
    form=fruits_form,
    quantity=15,
    price=15,
    is_available=True
),
jingar_papaya = Item.objects.create(
    name="papaya",
    category="Regular",
    brand=jingar,
    form=fruits_form,
    quantity=20,
    price=60,
    is_available=True
),
mothichur_green_apple = Item.objects.create(
    name="Green Apple",
    category="Seasonal",
    brand=mothichur,
    form=fruits_form,
    quantity=10,
    price=45,
    is_available=True
),
simla_green_apple = Item.objects.create(
    name="Green Apple",
    category="Seasonal",
    brand=simla,
    form=fruits_form,
    quantity=15,
    price=55,
    is_available=True
)