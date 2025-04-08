todo = []

while True:
    print("รายการสิ่งที่ต้องทำ")
    print("1. เพิ่มงาน")
    print("2. ดูงาน")
    print("3. ลบงาน")
    print("4. ออกจากโปรแกรม")

    choice = input("เลือกตัวเลือกของคุณ (1-4): ")

    if choice == '1':
        task = input("ป้อนงาน: ")
        todo.append(task)
        print(f"เพิ่มงาน '{task}' แล้ว.")
    elif choice == '2':
        if todo:
            print("Tasks:")
            for i, task in enumerate(todo, start=1):
                print(f"{i}. {task}")
        else:
            print("ไม่มีงานในรายการที่ต้องทำ")
    elif choice == '3':
        if todo:
            task_number = int(input("ป้อนหมายเลขงานที่ต้องการลบ: ")) - 1
            if 0 <= task_number < len(todo):
                removed_task = todo.pop(task_number)
                print(f"ลบงาน '{removed_task}' เรียบรอยแล้ว")
            else:
                print("หมายเลขงานไม่ถูกต้อง")
        else:
            print("ไม่มีงานที่ต้องการลบ")
    elif choice == '4':
        print(" ออกจากโปรแกรม")
        break
    else:
        print("ตัวเลือกไม่ถูกต้อง กรุณาลองอีกครั้ง")
