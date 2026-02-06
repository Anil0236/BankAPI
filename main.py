
from fastapi import FastAPI
import random
from datetime import datetime, timedelta
from faker import Faker

app = FastAPI()
fake = Faker()

cities = ["Hyderabad","Bangalore","Chennai","Mumbai","Delhi"]
channels = ["UPI","ATM","Card","NetBanking"]

# -------------------- CUSTOMERS API --------------------
@app.get("/customers")
def get_customers(count: int = 100):
    data = []
    for _ in range(count):
        data.append({
            "customer_id": random.randint(1000,5000),
            "name": fake.name(),
            "age": random.randint(21,70),
            "city": random.choice(cities),
            "income": random.randint(20000,150000),
            "risk_segment": random.choice(["LOW","MEDIUM","HIGH"]),
            "kyc_status": random.choice(["VERIFIED","PENDING"])
        })
    return data


# -------------------- ACCOUNTS API --------------------
@app.get("/accounts")
def get_accounts(count: int = 100):
    data = []
    for _ in range(count):
        data.append({
            "account_id": random.randint(20000,90000),
            "customer_id": random.randint(1000,5000),
            "account_type": random.choice(["Savings","Current"]),
            "balance": random.randint(1000,500000),
            "branch": random.choice(cities),
            "status": random.choice(["ACTIVE","DORMANT"])
        })
    return data


# -------------------- MERCHANTS API --------------------
@app.get("/merchants")
def get_merchants(count: int = 50):
    categories = ["Ecommerce","Food","Travel","Fuel","Shopping"]
    data = []
    for _ in range(count):
        data.append({
            "merchant_id": random.randint(500,900),
            "merchant_name": fake.company(),
            "merchant_category": random.choice(categories),
            "risk_category": random.choice(["LOW","MEDIUM","HIGH"]),
            "city": random.choice(cities)
        })
    return data


# -------------------- TRANSACTIONS API --------------------
@app.get("/transactions")
def get_transactions(count: int = 200):
    data = []
    for _ in range(count):
        amount = random.randint(100,80000)
        data.append({
            "txn_id": random.randint(10000000,99999999),
            "customer_id": random.randint(1000,5000),
            "account_id": random.randint(20000,90000),
            "merchant_id": random.randint(500,900),
            "amount": amount,
            "channel": random.choice(channels),
            "txn_type": random.choice(["DEBIT","CREDIT"]),
            "location": random.choice(cities),
            "status": "SUCCESS",
            "timestamp": str(datetime.now() - timedelta(minutes=random.randint(0,120)))
        })
    return data
