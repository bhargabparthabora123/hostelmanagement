class Student:
    def __init__(self, student_id, name, contact, course, admission_date):
        self.id = student_id
        self.name = name
        self.contact = contact
        self.course = course
        self.admission_date = admission_date

    def display_student(self):
        print(f"ID: {self.id}, Name: {self.name}, Contact: {self.contact}, Course: {self.course}, Admission Date: {self.admission_date}")


class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.type = room_type
        self.is_occupied = False

    def allocate(self, student):
        if not self.is_occupied:
            print(f"Allocated Room {self.room_number} to {student.name}")
            self.is_occupied = True
        else:
            print(f"Room {self.room_number} is already occupied.")

    def display_room(self):
        print(f"Room: {self.room_number}, Type: {self.type}, Occupied: {self.is_occupied}")


class Staff:
    def __init__(self, staff_id, name, contact, role):
        self.id = staff_id
        self.name = name
        self.contact = contact
        self.role = role

    def display_staff(self):
        print(f"ID: {self.id}, Name: {self.name}, Contact: {self.contact}, Role: {self.role}")


class Complaint:
    def __init__(self, complaint_id, description, student_id):
        self.id = complaint_id
        self.description = description
        self.student_id = student_id

    def display_complaint(self):
        print(f"Complaint ID: {self.id}, Description: {self.description}, Student ID: {self.student_id}")


class HostelManagementSystem:
    def __init__(self):
        self.students = []
        self.rooms = []
        self.staff = []
        self.complaints = []

    def register_student(self, student):
        self.students.append(student)
        print(f"Student registered: {student.name}")

    def list_students(self):
        print("\n--- Student List ---")
        for s in self.students:
            s.display_student()

    def add_room(self, room):
        self.rooms.append(room)
        print(f"Room added: {room.room_number}")

    def list_rooms(self):
        print("\n--- Room List ---")
        for r in self.rooms:
            r.display_room()

    def allocate_room(self, student_id):
        student = self.get_student_by_id(student_id)
        if student:
            for room in self.rooms:
                if not room.is_occupied:
                    room.allocate(student)
                    return
            print("No available rooms.")
        else:
            print("Student not found.")

    def get_student_by_id(self, student_id):
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Staff added: {staff_member.name}")

    def list_staff(self):
        print("\n--- Staff List ---")
        for s in self.staff:
            s.display_staff()

    def file_complaint(self, complaint):
        self.complaints.append(complaint)
        print(f"Complaint filed: {complaint.id}")

    def list_complaints(self):
        print("\n--- Complaints ---")
        for c in self.complaints:
            c.display_complaint()


def main():
    hms = HostelManagementSystem()

    # Pre-populate some rooms and staff
    hms.add_room(Room(101, "Single"))
    hms.add_room(Room(102, "Double"))
    hms.add_staff(Staff("S001", "Alice", "9876543210", "Warden"))
    hms.add_staff(Staff("S002", "Bob", "9123456789", "Manager"))

    while True:
        print("\n--- Hostel Management System ---")
        print("1. Register Student")
        print("2. List Students")
        print("3. Add Room")
        print("4. List Rooms")
        print("5. Allocate Room to Student")
        print("6. Add Staff")
        print("7. List Staff")
        print("8. File Complaint")
        print("9. List Complaints")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            contact = input("Enter Contact: ")
            course = input("Enter Course: ")
            admission_date = input("Enter Admission Date: ")
            hms.register_student(Student(sid, name, contact, course, admission_date))

        elif choice == "2":
            hms.list_students()

        elif choice == "3":
            room_number = int(input("Enter Room Number: "))
            room_type = input("Enter Room Type: ")
            hms.add_room(Room(room_number, room_type))

        elif choice == "4":
            hms.list_rooms()

        elif choice == "5":
            student_id = input("Enter Student ID for Room Allocation: ")
            hms.allocate_room(student_id)

        elif choice == "6":
            staff_id = input("Enter Staff ID: ")
            name = input("Enter Name: ")
            contact = input("Enter Contact: ")
            role = input("Enter Role: ")
            hms.add_staff(Staff(staff_id, name, contact, role))

        elif choice == "7":
            hms.list_staff()

        elif choice == "8":
            comp_id = input("Enter Complaint ID: ")
            desc = input("Enter Description: ")
            stu_id = input("Enter Student ID: ")
            hms.file_complaint(Complaint(comp_id, desc, stu_id))

        elif choice == "9":
            hms.list_complaints()

        elif choice == "10":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
