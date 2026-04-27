n, d = map(int, input().split())
hashtag = {
    1: 'TechTrends',
    2: 'EcoLife',
    3: 'FoodieHeaven',
    4: 'FashionWeek',
    5: 'HealthyLiving',
}

hashtag_data = []
max_total = -1
top_performer = ""

for _ in range(n):
    data = list(map(int, input().split()))
    h_id = data[0]
    name = hashtag[h_id]
    usage = data[1:]
    total_usage = sum(usage)
    average_usage = total_usage / d
    
    if usage[-1] > usage[0]:
        trend = "GROWING"
    elif usage[-1] < usage[0]:
        trend = "DECLINING"
    else:
        trend = "STABLE"
    
    hashtag_data.append({
        'name': name,
        'total': total_usage,
        'average': average_usage,
        'trend': trend
    })
    
    if total_usage > max_total:
        max_total = total_usage
        top_performer = name

# Print all hashtags
for data in hashtag_data:
    print(f"{data['name']}: {data['total']} total, {data['average']:.2f} avg, {data['trend']}")

# Print top performer
print(f"Top performer: {top_performer}")