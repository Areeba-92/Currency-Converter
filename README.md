#  Currency Converter

A simple **currency converter** built in Python that uses **USD as the base reference**.  
It works without internet, supports multiple currencies, and is designed to be **user-friendly, scalable, and readable**.

---

## ✨ Features
-  Works without internet (no API required)  .
-  Supports conversion between multiple currencies.  
-  Input by **currency code (USD, EUR, PKR)** or **currency symbol ($, €, ₨)**  .
-  Displays **conversion history (last 5 conversions)**  .
-  Well-formatted output with commas for readability  .
-  Exit anytime with `"exit"` command  .

---

## 💱 Supported Currencies
| Code | Currency Name       | Symbol |
|------|---------------------|--------|
| USD  | US Dollar           | $      |
| EUR  | Euro                | €      |
| GBP  | British Pound       | £      |
| PKR  | Pakistani Rupee     | ₨      |
| INR  | Indian Rupee        | ₹      |
| JPY  | Japanese Yen        | ¥      |
| SAR  | Saudi Riyal         | ﷼      |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/currency-converter.git
cd currency-converter
```
### 2️⃣ Run the Program
python currency_converter.py

## Example
```
🌍 Welcome to the Currency Converter 🌍
You can convert between the following currencies (or type 'exit' anytime):

 USD - US Dollar ($)
 EUR - Euro (€)
 GBP - British Pound (£)
 PKR - Pakistani Rupee (₨)
 INR - Indian Rupee (₹)
 JPY - Japanese Yen (¥)
 SAR - Saudi Riyal (﷼)

Enter the currency you want to convert FROM: USD
Enter the currency you want to convert TO: PKR
Enter the amount in USD (US Dollar): 10

📊 Conversion Result:
 10.00 USD (US Dollar, $)
    = 2,775.00 PKR (Pakistani Rupee, ₨) ✅
 💱 Exchange Rate: 1 USD = 277.5000 PKR

📝 Recent Conversions:
 - 10.00 USD → 2,775.00 PKR

➡️ Convert again? (y/n): n

👋 Thank you for using the Currency Converter. Goodbye!

```
🛠️ Requirements

- Python 3.6+

- No external libraries required (pure Python)



