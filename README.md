# 🏗️ Object-Oriented Programming Activities in Python

## 📘 Description
This project contains **two Python programs** demonstrating core **OOP (Object-Oriented Programming)** concepts:  
1. **Class Design, Inheritance, and Encapsulation**  
2. **Polymorphism Challenge**

Each activity shows how objects, classes, and methods bring real-world concepts to life in Python!

---

## 🧱 Activity 1: Design Your Own Class

### 🎯 Objective
Create a class that represents something real (like a **Smartphone**),  
add attributes and methods, and include **inheritance** and **encapsulation**.

### 📄 File Name
`activity1_class_design.py`

### 🧩 Features
- Uses a base class `Smartphone` and a subclass `GamingPhone`.  
- Demonstrates:
  - **Encapsulation** → private attributes (`__storage`)
  - **Inheritance** → `GamingPhone` extends `Smartphone`
  - **Constructors** → initialize unique values per object

### 🧠 Example Code Snippet
```python
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 85)
phone2 = GamingPhone("ASUS", "ROG Phone 8", "512GB", 90, "Adreno 750")

phone1.call("0712345678")
phone1.charge()
print(f"{phone1.brand} storage: {phone1.get_storage()}")

phone2.play_game("Call of Duty Mobile")
phone2.charge()
