class Management:
    def __init__(self):
        self.Employees = []

    def SoftwareCost(self, softwareId):
        amount = 0
        for emp in self.Employees:
            for device in emp.Devices:
                for software in device.softwares:
                    if software.softwareId == softwareId:
                        amount += software.amount
        return amount

    def Software_In_a_Device(self, deviceId):
        for emp in self.Employees:
            for device in emp.Devices:
                if device.DeviceId == deviceId:
                    return len(device.softwares)
        return 0

    def Software_For_Employee(self, employeeId):
        count = 0
        for emp in self.Employees:
            if emp.employeeId == employeeId:
                for device in emp.Devices:
                    count += len(device.softwares)
        return count

    def Amount_spent_on_Software(self, softwareId):
        total = 0
        for emp in self.Employees:
            for device in emp.Devices:
                for software in device.softwares:
                    if software.softwareId == softwareId:
                        total += software.amount
        return total

    def Amount_spend_for_employee(self, employeeId):
        total = 0
        for emp in self.Employees:
            if emp.employeeId == employeeId:
                for device in emp.Devices:
                    for software in device.softwares:
                        total += software.amount
        return total

    def Amount_spend_on_vendor(self, vendorId):
        total = 0
        for emp in self.Employees:
            for device in emp.Devices:
                for software in device.softwares:
                    if software.vendorId == vendorId:
                        total += software.amount
        return total

    def No_of_Installation_from_vendor(self, vendorId):
        total = 0
        for emp in self.Employees:
            for device in emp.Devices:
                for software in device.softwares:
                    if software.vendorId == vendorId:
                        total += 1
        return total
