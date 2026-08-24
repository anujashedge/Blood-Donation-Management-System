class BloodRequest:
    def __init__(self, request_id, blood_group, location, priority):
        self.request_id = request_id
        self.blood_group = blood_group
        self.location = location
        self.priority = priority


priority_order = {
    "Critical": 1,
    "High": 2,
    "Normal": 3
}


def prioritize_requests(requests):
    return sorted(
        requests,
        key=lambda request: priority_order[request.priority]
    )


requests = [
    BloodRequest("BR001", "O+", "Kolhapur", "Normal"),
    BloodRequest("BR002", "A+", "Pune", "Critical"),
    BloodRequest("BR003", "B+", "Satara", "High")
]

sorted_requests = prioritize_requests(requests)

print("Blood Requests by Priority:")

for request in sorted_requests:
    print(
        request.request_id,
        request.blood_group,
        request.location,
        request.priority
    )
