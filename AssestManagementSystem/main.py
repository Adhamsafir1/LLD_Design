from Employee import Employee
from Device import Device
from software import Software
from Vendor import Vendor
from management import Management

# Initialize management system
mgmt = Management()

# Vendors
vendor1 = Vendor()
vendor2 = Vendor()

# Software installations
software1 = Software("v1", "s1", "2025-12-12", 500)
software2 = Software("v1", "s2", "2026-01-10", 1000)
software3 = Software("v2", "s3", "2025-09-30", 1500)

# Devices
device1 = Device("d1")
device2 = Device("d2")

device1.softwares.extend([software1, software2])
device2.softwares.append(software3)

# Employee
employee1 = Employee("e1")
employee1.Devices.extend([device1, device2])

# Add employee to management
mgmt.Employees.append(employee1)

# Outputs
print("Software in Device d1:", mgmt.Software_In_a_Device("d1"))
print("Total software for Employee e1:", mgmt.Software_For_Employee("e1"))
print("Amount spent on software s1:", mgmt.Amount_spent_on_Software("s1"))
print("Amount spent on vendor v1:", mgmt.Amount_spend_on_vendor("v1"))
print("No. of installations from vendor v1:", mgmt.No_of_Installation_from_vendor("v1"))
print("Total spent by employee e1:", mgmt.Amount_spend_for_employee("e1"))
