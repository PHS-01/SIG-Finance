def report_category(transactions, categories):
    totals = {
        "income": {
            "Total" : 0
        },
        "expense": {
            "Total" : 0
        }
    }

    for item in transactions.values():
        type = item.get("type")
        cat_name = categories.get(item.get("category_id")).get("name")
        if cat_name in totals[type].keys():
            totals[type].update({cat_name : (item.get("value")+totals[type][cat_name])})
        else:
            totals[type].update({cat_name : item.get("value")})
        
        totals[type].update({"Total" : (totals[type]["Total"]+item.get("value"))})

    return totals
    

def report_period(transactions):
    totals = {
        "income": {
            "Total" : 0
        },
        "expense": {
            "Total" : 0
        }
    }

    for item in transactions.values():
        type = item.get("type")
        date = item.get("date")[:7]
        if date in totals[type].keys():
            totals[type].update({date : (item.get("value")+totals[type][date])})
        else:
            totals[type].update({date : item.get("value")})
        
        totals[type].update({"Total" : (totals[type]["Total"]+item.get("value"))})

    return totals

def report_total_balance(transactions):
    totals = {
        "income": {
            "Total" : 0
        },
        "expense": {
            "Total" : 0
        }
    }

    for item in transactions.values():
        type = item.get("type")
        totals[type].update({"Total" : (totals[type]["Total"]+item.get("value"))})

    balance = totals["income"]["Total"] - totals["expense"]["Total"]

    return balance