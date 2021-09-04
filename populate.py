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
    description="Dry Fruits brand"
)
dosthi.save()

apple = Item.objects.create(
    name="Apple",
    category="Seasonal",
    brand=simla,
    form=fruits_form,
    quantity=10,
    price=45
)
apple.save()
apple.brand.add(simla, mothichur)