D = [
    {"id": 100001, "p-num": "101", "user-meta": [
        {"f-name": "FirstName 1"},
        {"l-name": "LastName 1"},
        {"comp": "CompanyName 1"},
        {"s-num": "102"},
        {"s-num": "103"},
        {"s-num": "104"},
    ]},
    {"id": 100002, "p-num": "201", "user-meta": [
        {"f-name": "FirstName 2"},
        {"l-name": "LastName 2"},
    ]},
    {"id": 100003, "p-num": "301", "user-meta": [
        {"f-name": "FirstName 3"},
        {"l-name": "LastName 3"},
        {"s-num": "302"},
    ]}
]

X = {
    "p-num": "Primary Number",
    "s-num": "Number",
    "f-name": "First Name",
    "l-name": "Last Name",
    "comp": "Company",
    "id": "ID"
}

for user in D:
    print("-" * 50)
    for key in user.keys():
        if key != "user-meta":
            print(X[key], ": ", user[key])
    print("------------")
    print("Contact Info")
    print("------------")
    for item in user["user-meta"]:
        for key, value in item.items():
            print("--->", X[key], ": ", value)
