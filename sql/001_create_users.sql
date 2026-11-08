-- MySQL 8: tao CSDL va bang users cho chuc nang dang ky / dang nhap
CREATE DATABASE IF NOT EXISTS gia_su_ai CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE gia_su_ai;

CREATE TABLE IF NOT EXISTS users (
  id            INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  full_name     VARCHAR(100) NOT NULL,
  email         VARCHAR(255) NOT NULL,            -- luon luu chu thuong
  password_hash VARCHAR(100) NOT NULL,            -- bcrypt hash, KHONG luu mat khau goc
  role          VARCHAR(20)  NOT NULL DEFAULT 'student',
  status        VARCHAR(20)  NOT NULL DEFAULT 'active',
  created_at    DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_users_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
