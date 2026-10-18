# My_Python

![CI](https://github.com/c-dillon77-byte/My_Python/actions/workflows/ci.yml/badge.svg)

Various Python programs I've written, some for fun and some for everyday use, including tools based on
restaurant operations (food cost and a point-of-sale style receipt).

## Programs

| Program | What it does | Run |
|---|---|---|
| [`cash_register/`](cash_register/cash_register.py) | Command-line cash register: ring up items, per-item tax classes, % or $ discounts, cash or card tender, and a printed 42-column thermal-style receipt | `python cash_register/cash_register.py` |
| [`food_cost/`](food_cost/food_cost.py) | Food cost calculator for two profit centers (Taco and Pizza): COGS and food cost % per center and combined | `python food_cost/food_cost.py` |
| [`calculator/`](calculator/calculator.py) | Menu-driven scientific calculator: arithmetic, powers, roots, logs, trig (degrees or radians), factorial, with input validation | `python calculator/calculator.py` |

All three use only the Python standard library (Python 3.10+).

### Food cost formula
```
COGS        = beginning inventory + purchases (receipts) - ending inventory
Food cost % = COGS / total sales × 100
```
Example: beginning $1,000 + purchases $500 − ending $300 = **$1,200 COGS**. On $4,000 of sales,
that's **30.00%** food cost.

### Sample receipt (cash_register)
```
                DEMO STORE
         THANK YOU FOR SHOPPING!
             123 Example St.
            Anytown, ST 00000
              (555) 555-0100
==========================================
DATE 10/18/2026              TIME 07:31 PM
REG R7                   TRANS 258343-8694
------------------------------------------
BURGER
 2 @ $5.00                          $10.00
  TAX 7.00%                          $0.70

------------------------------------------
SUBTOTAL                            $10.00
TAX                                  $0.70
------------------------------------------
TOTAL                               $10.70
==========================================
TENDER CASH                         $20.00
CHANGE                               $9.30
==========================================
```
The store name and address are placeholders. Edit `STORE_NAME` / `STORE_ADDRESS` at the top of the file.

## Development
```bash
pip install -r requirements-dev.txt
ruff check .
pytest -q
```
Tests cover the food cost math, cash register item/discount/tax totals and receipt layout, and the
calculator's input validation. CI runs lint and tests on every push and pull request.
