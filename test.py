data = [{
    "property": "state__id",
    "value": 5,
    "stage": 1
}]

stages = {}

for expression in data:
    stage = stages.get(expression.get('stage'), [])
    stage.append(expression.get('stage'))
    print(stage)

    
