"""
E-commerce Marketplace Data Generator
Creates realistic marketplace data with embedded insights
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# Configuration
n_sellers = 150
n_products = 2000
n_orders = 10000
n_reviews = 6500

# Date range: 18 months of data
end_date = datetime(2024, 1, 31)
start_date = end_date - timedelta(days=540)

print("🏪 Generating Marketplace Dataset...")
print(f"Timeline: {start_date.date()} to {end_date.date()}")

# ============= SELLERS =============
print("\n📊 Creating sellers...")

seller_tiers = ['bronze', 'silver', 'gold', 'platinum']
seller_tier_weights = [0.5, 0.3, 0.15, 0.05]

sellers = pd.DataFrame({
    'seller_id': [f'S{i:04d}' for i in range(1, n_sellers + 1)],
    'seller_name': [f'Seller_{i}' for i in range(1, n_sellers + 1)],
    'tier': np.random.choice(seller_tiers, n_sellers, p=seller_tier_weights),
    'join_date': [start_date + timedelta(days=np.random.randint(0, 400)) for _ in range(n_sellers)],
    'country': np.random.choice(['US', 'UK', 'CA', 'AU', 'DE'], n_sellers, p=[0.45, 0.25, 0.15, 0.10, 0.05]),
    'verified': np.random.choice([True, False], n_sellers, p=[0.7, 0.3])
})

# Calculate seller tenure
sellers['tenure_days'] = (end_date - sellers['join_date']).dt.days

print(f"  ✓ {len(sellers)} sellers created")
print(f"    Tiers: {sellers['tier'].value_counts().to_dict()}")

# ============= PRODUCTS =============
print("\n📦 Creating products...")

categories = ['Electronics', 'Home & Garden', 'Fashion', 'Art & Crafts', 'Jewelry', 
              'Toys & Games', 'Beauty', 'Sports', 'Books', 'Food & Beverage']

products = pd.DataFrame({
    'product_id': [f'P{i:05d}' for i in range(1, n_products + 1)],
    'seller_id': np.random.choice(sellers['seller_id'], n_products),
    'category': np.random.choice(categories, n_products),
    'base_price': np.random.lognormal(3.5, 0.8, n_products),  # Log-normal for realistic price distribution
    'listing_date': [start_date + timedelta(days=np.random.randint(0, 450)) for _ in range(n_products)],
})

# Add tier-based quality indicators
products = products.merge(sellers[['seller_id', 'tier']], on='seller_id')

# INSIGHT 1: Higher tier sellers have better quality products (hidden pattern)
tier_quality_boost = {'bronze': 0, 'silver': 0.5, 'gold': 1.0, 'platinum': 1.5}
products['quality_score'] = np.random.uniform(6, 8, n_products) + products['tier'].map(tier_quality_boost)
products['quality_score'] = products['quality_score'].clip(1, 10)

# Price varies by category
category_price_multiplier = {
    'Electronics': 1.8, 'Jewelry': 2.2, 'Fashion': 1.0, 'Art & Crafts': 0.9,
    'Home & Garden': 1.1, 'Toys & Games': 0.8, 'Beauty': 1.0, 
    'Sports': 1.3, 'Books': 0.5, 'Food & Beverage': 0.7
}
products['price'] = products['base_price'] * products['category'].map(category_price_multiplier)
products['price'] = products['price'].round(2)

products = products.drop(['base_price', 'tier'], axis=1)

print(f"  ✓ {len(products)} products created")
print(f"    Categories: {products['category'].nunique()}")

# ============= ORDERS =============
print("\n🛒 Creating orders...")

# INSIGHT 2: Weekends and holidays have different patterns
def generate_order_dates(n, start, end):
    dates = []
    for _ in range(n):
        # Bias towards weekends (Saturday/Sunday)
        if np.random.random() < 0.35:  # 35% weekend orders
            date = start + timedelta(days=np.random.randint(0, (end - start).days))
            # Adjust to weekend
            weekday = date.weekday()
            if weekday < 5:
                date += timedelta(days=(5 - weekday) + np.random.randint(0, 2))
        else:
            date = start + timedelta(days=np.random.randint(0, (end - start).days))
        dates.append(date)
    return dates

order_dates = generate_order_dates(n_orders, start_date, end_date)

orders = pd.DataFrame({
    'order_id': [f'O{i:06d}' for i in range(1, n_orders + 1)],
    'product_id': np.random.choice(products['product_id'], n_orders),
    'order_date': order_dates,
    'quantity': np.random.choice([1, 1, 1, 1, 2, 2, 3], n_orders),  # Most orders are single item
})

# Merge with product info
orders = orders.merge(products[['product_id', 'price', 'quality_score', 'seller_id', 'category']], on='product_id')
orders['revenue'] = (orders['price'] * orders['quantity']).round(2)

# INSIGHT 3: Higher quality products have lower return rates
base_return_rate = 0.12
orders['returned'] = (np.random.random(n_orders) < (base_return_rate - (orders['quality_score'] - 7) * 0.02)).astype(bool)

# Add shipping time (quality affects fulfillment speed)
orders['shipping_days'] = np.random.poisson(5, n_orders) - (orders['quality_score'] - 7).clip(0, 3).astype(int)
orders['shipping_days'] = orders['shipping_days'].clip(2, 15)

# Customer segments
orders['customer_segment'] = np.random.choice(['New', 'Returning', 'VIP'], n_orders, p=[0.4, 0.45, 0.15])

# INSIGHT 4: VIP customers buy higher-priced items
price_boost = {'New': 1.0, 'Returning': 1.15, 'VIP': 1.4}
orders['adjusted_price'] = orders['price']
for segment, boost in price_boost.items():
    mask = orders['customer_segment'] == segment
    orders.loc[mask, 'adjusted_price'] = orders.loc[mask, 'price'] * boost

# Use adjusted price for revenue
orders['revenue'] = (orders['adjusted_price'] * orders['quantity']).round(2)
orders = orders.drop(['adjusted_price', 'quality_score'], axis=1)

print(f"  ✓ {len(orders)} orders created")
print(f"    Revenue: ${orders['revenue'].sum():,.2f}")

# ============= REVIEWS =============
print("\n⭐ Creating reviews...")

# Sample orders that will have reviews (not all orders get reviewed)
reviewed_orders = orders.sample(n_reviews, random_state=42)

reviews = pd.DataFrame({
    'review_id': [f'R{i:06d}' for i in range(1, n_reviews + 1)],
    'order_id': reviewed_orders['order_id'].values,
    'product_id': reviewed_orders['product_id'].values,
    'seller_id': reviewed_orders['seller_id'].values,
})

# Merge quality score back
reviews = reviews.merge(products[['product_id', 'quality_score', 'category']], on='product_id')

# INSIGHT 5: Rating correlates with quality but has noise
reviews['rating'] = (reviews['quality_score'] * 0.5 + np.random.normal(2.5, 1.2, n_reviews)).clip(1, 5).round()

# Review dates slightly after order dates
reviews = reviews.merge(orders[['order_id', 'order_date']], on='order_id')
reviews['review_date'] = reviews['order_date'] + pd.to_timedelta(np.random.randint(1, 30, n_reviews), unit='D')

# Response time (better sellers respond faster)
reviews = reviews.merge(sellers[['seller_id', 'tier']], on='seller_id')
tier_response_speed = {'bronze': 10, 'silver': 7, 'gold': 4, 'platinum': 2}
reviews['seller_response_days'] = reviews['tier'].map(tier_response_speed) + np.random.randint(-2, 5, n_reviews)
reviews['seller_response_days'] = reviews['seller_response_days'].clip(0, 20)
reviews['has_seller_response'] = reviews['seller_response_days'] < 8

# Helpful votes (better ratings get more helpful votes)
reviews['helpful_votes'] = (reviews['rating'] * 2 + np.random.poisson(3, n_reviews)).clip(0, 50)

reviews = reviews.drop(['quality_score', 'tier', 'order_date'], axis=1)

print(f"  ✓ {len(reviews)} reviews created")
print(f"    Avg rating: {reviews['rating'].mean():.2f}")

# ============= SAVE DATA =============
print("\n💾 Saving datasets...")

sellers.to_csv('/home/claude/sellers.csv', index=False)
products.to_csv('/home/claude/products.csv', index=False)
orders.to_csv('/home/claude/orders.csv', index=False)
reviews.to_csv('/home/claude/reviews.csv', index=False)

print("\n✅ Dataset generation complete!")
print("\n📁 Files created:")
print("   - sellers.csv")
print("   - products.csv")
print("   - orders.csv")
print("   - reviews.csv")

print("\n🔍 Hidden insights embedded:")
print("   1. Seller tier quality premium")
print("   2. Weekend/weekday purchase patterns")
print("   3. Quality-returns correlation")
print("   4. Customer segment value differences")
print("   5. Rating-quality relationships")
print("\n🎯 Ready for exploration!")
