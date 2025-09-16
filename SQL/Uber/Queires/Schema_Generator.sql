CREATE DATABASE uber_clone;
USE uber_clone;
CREATE TABLE Locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    city VARCHAR(255) NOT NULL,
    region VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(50) UNIQUE NOT NULL,
    user_type ENUM('Rider', 'Driver') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    location_id INT,
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

CREATE TABLE Vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT NOT NULL,
    make VARCHAR(255),
    model VARCHAR(255),
    year INT,
    license_plate VARCHAR(255) UNIQUE,
    vehicle_type ENUM('UberX', 'UberPool', 'UberBlack'),
    capacity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (driver_id) REFERENCES Users(user_id)
);

CREATE TABLE Trips (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    driver_id INT NOT NULL,
    start_location_id INT NOT NULL,
    end_location_id INT NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    trip_type ENUM('UberX', 'UberPool', 'UberBlack'),
    fare DECIMAL(10,2),
    distance_km DECIMAL(10,2),
    rating DECIMAL(3,2),
    status ENUM('Completed', 'Cancelled', 'No Show'),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (driver_id) REFERENCES Users(user_id),
    FOREIGN KEY (start_location_id) REFERENCES Locations(location_id),
    FOREIGN KEY (end_location_id) REFERENCES Locations(location_id)
);

CREATE TABLE Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT NOT NULL,
    amount DECIMAL(10,2),
    payment_method ENUM('Credit Card', 'Cash', 'PayPal'),
    payment_status ENUM('Completed', 'Pending', 'Failed'),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trip_id) REFERENCES Trips(trip_id)
);

CREATE TABLE Promotions (
    promotion_id INT AUTO_INCREMENT PRIMARY KEY,
    promo_code VARCHAR(255) UNIQUE NOT NULL,
    discount_percentage DECIMAL(5,2),
    valid_from TIMESTAMP,
    valid_until TIMESTAMP,
    applies_to_trip_types JSON
);

CREATE TABLE Driver_Performance (
    performance_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT NOT NULL,
    trip_count INT,
    average_rating DECIMAL(3,2),
    cancellation_rate DECIMAL(5,2),
    complaints_count INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (driver_id) REFERENCES Users(user_id)
);

CREATE TABLE Surge_Pricing (
    surge_id INT AUTO_INCREMENT PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    surge_multiplier DECIMAL(5,2),
    location_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);
