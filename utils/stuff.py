import json

def process_data_disk_tab_separated_file():
    with open("raw_dd_data.txt", 'r') as f:
        lines = f.readlines()
        rows = list(map(lambda l: l.split("\t"), lines))

    output = []
    for row in rows:
        output.append({
            'equippedStatus': row[0],
            'type': row[1],
            'cost': row[2],
            'rarity': row[3],
            'name': row[4],
            'description': row[5]
        })

    with open("dd_data.json", 'w') as f:
        json.dump(output, f, indent = 4)

def process_feat_tab_separated_file():
    with open("raw_feat_data.txt", 'r') as f:
        lines = f.readlines()
        rows = list(map(lambda l: l.split("\t"), lines))

    output = []
    for row in rows:
        if row[0] == "Completed":
            continue
        output.append({
            'completed': row[0],
            'sector': row[1],
            'kind': row[2],
            'description': row[3],
            'reward': row[4],
        })

    with open("feat_data.json", 'w') as f:
        json.dump(output, f, indent = 4)

process_feat_tab_separated_file()
