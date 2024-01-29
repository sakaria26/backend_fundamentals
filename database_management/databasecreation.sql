create table restaurant_address(
	id int not null primary key identity(100,1),
	building_number int not null,
	street varchar(100) not null,
	city varchar(100) not null,
	country varchar(100) not null
);

create table restaurant(
	id int not null primary key identity(100,1),
	restaurant_name varchar(150) not null,
	phone_number varchar(20) not null,
	address_id int not null,
	constraint fk_restaurant_address foreign key (address_id) references restaurant_address
);


create table waiter(
	id int not null primary key identity(100,1),
	firstname varchar(100) not null,
	lastname varchar(100) not null,
	phone_number varchar(20)
);

create table reservation(
	id int not null primary key identity(100,1),
	title varchar(150) not null,
	reservation_date date not null,
	start_time time not null,
	party_size int not null,
	contact_number varchar(20) not null,
	table_number int not null,
	restaurant_id int not null,
	waiter_id int not null,
	constraint fk_reservation_restaurant foreign key (restaurant_id) references restaurant,
	constraint fk_reservation_waiter foreign key (waiter_id) references waiter
);

create table dish(
	id int not null primary key identity(100,1),
	dish_name varchar(100) not null,
	price decimal(10,2) not null,
	restaurant_id int not null,
	constraint fk_dish_restaurant foreign key (restaurant_id) references restaurant
);

create table bill(
	id int not null primary key identity(100,1),
	reservation int not null,
	total decimal(10,2) not null
);

create table bill_dish(
	bill_id int not null,
	dish_id int not null,
	constraint fk_bill foreign key (bill_id) references bill,
	constraint fk_dish foreign key (dish_id) references dish
);