from orders.models import Order

def add_order():
    Order.objects.create()


def get_all_objects(model):
    print('Logging')
    return model.objects.all()

def filter_objects(model, user, **kwargs):
    return model.objects.filter(user=user, **kwargs)

