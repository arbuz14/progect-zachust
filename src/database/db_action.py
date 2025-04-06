from uuid import uuid4

from src.database.base import db
from src.database.models import Product, Review, User


def get_products():
    return db.session.query(Product).all()


def get_product(product_id: str):
    return Product.query.filter_by(id=product_id).one_or_404()


def add_product(name: str, description: str, price: float, img_url: str):
    product = Product(
        id=uuid4().hex,
        name=name,
        description=description,
        price=price,
        img_url=img_url
    )

    db.session.add(product)
    db.session.commit()
    return f"Товар '{name}' успішно додано"

def delete_product(product_id: str):
    product = Product.query.filter_by(id=product_id).one_or_404()
    db.session.delete(product)
    db.session.commit()
    return f"Товар '{product_id}' успішно додано"


def update_product(product_id: str, name: str, description: str, price: float, img_url: str) -> str:
    product = Product.query.filter_by(id = product_id).one_or_404()
    product.name = name
    product.description = description
    product.price = price
    product.img_url = img_url
    db.session.commit()
    return f"Товар з id '{product_id}' успішно додано"

def add_review_product(product_id: str, text: str):
    review = Review(id=uuid4().hex, text=text)
    product = Product.query.filter_by(id=product_id).one_or_404()
    product.reviews.append(review)
    db.session.commit()
    return "Відгук успішно додано"

def buy_product(product_id: str, name: str) -> str:
    product = Product.query.filter_by(id=product_id).one_or_404()
    
    user = User.query.filter_by(name=name).first()
    
    if not user:
        user = User(id=str(uuid4()), name=name)  
        db.session.add(user)  # Додаємо нового користувача до сесії

    if user not in product.users:  # Перевіряємо, чи вже є зв'язок у багатьох-до-багатьох
        product.users.append(user)

    db.session.commit()
    
    return f"Користувач {name} успішно купив товар {product.name}"