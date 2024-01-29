-- Entering Sample Data Into Restaurant_Address
insert into restaurant_address
(building_number, street, city, country)
values
(5, 'Independence Avenue', 'Windhoek', 'Namibia'),
(40, 'Aambeeld', 'Windhoek', 'South Africa');

-- Entering Sample Data Into Restaurant
insert into restaurant
(restaurant_name, phone_number, address_id)
values
('Rolling Flash Trattoria', '+264613099980', 100),
('Rising Peak Restaurant', '+275402309', 101);

-- Entering Sample Data Into Waiter
insert into waiter
(firstname, lastname, phone_number)
values
('John', 'Doe', '+264811122334');

-- Entering Sample Data Into Reservation
insert into reservation
(title, reservation_date, start_time, party_size, contact_number, table_number, restaurant_id, waiter_id)
values
('Sara Fischer', '2025-01-30', '20:00:00', 5, '+264813027483', 10, 100, 100);

-- Entering Sample Data Into Dish
insert into dish
(dish_name, price, restaurant_id)
values
('Grouse and tofu panini', 2199.99, 100),
('Grouse and apple ciabatta', 2599.99, 100),
('Grouse and gruyere toastie', 199.99, 100),
('Grouse and parmesan bagel', 299.99, 100),
('Turkey and chicken panini', 399.99, 101),
('Cheese and crayfish panini', 219.99, 101),
('Ham and black pepper toastie', 99.99, 101),
('Chicken and parmesan ciabatta', 299.99, 101);

-- Entering Sample Data Into Bill
insert into bill
(reservation, total)
values
(100, 5499.95);

-- Entering Sample Data Into Bill_Dish
insert into bill_dish
(bill_id, dish_id)
values
(100, 100),
(100, 101),
(100, 102),
(100, 102),
(100, 103);